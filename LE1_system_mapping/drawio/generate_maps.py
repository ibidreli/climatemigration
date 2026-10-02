"""
Erzeugt causal_loop_map und stakeholder_map nach drawio/ und png/.

Achtung: Überschreibt die bestehenden Dateien. Manuelle Änderungen
in draw.io gehen dabei verloren. Benötigt Pillow und die Windows-Schrift Arial.
"""
from pathlib import Path
import xml.etree.ElementTree as E
from PIL import Image, ImageDraw, ImageFont
import math

P=Path(__file__).resolve().parent
C={'green':('#d5e8d4','#82b366'),'blue':('#dae8fc','#6c8ebf'),'red':('#f8cecc','#b85450'),'yellow':('#fff2cc','#d6b656'),'purple':('#e1d5e7','#9673a6'),'orange':('#ffe6cc','#d79b00'),'grey':('#f5f5f5','#888888'),'white':('#ffffff','#d5d9df')}
class Map:
 def __init__(self,name,w,h):
  self.name=name; self.w=w; self.h=h; self.nodes={}; self.edges=[]; self.i=0
  self.doc=E.Element('mxfile',host='app.diagrams.net',type='device')
  d=E.SubElement(self.doc,'diagram',name=name,id=name.replace(' ','-'))
  m=E.SubElement(d,'mxGraphModel',grid='1',gridSize='10',guides='1',connect='1',arrows='1',page='1',pageScale='1',pageWidth=str(w),pageHeight=str(h),background='#ffffff')
  self.r=E.SubElement(m,'root'); E.SubElement(self.r,'mxCell',id='0'); E.SubElement(self.r,'mxCell',id='1',parent='0')
 def box(self,id,text,x,y,w,h,col='grey',size=22,bold=False,align='center',plain=False):
  fill,stroke=C[col]; style=f'rounded=1;arcSize=10;whiteSpace=wrap;html=0;fontFamily=Arial;fontSize={size};fontStyle={1 if bold else 0};align={align};verticalAlign=middle;spacing=18;fillColor={fill};strokeColor={stroke};strokeWidth=2;'
  if plain: style+='fillColor=none;strokeColor=none;'
  c=E.SubElement(self.r,'mxCell',id=id,value=text,style=style,vertex='1',parent='1'); E.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
  self.nodes[id]=(text,x,y,w,h,col,size,bold,align,plain)
 def text(self,id,text,x,y,w,h,size=24,bold=False): self.box(id,text,x,y,w,h,'white',size,bold,plain=True)
 def edge(self,a,b,label='',col='grey',dashed=False,points=None,ports=(1,.5,0,.5),arrow=True):
  self.i+=1; color=C[col][1]; ex,ey,ix,iy=ports
  style=f'edgeStyle=none;rounded=0;html=0;endArrow={"block" if arrow else "none"};endFill=1;strokeWidth=3;strokeColor={color};fontColor={color};fontSize=23;fontStyle=1;labelBackgroundColor=#ffffff;exitX={ex};exitY={ey};entryX={ix};entryY={iy};exitPerimeter=0;entryPerimeter=0;dashed={int(dashed)};'
  c=E.SubElement(self.r,'mxCell',id=f'e{self.i}',source=a,target=b,value=label,edge='1',parent='1',style=style)
  g=E.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
  if points:
   ar=E.SubElement(g,'Array',attrib={'as':'points'})
   for x,y in points: E.SubElement(ar,'mxPoint',x=str(x),y=str(y))
  self.edges.append((a,b,label,color,dashed,points or [],ports,arrow))
 def save(self,stem):
  E.indent(self.doc); E.ElementTree(self.doc).write(P/'drawio'/(stem+'.drawio'),encoding='utf-8',xml_declaration=True)
  im=Image.new('RGB',(self.w,self.h),'white'); d=ImageDraw.Draw(im)
  for text,x,y,w,h,col,size,bold,align,plain in self.nodes.values():
   if not plain: d.rounded_rectangle((x,y,x+w,y+h),radius=16,fill=C[col][0],outline=C[col][1],width=2)
   f=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf' if bold else 'C:/Windows/Fonts/arial.ttf',size)
   lines=[]
   for paragraph in text.split('\n'):
    line=''
    for word in paragraph.split():
     test=(line+' '+word).strip()
     if d.textlength(test,font=f)>w-36 and line: lines.append(line); line=word
     else: line=test
    lines.append(line)
   lh=size+7
   assert len(lines)*lh<=h,(stem,text[:50],len(lines)*lh,h)
   yy=y+(h-len(lines)*lh)/2
   for line in lines:
    xx=x+18 if align=='left' else x+(w-d.textlength(line,font=f))/2
    d.text((xx,yy),line,fill='#263238',font=f); yy+=lh
  for a,b,label,color,dashed,points,ports,arrow in self.edges:
   _,x,y,w,h,*_=self.nodes[a]; _,xx,yy,ww,hh,*_=self.nodes[b]; ex,ey,ix,iy=ports
   ps=[(x+ex*w,y+ey*h)]+points+[(xx+ix*ww,yy+iy*hh)]
   for p,q in zip(ps,ps[1:]):
    if dashed:
     length=math.dist(p,q)
     for t in range(0,int(length),20):
      u=t/length; v=min(t+11,length)/length
      d.line((p[0]+(q[0]-p[0])*u,p[1]+(q[1]-p[1])*u,p[0]+(q[0]-p[0])*v,p[1]+(q[1]-p[1])*v),fill=color,width=3)
    else:d.line((p,q),fill=color,width=3)
   if arrow:
    p,q=ps[-2:]; angle=math.atan2(q[1]-p[1],q[0]-p[0]); d.polygon([q,(q[0]-16*math.cos(angle-.4),q[1]-16*math.sin(angle-.4)),(q[0]-16*math.cos(angle+.4),q[1]-16*math.sin(angle+.4))],fill=color)
   if label:
    p,q=ps[len(ps)//2-1:len(ps)//2+1]; lx=(p[0]+q[0])/2; ly=(p[1]+q[1])/2
    f=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',23); bw=d.textlength(label,font=f)
    d.rectangle((lx-bw/2-5,ly-17,lx+bw/2+5,ly+17),fill='white'); d.text((lx-bw/2,ly-14),label,fill=color,font=f)
  im.save(P/'png'/(stem+'.png'))
  ids=[c.get('id') for c in self.r]; assert len(ids)==len(set(ids))
  for a,b,*_ in self.edges: assert a in ids and b in ids
  print(stem,len(self.nodes),'elements',len(self.edges),'relationships; XML, references and text fit verified')

s=Map('Stakeholder Map – ausführlich',3100,2900)
s.text('title','STAKEHOLDER MAP | Klimabedingte Abwanderung in Kaffrine',50,25,3000,70,38,True)
s.text('sub','Sahel-Zone · Senegal · Region Kaffrine | Alle zehn Akteursgruppen, ihre Rollen und Beziehungen',50,100,3000,55,25)
s.text('lh','DIREKT BETROFFENE AKTEURE',50,190,760,50,28,True)
s.text('rh','UNTERSTÜTZUNG, STEUERUNG UND WISSEN',2190,190,860,50,28,True)
left=[('house','Lokale Haushalte','yellow','Betroffenheit: Dürre, Wasserknappheit, Ernteausfälle und Abwanderung.\nInteressen: verlässliche Versorgung, tragfähiges Einkommen und gesicherte Lebensgrundlagen.\nRolle: treffen bzw. tragen Entscheidungen über Erwerb und Abwanderung.'),('farm','Landwirtschaftliche Betriebe und Bauern','blue','Betroffenheit: abhängig von Wasserverfügbarkeit und landwirtschaftlichen Erträgen.\nInteressen: stabile Produktion, verfügbare Arbeitskräfte und ausreichendes Einkommen.\nAnsatzpunkte: Anbau, Bewässerung und landwirtschaftliche Anpassung.'),('mig','Abwandernde Personen','yellow','Betroffenheit: verlassen die Region im Kontext unsicherer Lebensgrundlagen.\nSystemwirkung: verändern lokale Bevölkerung und verfügbare Arbeitskräfte.\nBeziehungen: bleiben potenziell über Familie, Netzwerke und Rücküberweisungen verbunden.'),('fam','Zurückbleibende Familien','purple','Betroffenheit: mögliche Lücken bei Arbeit, Versorgung und familiären Aufgaben.\nMögliche Entlastung: Rücküberweisungen abgewanderter Angehöriger.\nInteressen: gesichertes Haushaltseinkommen und tragfähige familiäre Unterstützung.')]
for i,(id,title,col,body) in enumerate(left):
 y=270+i*330; s.box(id,title+'\n\n'+body,50,y,760,290,col,23,align='left')
right=[('auth','Lokale und regionale Behörden','Infrastruktur, Wasserversorgung und Unterstützungsprogramme.\nAnsatzpunkt: lokale Umsetzung und Koordination.','orange'),('aid','Hilfs- und Entwicklungsorganisationen','Ernährungssicherheit, Landwirtschaft und Klimaanpassung.\nAnsatzpunkt: Projekte, Unterstützung und Zusammenarbeit.','orange'),('gov','Nationale Regierung','Möglicher Beitrag: Rahmenbedingungen, Mittel und staatliche Unterstützung.\nSchnittstelle: lokale und regionale Behörden.','orange'),('advice','Landwirtschaftliche Beratungsstellen','Möglicher Beitrag: Wissen zu Anbau, Wasserbewirtschaftung und Anpassung.\nSchnittstelle: Betriebe und Bauern.','blue'),('community','Lokale Gemeinschaften','Möglicher Beitrag: soziale Netzwerke, Austausch und gegenseitige Hilfe.\nSchnittstelle: Haushalte und Familien.','purple'),('research','Forschung und internationale Organisationen','Möglicher Beitrag: Daten, Analysen und Wissen zu Klima, Landwirtschaft und Migration.\nSchnittstelle: Planung und Unterstützungsprogramme.','grey')]
for i,(id,title,body,col) in enumerate(right):
 y=270+i*215; s.box(id,title+'\n\n'+body,2230,y,820,190,col,22,align='left')
s.box('system','SYSTEMKERN\nKlimabedingte Abwanderung\nin Kaffrine',1050,400,870,180,'green',32,True)
s.text('path','Dürre / Wasserknappheit → Ernteausfälle\n→ unsichere Einkommen → Abwanderung',1060,605,850,110,26)
for i,(title,body,col) in enumerate([('Klima und Umwelt','Niederschlag · Dürre · Temperatur\nWasserverfügbarkeit · Bodenqualität','green'),('Landwirtschaft und Ernährung','Ertrag · Anbaufläche · Wasserbedarf\nProduktion · Nahrungsmittelverfügbarkeit','blue'),('Wirtschaft','Landwirtschaftliches Einkommen\nHaushaltseinkommen · Preise · Alternativen','red'),('Bevölkerung und Abwanderung','Bevölkerung · Entwicklung\nAbwanderung · verfügbare Arbeitskräfte','yellow'),('Soziale Faktoren','Familiäre Abhängigkeiten\nRücküberweisungen · soziale Netzwerke','purple'),('Institutionelle Faktoren','Wasserversorgung · Bewässerung\nHilfsprogramme · Unterstützung · Infrastruktur','orange')]):
 s.box('topic'+str(i),title+'\n'+body,1030,750+i*130,930,120,col,22)
for i,(id,*_) in enumerate(left):
 s.edge(id,'system','', 'yellow',ports=(1,.5,0,.15+i*.23),arrow=False)
for i,(id,*_) in enumerate(right):
 s.edge(id,'system','','orange',ports=(0,.5,1,.08+i*.17),arrow=False)
s.text('rel-title','BEZIEHUNGEN IM DETAIL',50,1585,3000,60,30,True)
s.text('rel-sub','Eigenständige Beziehungsausschnitte: Pfeile benennen einen Beitrag oder eine Wirkung. Gestrichelt = ergänzende Arbeitshypothese.',50,1650,3000,45,22)
rels=[('Abwandernde Personen','Zurückbleibende Familien','Rücküberweisungen','Mögliche finanzielle Unterstützung; keine Garantie für regelmässige Zahlungen.','purple',False),('Abwandernde Personen','Landwirtschaftliche Betriebe','Weniger Arbeitskräfte','Abwanderung kann die lokal verfügbare Arbeit und damit die Produktion verringern.','yellow',False),('Betriebe und Bauern','Lokale Haushalte','Ertrag und Einkommen','Die landwirtschaftliche Situation prägt die Lebensgrundlagen betroffener Haushalte.','blue',True),('Lokale / regionale Behörden','Lokale Haushalte','Versorgung / Infrastruktur','Wasserversorgung und Unterstützungsprogramme als mögliche Einflusswege.','orange',False),('Hilfsorganisationen','Betriebe und Bauern','Anpassung / Unterstützung','Unterstützung bei Landwirtschaft und Anpassung an klimatische Veränderungen.','orange',False),('Hilfsorganisationen','Lokale Haushalte','Ernährungssicherheit','Unterstützung zur Stabilisierung der Versorgung und Lebensgrundlagen.','orange',False),('Nationale Regierung','Lokale / regionale Behörden','Rahmen / Ressourcen','Mögliche Verbindung zwischen nationaler Unterstützung und lokaler Umsetzung.','orange',True),('Beratungsstellen','Betriebe und Bauern','Beratung / Wissen','Mögliche Verbesserung von Anbau und Wasserbewirtschaftung.','blue',True),('Lokale Gemeinschaften','Haushalte / Familien','Netzwerke / Hilfe','Möglicher Austausch von Informationen und gegenseitige Unterstützung.','purple',True),('Forschung / int. Organisationen','Behörden / Hilfsorganisationen','Daten / Analysen','Möglicher Beitrag zur Planung, Priorisierung und Bewertung von Massnahmen.','grey',True),('Zurückbleibende Familien','Abwandernde Personen','Familiäre Bindungen','Abhängigkeiten und Verpflichtungen können Entscheidungen prägen; Richtung offen.','purple',True),('Lokale Haushalte','Behörden / Hilfsorganisationen','Bedarf / Erfahrungen','Möglicher Rückfluss lokaler Bedürfnisse und Erfahrungen an unterstützende Akteure.','orange',True)]
for i,(a,b,label,note,col,hyp) in enumerate(rels):
 x=50+(i%3)*1010; y=1730+(i//3)*240; k='rel'+str(i)
 s.box(k,'',x,y,980,220,'white')
 s.box(k+'a',a,x+20,y+20,365,70,col,21)
 s.box(k+'b',b,x+595,y+20,365,70,col,21)
 s.edge(k+'a',k+'b','',col,hyp)
 s.text(k+'label',label,x+380,y+90,220,60,19,True)
 s.text(k+'note',note,x+25,y+145,930,60,21)
s.box('scope','SYSTEMGRENZEN UND LESART\nRegion Kaffrine; konkrete Zielorte, Zuwanderung und Rückkehrmigration ausserhalb des direkten Modellfokus. Konflikte, detaillierte politische Entwicklungen und wirtschaftliche Krisen bleiben Kontext.\nAkteursgruppen können sich überschneiden. Rollenbeschreibungen und gestrichelte Beziehungen sind konzeptionelle Ergänzungen, keine empirisch geprüfte Einflussbewertung.',50,2720,3000,145,'grey',22,align='left')
s.save('stakeholder_map')

c=Map('Causal Loop Map – ausführlich',3100,2900)
c.text('title','CAUSAL LOOP MAP | Klimabedingte Abwanderung in Kaffrine',50,25,3000,70,38,True)
c.text('sub','Kernmodell und vollständige Themenübersicht | Durchgezogen: vorgegebene Wirkungen · gestrichelt: mögliche B-Schleife bzw. ergänzende Annahmen',50,100,3000,65,23)
c.box('core','',40,185,3020,860,'white')
c.text('coretitle','01  KERNMODELL: KLIMA → LANDWIRTSCHAFT → EINKOMMEN → ABWANDERUNG',65,200,1640,55,27,True)
nodes=[('rain','Niederschlag',90,320,'green'),('drought','Dürre',90,570,'green'),('water','Wasserverfügbarkeit',510,445,'green'),('yield','Landwirtschaftlicher\nErtrag',930,445,'blue'),('income','Landwirtschaftliches\nEinkommen',1350,445,'red'),('migration','Abwanderung',1800,445,'yellow'),('pop','Bevölkerung',2420,445,'yellow'),('labor','Verfügbare\nArbeitskräfte',1800,810,'yellow'),('production','Landwirtschaftliche\nProduktion',1350,810,'blue'),('remit','Rücküberweisungen',2420,235,'purple'),('houseincome','Haushaltseinkommen',1800,235,'red')]
for id,t,x,y,col in nodes:c.box(id,t,x,y,300,105,col,25,id=='migration')
for a,b,l,co,d,p in [('rain','water','+','green',False,(1,.5,0,.25)),('drought','water','−','green',False,(1,.5,0,.75)),('water','yield','+','grey',False,(1,.5,0,.5)),('yield','income','+','grey',False,(1,.5,0,.5)),('income','migration','−','red',False,(1,.5,0,.5)),('migration','pop','−','grey',False,(1,.5,0,.5)),('migration','labor','−','red',False,(.5,1,.5,0)),('labor','production','+','red',False,(0,.5,1,.5)),('production','income','+','red',False,(.5,0,.5,1)),('migration','remit','+','purple',True,(1,0,.5,1)),('remit','houseincome','+','purple',True,(0,.5,1,.5)),('houseincome','migration','−','purple',True,(.5,1,.5,0))]:c.edge(a,b,l,co,d,ports=p)
c.text('r','R · VERSTÄRKEND\nArbeitskräfte–Einkommen',1515,640,400,95,25,True)
c.text('b','B · AUSGLEICHEND\nRücküberweisungen\n(möglich)',2130,305,245,78,18,True)
c.box('key','+  Gleiche Wirkungsrichtung\n−  Entgegengesetzte Wirkungsrichtung\n\nVorzeichen gelten bei sonst gleichen Bedingungen.\nSie bedeuten nicht «gut» oder «schlecht».',90,770,1030,210,'grey',24,align='left')
c.text('corefoot','R: Zwei negative Verbindungen → verstärkend.    B: Eine negative Verbindung → ausgleichend.\nDie mögliche B-Schleife wird nur bei geeigneter Datenlage und angemessener Modellkomplexität übernommen.',1190,950,1770,70,23)

# Detail modules deliberately repeat shared variables so the large map remains readable.
c.text('modules','02  DETAILMODULE: ALLE FAKTOREN DER CLUSTER MAP',50,1080,3000,55,29,True)
c.text('repeat','Gleich benannte Knoten stehen für dieselbe Grösse wie im Kernmodell. Detailmodule zeigen ergänzende Wirkungshypothesen; sie sind keine zusätzlichen unabhängigen Systeme.',50,1140,3000,60,22)
def panel(k,title,x,y,col,note):
 c.box(k,'',x,y,980,590,'white'); c.box(k+'title',title,x+15,y+15,950,65,col,25,True)
 c.text(k+'note',note,x+25,y+465,930,105,21)
def n(k,t,x,y,col): c.box(k,t,x,y,270,85,col,21)
def e(a,b,l,ports=(1,.5,0,.5),points=None):c.edge(a,b,l,'grey',True,points,ports)

x=50;y=1230;panel('climate','KLIMA UND UMWELT',x,y,'green','Annahmen: höhere Temperatur kann Dürre und Wasserstress begünstigen; Dürre kann die Bodenqualität beeinträchtigen. Die Stärke und zeitliche Verzögerung sind zu prüfen.')
n('temp','Temperatur',x+30,y+125,'green');n('dry2','Dürre',x+365,y+125,'green');n('soil','Bodenqualität',x+685,y+125,'green');n('water2','Wasserverfügbarkeit',x+365,y+335,'green');n('yield2','Landwirtschaftlicher\nErtrag',x+685,y+335,'blue');n('rain2','Niederschlag',x+30,y+335,'green')
e('temp','dry2','+');e('dry2','soil','−');e('soil','yield2','+',(.5,1,.5,0));e('dry2','water2','−',(.5,1,.5,0));e('rain2','water2','+');e('water2','yield2','+')

x=1060;panel('agri','LANDWIRTSCHAFT UND ERNÄHRUNG',x,y,'blue','Ertrag bezeichnet hier die Produktivität pro Fläche, Produktion die gesamte Menge. Mehr Fläche erhöht den Wasserbedarf; mehr Produktion kann die Nahrungsmittelverfügbarkeit erhöhen.')
for k,t,dx,dy,col in [('area','Verfügbare Anbaufläche',30,125,'blue'),('demand','Wasserbedarf der\nLandwirtschaft',365,125,'blue'),('water3','Wasserverfügbarkeit',685,125,'green'),('yield3','Landwirtschaftlicher\nErtrag',30,335,'blue'),('prod3','Landwirtschaftliche\nProduktion',365,335,'blue'),('food','Nahrungsmittel-\nverfügbarkeit',685,335,'blue')]:n(k,t,x+dx,y+dy,col)
e('area','demand','+');e('demand','water3','−');e('area','prod3','+',(.5,1,.5,0));e('yield3','prod3','+');e('prod3','food','+')

x=2070;panel('econ','WIRTSCHAFT UND LEBENSGRUNDLAGEN',x,y,'red','Mehr landwirtschaftliches Einkommen und lokale Erwerbsalternativen können Haushalte stärken. Preise beeinflussen die Kaufkraft, nicht direkt das nominale Einkommen. Preiswirkungen hängen auch von externen Märkten ab.')
for k,t,dx,dy,col in [('inc3','Landwirtschaftliches\nEinkommen',30,125,'red'),('hh3','Haushaltseinkommen',365,125,'red'),('alternatives','Wirtschaftliche\nAlternativen vor Ort',685,125,'red'),('prices','Lebensmittelpreise',30,335,'red'),('purchase','Kaufkraft für\nLebensmittel',365,335,'red'),('mig3','Abwanderung',685,335,'yellow')]:n(k,t,x+dx,y+dy,col)
e('inc3','hh3','+');e('alternatives','hh3','+',(0,.5,1,.5));e('hh3','purchase','+',(.5,1,.5,0));e('prices','purchase','−');e('purchase','mig3','−');e('alternatives','mig3','−',(.5,1,.5,0))

x=50;y=1870;panel('demo','BEVÖLKERUNG UND ABWANDERUNG',x,y,'yellow','Bevölkerungsentwicklung beschreibt die zeitliche Veränderung des Bestands, keine zusätzliche unabhängige Ursache. Weniger Bevölkerung kann den lokalen Versorgungsdruck senken; diese Erweiterung ist zu prüfen.')
for k,t,dx,dy,col in [('mig4','Abwanderung',30,125,'yellow'),('pop4','Bevölkerung',365,125,'yellow'),('labor4','Verfügbare\nArbeitskräfte',685,125,'yellow'),('change','Bevölkerungsentwicklung\n(Veränderung des Bestands)',30,335,'yellow'),('pressure','Lokaler Versorgungsdruck',365,335,'yellow'),('food4','Nahrungsmittel-\nverfügbarkeit pro Person',685,335,'blue')]:n(k,t,x+dx,y+dy,col)
e('mig4','pop4','−');e('pop4','labor4','+');e('pop4','pressure','+',(.5,1,.5,0));e('pressure','food4','−');c.edge('pop4','change','Verlauf','yellow',True,ports=(0,1,1,0),arrow=False)

x=1060;panel('social','SOZIALE FAKTOREN',x,y,'purple','Netzwerke können vor Ort stützen oder Migration erleichtern; familiäre Abhängigkeiten können Bleiben oder Gehen begünstigen. Deshalb erhalten diese Beziehungen kein eindeutiges +/−. Rücküberweisungen bleiben eine mögliche Wirkung.')
for k,t,dx,dy,col in [('network','Soziale Netzwerke',30,125,'purple'),('mig5','Abwanderung',365,125,'yellow'),('family','Familiäre\nAbhängigkeiten',685,125,'purple'),('remit5','Rücküberweisungen',365,335,'purple'),('hh5','Haushaltseinkommen',685,335,'red')]:n(k,t,x+dx,y+dy,col)
e('network','mig5','±');e('family','mig5','±',(0,.5,1,.5));e('mig5','remit5','+',(.5,1,.5,0));e('remit5','hh5','+')

x=2070;panel('inst','INSTITUTIONELLE FAKTOREN',x,y,'orange','Wirkungshypothesen: Unterstützung kann Infrastruktur und Hilfsprogramme ermöglichen. Versorgung und Bewässerung können nutzbares Wasser erhöhen; tatsächliche Effekte hängen von Kapazität und Umsetzung ab.')
for k,t,dx,dy,col in [('support','Staatliche Unterstützung',30,125,'orange'),('infra','Infrastruktur',365,125,'orange'),('supply','Wasserversorgung',685,125,'orange'),('program','Landwirtschaftliche\nHilfsprogramme',30,335,'orange'),('irrigation','Bewässerung',365,335,'orange'),('water6','Wasserverfügbarkeit',685,335,'green')]:n(k,t,x+dx,y+dy,col)
e('support','infra','+');e('infra','supply','+');e('support','program','+',(.5,1,.5,0));e('program','irrigation','+');e('irrigation','water6','+');e('supply','water6','+',(.5,1,.5,0))
c.box('scope','03  SYSTEMGRENZEN / KONTEXT\nRäumlich: Kaffrine in Senegal, im Kontext der Sahel-Zone. Die Ziele der Abwanderung liegen ausserhalb des Systems.\nAusserhalb des direkten Modellfokus: konkrete Zielorte, Zuwanderung, Rückkehrmigration, Konflikte als eigenständige Dynamik, detaillierte politische Entwicklungen und wirtschaftliche Krisen. Diese Einflüsse werden hier nicht kausal ausmodelliert.\nZeitlich: Betrachtungs- und Simulationszeitraum werden in LE2 anhand verfügbarer Klima-, Landwirtschafts- und Migrationsdaten festgelegt.',50,2510,1480,335,'grey',23,align='left')
c.box('assumptions','04  MODELLLOGIK / OFFENE PRÜFPUNKTE\nDie 12 Verbindungen des Kernmodells entsprechen der vorgegebenen Wirkungskette sowie R- und B-Schleife. Erweiterungen in den Detailmodulen sind konzeptionelle Annahmen, keine geprüften Befunde für Kaffrine.\nAbwanderung bezeichnet im Kernmodell die Intensität bzw. Rate. Rücküberweisungen hängen zudem vom Bestand abgewanderter Personen, deren Einkommen und zeitlichen Verzögerungen ab.\n± = kontextabhängige Richtung; keine feste Polarität. Kaufkraft und Versorgungsdruck sind ergänzte Vermittlungsgrössen. Ertrag, Produktion und Einkommen sind im Simulationsmodell getrennt zu definieren, um Doppelzählungen zu vermeiden.',1570,2510,1480,335,'grey',23,align='left')
c.save('causal_loop_map')
