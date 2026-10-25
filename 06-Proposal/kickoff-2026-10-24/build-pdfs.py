"""Rebuild the two local review PDFs from real browser captures and editable copy."""
from pathlib import Path
from xml.sax.saxutils import escape
import json
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
SHOTS=HERE/'screenshots'
pdfmetrics.registerFont(TTFont('Jost',str(ROOT/'05-Mockup/kickoff-v3/fonts/Jost-Variable.ttf')))
INK=HexColor('#36333C'); BLUE=HexColor('#3A62C9'); PALE=HexColor('#F6F8FE'); MUTED=HexColor('#625E68'); ORANGE=HexColor('#FB8500')
LOGO=ROOT/'04-Assets/scraped-2026-10-20/logos/i2printLOGO_FOOTER_02.png'
AUDIT=[]

def para(c,text,x,top,w,size=13,leading=None,color=INK):
    p=Paragraph(escape(text).replace('\n','<br/>'),ParagraphStyle('p',fontName='Jost',fontSize=size,leading=leading or size*1.38,textColor=color))
    _,h=p.wrap(w,2000)
    assert top-h>=34, (text[:55],top,h)
    p.drawOn(c,x,top-h)
    return top-h

def stripe(c,w,y=0):
    for i,col in enumerate(['#00A6D6','#E0007A','#FFD400']):
        c.setFillColor(HexColor(col));c.rect(i*w/3,y,w/3,4,fill=1,stroke=0)

def base(c,n,w,h,title,eyebrow='WEBSITE CONCEPT / PROPOSED'):
    c.setFillColor(white);c.rect(0,0,w,h,fill=1,stroke=0)
    c.drawImage(str(LOGO),40,h-61,width=97,height=31,preserveAspectRatio=True,mask='auto')
    c.setFillColor(MUTED);c.setFont('Jost',10);c.drawRightString(w-40,h-45,'DRAFT · FOR DISCUSSION · 24 OCTOBER 2026')
    para(c,eyebrow,40,h-92,w-80,10,color=BLUE)
    para(c,title,40,h-113,w-80,30,34)
    c.setFillColor(MUTED);c.setFont('Jost',9)
    c.drawString(40,20,'i2Print × RaxaRisk, LLC  /  Daniel Raxa  /  Private review copy')
    c.drawRightString(w-40,20,f'{n:02d}')
    stripe(c,w)

def screen(c,name,x,y,w,h,crop=None):
    im=Image.open(SHOTS/name)
    if crop:im=im.crop(crop)
    iw,ih=im.size;s=min(w/iw,h/ih);dw=iw*s;dh=ih*s
    c.setFillColor(PALE);c.roundRect(x-4,y-4,w+8,h+8,8,fill=1,stroke=0)
    c.drawImage(ImageReader(im),x+(w-dw)/2,y+(h-dh)/2,dw,dh,mask='auto')
    AUDIT.append({'image':name,'native':im.size,'placed':(round(dw),round(dh))})

def notes(c,items,x,top,w):
    for i,(head,body) in enumerate(items,1):
        c.setFillColor(BLUE);c.circle(x+10,top-10,10,fill=1,stroke=0)
        c.setFillColor(white);c.setFont('Jost',10);c.drawCentredString(x+10,top-13,str(i))
        top=para(c,head,x+32,top+1,w-32,15,color=BLUE)-9
        top=para(c,body,x+32,top,w-32,12)-27

def single(c,n,title,shot,items,crop=None):
    W,H=1152,720;base(c,n,W,H,title)
    screen(c,shot,40,79,804,463,crop)
    notes(c,items,873,528,239)
    c.showPage()

def concept():
    W,H=1152,720;c=canvas.Canvas(str(HERE/'i2Print-Website-Concept-DRAFT-v3.pdf'),pagesize=(W,H))
    c.setTitle('i2Print Website Concept — Draft v3');c.setAuthor('Daniel Raxa · RaxaRisk, LLC')
    base(c,1,W,H,'A clearer path from idea to print.','WEBSITE CONCEPT / 14 SCREENS & DECISIONS')
    screen(c,'home-desktop.png',392,80,720,455)
    para(c,'The next i2Print website',40,517,310,31,36,color=BLUE)
    para(c,'A visual conversation about browsing, quoting, checking artwork and reviewing proofs.',40,415,310,18,25)
    para(c,'Prepared for Tom and Lindsay.\nBuilt on the existing concept and initial strategic research.',40,306,310,13)
    para(c,'PROPOSED\nDesign, product options and audience priorities need your input. The local interactions demonstrate a journey; no orders or production jobs are created.',40,208,310,12)
    c.showPage()
    base(c,2,W,H,'One connected customer journey.','SITEMAP / PROPOSED INFORMATION ARCHITECTURE')
    labels=[('01','Explore','Homepage + catalog'),('02','Choose','Cards or banners'),('03','Specify','Guided quote request'),('04','Check','Image + placement'),('05','Review','Simulated proof')]
    for i,(num,head,body) in enumerate(labels):
        x=40+i*216;c.setFillColor(PALE);c.roundRect(x,378,208,148,12,fill=1,stroke=0)
        para(c,num,x+18,509,172,14,color=BLUE);para(c,head,x+18,475,172,24);para(c,body,x+18,433,172,12)
    para(c,'Customer entry points',40,321,315,23,color=BLUE)
    para(c,'Business printing\nPersonal and event printing\nShop and contact\nProduct browsing and guided quotes',40,277,315,16,27)
    para(c,'The shop stays part of the journey',415,321,620,23,color=BLUE)
    para(c,'Quote requests bring specifications together. Staff confirm materials, pricing, timing and fulfillment. A real proof decision and production release belong to a later, validated workflow.',415,276,650,16,24)
    para(c,'OWNER-PENDING  /  Confirm the audience, navigation labels, product families and approval responsibilities during discovery.',415,155,650,12)
    c.showPage()
    single(c,3,'Homepage / a direct invitation to start.','home-desktop.png',[
      ('Two useful next steps','Browse products or begin a guided quote.'),('A recognizable identity','Existing i2Print logo; proposed Jost type, accessible blue and CMY accents.'),('Product-led imagery','Existing i2Print artwork is used locally for discussion; production usage needs approval.')])
    base(c,4,W,H,'The same journey, sized for a phone.','MOBILE / 375-PIXEL VIEWPORT')
    screen(c,'home-mobile-full.png',50,80,242,465,crop=(0,0,375,760))
    screen(c,'home-mobile-full.png',320,80,242,465,crop=(0,760,375,1520))
    notes(c,[('A clear first choice','Large actions and a compact menu keep the entry point simple.'),('Products follow the story','Stacked cards preserve the browsing sequence without horizontal scrolling.'),('Built for more than a mouse','Visible focus, native form controls and reduced-motion support are included in the local concept.')],610,530,455)
    c.showPage()
    single(c,5,'Catalog / find the right starting point.','catalog.png',[
      ('Browse by need','A compact product range and category filters make the next choice visible.'),('Go deeper where it matters','Cards and banners have detailed concept pages and quote paths.'),('Owner-pending','Confirm the launch catalog, product names and available variations.')])
    single(c,6,'Business cards / make the options understandable.','product-cards.png',[
      ('Show the product','Lead with the printed object and a clear purpose.'),('Explain the choices','Dimensions, paper, sides and finishing lead into the quote request.'),('No premature promise','Illustrative options remain subject to shop confirmation; prices and turnaround are absent.')])
    single(c,7,'Banners / start with size and use.','product-banners.png',[
      ('Custom dimensions','A banner flow captures width and height in inches.'),('Useful production context','Material, quantity, finishing and artwork readiness travel with the request.'),('Validate before commerce','Test i2Print’s hardest size-based pricing rules before choosing the store platform.')])
    base(c,8,W,H,'Guided quoting / enough detail for a useful conversation.','INTERACTIVE DEMO / SPECIFICATIONS → PROJECT DETAILS')
    screen(c,'quote-step-1.png',40,180,526,365);screen(c,'quote-step-2.png',586,180,526,365)
    para(c,'01  Your print',40,151,526,17,color=BLUE);para(c,'Choose the product, dimensions, stock, quantity, sides and finishing. Required values are validated.',40,121,526,13)
    para(c,'02  Project details',586,151,526,17,color=BLUE);para(c,'Capture artwork readiness, pickup or shipping preference, requested date and project notes.',586,121,526,13)
    c.showPage()
    single(c,9,'Quote summary / clear details, human-reviewed pricing.','quote-summary.png',[
      ('Check before handoff','Selections are gathered into one reviewable request and can be edited.'),('Pricing remains pending','The demo calculates no price. Future estimates need approved pricing rules and exception handling.'),('Local demonstration','Nothing is submitted, emailed or stored in a customer account.')])
    base(c,10,W,H,'File check / see what Fit and Fill change.','WORKING IMAGE DEMO / JPG · PNG · WEBP')
    screen(c,'file-fit.png',40,206,526,340,crop=(145,365,1275,1095))
    screen(c,'file-fill.png',586,206,526,340,crop=(145,365,1275,1095))
    para(c,'FIT / preserve the full image',40,177,526,18,color=BLUE)
    para(c,'The sample measures 300 effective ppi with padding. A matching resolution target does not certify production readiness.',40,143,526,13)
    para(c,'FILL / cover the area by cropping',586,177,526,18,color=BLUE)
    para(c,'The same sample measures 240 effective ppi and shows a warning. Check the crop and placement before proceeding.',586,143,526,13)
    para(c,'Sample: 900 × 675 px; 3.5 × 2-inch card plus 0.125-inch bleed on each edge. Extend is simulated. PDF preflight, fonts, color checks and real AI extension are future work. Downloads are watermarked.',40,72,1072,11)
    c.showPage()
    single(c,11,'Proof review / make the decision explicit.','proof.png',[
      ('A separate review step','Show the artwork, version and a clear decision state.'),('Approve or request changes','The acknowledgement and revision note are part of the simulated flow.'),('A change resets the decision','New artwork or placement requires another look. These controls cannot authorize production.')],crop=(90,120,1330,1030))
    base(c,12,W,H,'Two audience paths to validate.','PROPOSED / BUSINESS AND PERSONAL PRINTING')
    screen(c,'business.png',40,185,526,365);screen(c,'events.png',586,185,526,365)
    para(c,'Business printing',40,155,526,18,color=BLUE);para(c,'Explore coordinated brand materials and repeat ordering. Confirm priority industries and typical buying patterns.',40,120,526,13)
    para(c,'Personal + event printing',586,155,526,18,color=BLUE);para(c,'Explore occasions, invitations and wedding-related needs. Confirm demand, product fit and whether buyers are direct customers or resellers.',586,120,526,13)
    c.showPage()
    single(c,13,'The shop / bring the conversation back to people.','visit.png',[
      ('A welcoming local identity','Long Island City anchors the concept.'),('An honest visual','The storefront graphic is an illustration, not a photograph of i2Print.'),('Owner-pending','Confirm public contact details, hours, pickup process and approved photography before launch.')])
    base(c,14,W,H,'Three signature moments, with a purpose.','MOTION STORYBOARD / BUILT ON THE EXISTING CONCEPTS')
    screen(c,'motion.png',40,249,1072,300,crop=(150,425,1260,745))
    for i,(head,body) in enumerate([
      ('01 / Registration','Color plates settle into the headline. A short introduction inspired by the print process.'),
      ('02 / Color wheel','The color wheel turns once. A signature brand detail without implying a turnaround promise.'),
      ('03 / Preview guides','Trim and safe-area guides appear around the sample. The motion explains placement; it is not a file-analysis result.')]):
        x=40+i*363;para(c,head,x,213,330,17,color=BLUE);para(c,body,x,178,330,13)
    para(c,'Reduced motion presents static compositions. Next: agree the audience and first release in a 45-minute discovery session; scope commerce and automation after validation.',40,79,1072,12)
    c.showPage();c.save()

def direction():
    data=json.loads((HERE/'direction-content.json').read_text(encoding='utf-8-sig'));W,H=612,792
    c=canvas.Canvas(str(HERE/'i2Print-Website-and-Automation-Direction-DRAFT-v3.pdf'),pagesize=(W,H))
    c.setTitle('i2Print Website and Automation Direction — Draft v3');c.setAuthor('Daniel Raxa · RaxaRisk, LLC')
    for n,page in enumerate(data['pages'],1):
        base(c,n,W,H,page['title'],page['eyebrow'].upper())
        top=H-202
        top=para(c,page['intro'],40,top,532,13,18,color=MUTED)-23
        for sec in page['sections']:
            top=para(c,sec['heading'],40,top,532,15,19,color=BLUE)-6
            if 'body' in sec:top=para(c,sec['body'],40,top,532,12.1,16.6)-17
            for b in sec.get('bullets',[]):top=para(c,'• '+b,48,top,524,12.1,16.6)-6
            if 'bullets' in sec:top-=11
        if page.get('sources'):
            top-=4
            for source in page['sources']:
                y=para(c,source['label']+' ↗',40,top,532,9,12,color=BLUE)
                c.linkURL(source['url'],(40,y,572,top),relative=0);top=y-3
        AUDIT.append({'direction_page':n,'bottom_y':round(top,1)})
        c.showPage()
    c.save()

if __name__=='__main__':
    concept();direction();(HERE/'qa/pdf-layout-audit.json').write_text(json.dumps(AUDIT,indent=2))
    print('Built 14-page landscape concept and 8-page portrait direction PDFs.')
