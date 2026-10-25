from pathlib import Path
import json
root=Path(__file__).resolve().parents[3]
p=root/'05-Mockup/kickoff-v3/app.js';s=p.read_text(encoding='utf-8-sig')
changes={
 "if(r==='main')return;":"if(r==='main'){if(main.childElementCount)return;r='home';}",
 "return state.image&&((state.image.height>state.image.width)!==(p.h>p.w))?":"return state.image&&Math.abs(state.image.width-state.image.height)/Math.max(state.image.width,state.image.height)>.02&&((state.image.height>state.image.width)!==(p.h>p.w))?",
 'aria-label="Choose a local image"':'aria-label="Choose an image locally"',
 'BUILDING ON CLAUDE’S MOTION CONCEPTS':'MOTION CONCEPTS',
 'Adapted from the existing CSS/SVG motion direction. No new video engine or AI integration is needed for these small website details.':'Short motion details support the print story. Each has a still alternative when reduced motion is preferred.',
 '<span class="status-icon">':'<span class="sr-only">${type===\'warning\'?\'Warning: \':type===\'bad\'?\'Problem: \':\'Note: \'}</span><span class="status-icon" aria-hidden="true">',
 '<div id="proof-state" aria-live="polite">':'<div id="proof-state" tabindex="-1" aria-live="polite">',
 "state.proof='approved';main.innerHTML=proof();bind()":"state.revision=document.getElementById('revision-notes').value.trim();state.proof='approved';main.innerHTML=proof();bind();document.getElementById('proof-state').focus()",
 "state.proofAccepted=false;main.innerHTML=proof();bind()":"state.proofAccepted=false;main.innerHTML=proof();bind();document.getElementById('proof-state').focus()",
 'clear next steps when something needs attention':'a closer look at the issues the image check flags',
 'Cards, invitations and event details, with space to ask for help choosing the right format.':'Cards and proposed event-printing options, with space to ask for help choosing the right format.',
 'TOM’S AUTOMATION GOALS':'PROPOSED AUTOMATION GOALS',
 "loadId++;state.image=c;":"loadId++;state.image?.close?.();state.image=c;",
 "const current=++loadId;state.image=null;":"const current=++loadId;state.image?.close?.();state.image=null;",
 "if(state.mode==='extend'){ctx.save();":"if(state.mode==='extend'&&'filter' in ctx){ctx.save();",
 "It is not generative AI and may repeat text or shapes at the edge.":"It is not generative AI and may repeat text or shapes at the edge. Browsers without blur support show neutral padding.",
 "<section class=\"section-small\"><div class=\"wrap\"><p class=\"notice\">Short motion":"<section class=\"section-small\"><div class=\"wrap\"><p class=\"motion-static-note notice\">Reduced motion is enabled: the compositions are shown as still images.</p><p class=\"notice\">Short motion",
}
for a,b in changes.items():
    assert a in s,a
    s=s.replace(a,b)
for func in ['detail','quoteSummary','motion','visit']:
    start=s.index('function '+func+'(');end=s.find('\nfunction ',start+10)
    if end<0:end=len(s)
    section=s[start:end].replace('<h3>','<h2>').replace('</h3>','</h2>')
    s=s[:start]+section+s[end:]
p.write_text(s,encoding='utf-8')
css=root/'05-Mockup/kickoff-v3/styles.css';s=css.read_text(encoding='utf-8-sig')
s=s.replace('.motion-stage h3','.motion-stage h2').replace('.registration.run h3','.registration.run h2')
s+='''\n/* Review fixes: visible status text, focus contrast and persistent demo labels. */
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.concept-bar,.footer-note{font-size:12px}.concept-bar :focus-visible,.callout :focus-visible{outline-color:white}
.topic-list h2,.motion-card>h2{font-size:24px;line-height:1.2}.motion-static-note{display:none}
#proof-state:focus{outline:3px solid var(--blue);outline-offset:4px}
@media(prefers-reduced-motion:reduce){[data-replay]{display:none}.motion-static-note{display:block;margin-bottom:20px}}
@media print{.concept-bar{display:block!important;background:white;color:#36333c;font-size:12px;padding:12px}.concept-bar>span:nth-child(2){display:block!important}.concept-bar>a{display:none}}
'''
css.write_text(s,encoding='utf-8')
p=root/'06-Proposal/kickoff-2026-10-24/direction-content.json';d=json.loads(p.read_text(encoding='utf-8-sig'))
bodies=[
 'Prepare campaigns and reorder reminders from an agreed audience, approved offers and permission-based lists. Discovery: which customer groups and channels bring repeat work? Staff approve audiences and messages before sending.',
 'Capture specifications now; later estimate from approved price matrices, minimums, finishing and delivery rules. Discovery: which jobs need exceptions, and who approves them? AI can gather requirements but must not invent prices.',
 'The prototype checks JPG, PNG and WebP dimensions/resolution and demonstrates Fit/Fill. Extend is simulated; PDF preflight and real AI extension are future work. Discovery: which file problems recur? Confirm specifications and require proof approval plus production review.',
 'Prepare job tickets from approved artwork and specifications. Needs: machine requirements, imposition, color and finishing rules. Discovery: where is information re-entered, and what can existing equipment accept? Staff approve release to production.',
 'Prepare shipment details after confirming carriers, packaging, weights and dispatch rules. Discovery: where do shipping errors or delays occur? Staff review before labels are purchased or dispatch is confirmed.'
]
for sec,body in zip(d['pages'][2]['sections'],bodies):sec['body']=body
d['pages'][3]['sections'][1]['body']='Proposed move from OnPrintShop: build and test the new website while current ordering remains in place. Agree how the two connect. Gate: accessible pages, correct content, working links, and an approved launch plan.'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print('Applied scoped review fixes and explicit discovery questions.')
