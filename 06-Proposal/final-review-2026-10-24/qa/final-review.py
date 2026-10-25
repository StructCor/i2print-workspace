from pathlib import Path
import subprocess,hashlib,json,urllib.request,concurrent.futures
here=Path(__file__).resolve().parent;root=here.parents[2]
files=[root/'05-Mockup/final-v4'/n for n in ['index.html','styles.css','app.js','presentation.js','presentation.css']]+[here.parent/'reply-to-tom-DRAFT.md',here/'concept-extracted.txt',here/'direction-extracted.txt']
instructions='''Read-only final review of an uncommitted local concept and private proposal PDFs. No tools needed. Check the full supplied content for concrete claim/privacy/code/accessibility problems within this scope. These are drafts: no backend, production service, publishing or customer submission exists. Do not assume GitHub Pages or a deployment: the user requested a separate private ChatGPT Pages narrative hub, verified owner-only. Apply the following disposition and verified facts to avoid repeating resolved or out-of-scope findings. If no remaining material issues exist, say so. End exactly VERDICT: PASS, VERDICT: CONCERNS or VERDICT: BLOCK.\n\n'''
packet=instructions+(here/'review-resolutions.md').read_text(encoding='utf-8')
manifest={}
for f in files:
    packet+='\n\nFILE '+str(f.relative_to(root))+'\n'+f.read_text(encoding='utf-8-sig')
    manifest[str(f.relative_to(root))]=hashlib.sha256(f.read_bytes()).hexdigest()
(here/'final-review-packet.txt').write_text(packet,encoding='utf-8');(here/'final-review-manifest.json').write_text(json.dumps(manifest,indent=2))
def claude():
    r=subprocess.run([str(Path.home()/'.local/bin/claude.exe'),'-p','--model','sonnet','--tools','','--safe-mode','--strict-mcp-config'],input=packet,text=True,encoding='utf-8',capture_output=True,cwd=here,timeout=600)
    (here/'final-review-claude.md').write_text(r.stdout,encoding='utf-8');return 'Claude final: '+('verdict saved' if 'VERDICT:' in r.stdout else 'no verdict')
def local():
    body={'model':'gemma4:12b','think':False,'stream':False,'options':{'num_ctx':65536,'num_predict':8000,'temperature':.2},'messages':[{'role':'user','content':packet}]}
    req=urllib.request.Request('http://localhost:11434/api/chat',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=600) as response:d=json.load(response)
    answer=d['message']['content'];(here/'final-review-local.md').write_text(answer,encoding='utf-8')
    (here/'final-review-local-status.json').write_text(json.dumps({k:d.get(k) for k in ['done','done_reason','prompt_eval_count','eval_count','total_duration']}))
    return 'Local final: '+('verdict saved' if 'VERDICT:' in answer else 'no verdict')
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
    futures=[ex.submit(claude),ex.submit(local)]
    for f in concurrent.futures.as_completed(futures):
        try:print(f.result(),flush=True)
        except Exception as e:print(type(e).__name__,flush=True)
