"""Read-only review of the uncommitted delivery package, using the configured reviewers.
Never invokes the commit-based gate or modifies the repository/review system.
"""
from pathlib import Path
import hashlib,json,os,re,subprocess,concurrent.futures,urllib.request,urllib.error
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
FILES=[ROOT/'05-Mockup/kickoff-v3'/n for n in ['index.html','styles.css','app.js']]
FILES += [HERE.parent/'reply-to-tom-DRAFT.md',HERE/'concept-extracted.txt',HERE/'direction-extracted.txt']
packet='''Review this uncommitted i2Print package for client review. Do not modify files. No tools are available; all reviewed text follows. These are private drafts, not live production. Source images are referenced locally from authorized i2Print assets; no client logos are used and no assets or files are being committed. No email has been sent. No backend, prices, payments, customer database or live AI exists. Tom requested website first, marketing, estimates, file/proof checks, production preparation, shipping, server control, costs and timeline. User approved local demos, two PDFs, draft email and an owner-only Pages review hub. Scope-first cost/schedule; Shopify conditional; server ownership not assumed.
Check unsupported public claims, sensitive contract/developer/dispute references, copyright/attribution, privacy/secrets, broken code, form truthfulness, accessibility, and inaccurate claims of prototype behavior. Current site verifies Long Island City and the About page B2B/B2C/resellers. Business contact addresses are verified from the October 21 thread. All other specs/options are illustrative. Product photos are local-only client-site material; final sharing still needs Daniel approval. Portfolio examples limited to CCP; there are none here.
Browser verification already run: desktop1440 and mobile375 all routes no overflow/broken images; quote card500 and banner96x36 qty3; rejects zero/decimal quantity; state survives back; JPG/PNG/WebP local processing; lowres warning40ppi; portrait600x900 orients2x3.5; invalid image clears preview/disables export; Fit300ppi Fill240ppi; proof requires ack/revision note and resets after placement changes; reduced motion active gives0animations. No console errors. Exports watermarked. All22PDFpages rendered and visually inspected; content here is extracted text, not visual PDF review.
List only concrete findings as [BLOCK], [MAJOR] or [MINOR], file and fix. End exactly VERDICT: PASS, VERDICT: CONCERNS, or VERDICT: BLOCK.
'''
manifest={}
for f in FILES:
    data=f.read_text(encoding='utf-8-sig')
    if re.search(r'ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----',data):raise RuntimeError('Possible secret found: review transmission stopped')
    manifest[str(f.relative_to(ROOT))]=hashlib.sha256(f.read_bytes()).hexdigest()
    packet+='\n\nFILE: '+str(f.relative_to(ROOT))+'\n'+data
(HERE/'review-packet.txt').write_text(packet,encoding='utf-8')
(HERE/'review-manifest.json').write_text(json.dumps(manifest,indent=2))

def claude():
    try:
        r=subprocess.run([str(Path.home()/'.local/bin/claude.exe'),'-p','--model','sonnet','--tools','','--safe-mode','--strict-mcp-config'],input=packet,text=True,encoding='utf-8',capture_output=True,cwd=HERE,timeout=600)
        (HERE/'review-claude.md').write_text(r.stdout,encoding='utf-8')
        (HERE/'review-claude-status.json').write_text(json.dumps({'exit_code':r.returncode,'output_chars':len(r.stdout)}))
        return 'Claude: '+('verdict saved' if 'VERDICT:' in r.stdout else 'no verdict returned')
    except Exception as e:return 'Claude: '+type(e).__name__

def openrouter():
    key=os.environ.get('OPENROUTER_API_KEY')
    if not key:return 'OpenRouter: no configured key'
    body={'model':'z-ai/glm-5.3','temperature':.2,'max_tokens':12000,'reasoning':{'max_tokens':5000},'provider':{'data_collection':'deny'},'usage':{'include':True},'messages':[{'role':'user','content':packet}]}
    try:
        req=urllib.request.Request('https://openrouter.ai/api/v1/chat/completions',data=json.dumps(body).encode(),headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
        with urllib.request.urlopen(req,timeout=600) as response:data=json.load(response)
        answer=data['choices'][0]['message']['content'];(HERE/'review-openrouter.md').write_text(answer,encoding='utf-8')
        (HERE/'review-openrouter-usage.json').write_text(json.dumps({'model':data.get('model'),'usage':data.get('usage')},indent=2))
        return 'OpenRouter: '+('verdict saved' if 'VERDICT:' in answer else 'no verdict returned')
    except urllib.error.HTTPError as e:return 'OpenRouter: HTTP '+str(e.code)
    except Exception as e:return 'OpenRouter: '+type(e).__name__

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
    futures=[ex.submit(claude),ex.submit(openrouter)]
    for future in concurrent.futures.as_completed(futures):print(future.result(),flush=True)
