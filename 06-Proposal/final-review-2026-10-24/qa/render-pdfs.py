from pathlib import Path
import pypdfium2 as pdfium
from PIL import Image, ImageDraw
from pypdf import PdfReader
root=Path(__file__).resolve().parent.parent
for kind,name in [('concept','i2Print-Website-Concept.pdf'),('direction','i2Print-Website-and-Automation-Proposal.pdf')]:
    doc=pdfium.PdfDocument(str(root/name)); thumbs=[]
    texts=[]
    for i,p in enumerate(doc):
        im=p.render(scale=1.3).to_pil().convert('RGB'); im.save(root/'qa'/f'{kind}-{i+1:02}.png')
        im.thumbnail((576,620)); tile=Image.new('RGB',(600,660),'#e7e9ef');tile.paste(im,((600-im.width)//2,24));ImageDraw.Draw(tile).text((20,640),f'{kind} / {i+1}',fill='black');thumbs.append(tile)
    for start in range(0,len(thumbs),4):
        sheet=Image.new('RGB',(1200,1320),'white')
        for j,im in enumerate(thumbs[start:start+4]):sheet.paste(im,((j%2)*600,(j//2)*660))
        sheet.save(root/'qa'/f'{kind}-sheet-{start//4+1}.png')
    text='\n\n'.join(f'PAGE {i+1}\n{p.extract_text()}' for i,p in enumerate(PdfReader(root/name).pages))
    (root/'qa'/f'{kind}-extracted.txt').write_text(text,encoding='utf-8')
    print(kind,len(doc),'pages; rendered every page')
