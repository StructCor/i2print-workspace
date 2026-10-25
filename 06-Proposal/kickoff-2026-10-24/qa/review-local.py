from pathlib import Path
import json,urllib.request
here=Path(__file__).resolve().parent
body={'model':'gemma4:12b','stream':False,'options':{'num_ctx':32768,'num_predict':6144,'temperature':.2},'messages':[{'role':'user','content':(here/'review-packet.txt').read_text(encoding='utf-8')}]}
req=urllib.request.Request('http://localhost:11434/api/chat',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
with urllib.request.urlopen(req,timeout=600) as response:data=json.load(response)
answer=data['message']['content'];(here/'review-local.md').write_text(answer,encoding='utf-8')
print('Local fallback: '+('verdict saved' if 'VERDICT:' in answer else 'no verdict returned'))
