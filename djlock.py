modder = 'Cosmo TechZone'
author = 'Djoney Ardy'

from graphics import Image, screenshot
from appswitch import application_list, switch_to_bg, switch_to_fg
from appuifw import app, Canvas, note
from e32 import ao_sleep
from envy import set_app_system
from pykeylock import LockStatus, Unlock
import ini
set_app_system(1)

run=1
coba=0
sc=0

from sys import argv
drive = argv[0][:3]
pat=drive+'dj\\lock\\'
del argv
readcon = ini.read(pat + 'config.ini')
warna = readcon['warna']
ukuran_garis_pola = readcon['ukuran_garis_pola']
margin_x = readcon['margin_x']
margin_y = readcon['margin_y']

point=Image.open(pat+'point.png')
point1=Image.open(pat+'point1.png')
apname=application_list(1)[0]

def balik():
 global coba
 if coba==0:
  switch_to_bg(application_list(1)[0])

def quit():
 global run,coba
 if coba==0:
  run=0
  app.set_exit()
 elif coba==2:
  coba=0
 else:pass

def tomask(img):
    msk = Image.new(img.size, 'L')
    msk.blit(img)
    return msk

def hide():
 global ss
 import laa
 laa.execute(0x102750f0)
 laa.execute(0x101fd64c)
 ao_sleep(0)
 ss=screenshot()
 ao_sleep(0)
 del laa
 
def event(v):
 global sc
 sc,tp=v['scancode'],v['type']

app.exit_key_handler=balik
app.screen='full'
app.body=c=Canvas(None,event)
x,y=c.size
im=Image.new((x,y))
axy=70
w=(x-(2.70*axy))/2
h=(y-(4.6*axy))/3
key,n={},1
for j in range(49,58):
 key[j]=n
 n+=1
print key
tmp=[]

openn=eval(open(pat+'lock.dat').read().decode('hex'))

def newcode():
 global coba
 coba=2

def rest():
 global vpos,kode,tmp,sc
 vpos=[]
 kode=[]
 tmp=[]
 sc=0

def saved():
 global coba,openn,vpos,kode,tmp,sc
 if kode==[]:note(u'Pattern still empty','error')
 else:
  openn=kode
  note(u'Pattern saved','conf')
  coba=0
  open(pat+'lock.dat','w').write((str(openn).encode('hex')))
 app.exit_key_handler=balik
 vpos=[]
 kode=[]
 tmp=[]
 sc=0

kode=[]
app.menu=[]
note(u'Initializing...')
hide()
aps1=application_list(1)[0]

def canc():
 global coba
 coba=0
 rest()
 app.exit_key_handler=balik

while run:
 aps=application_list(1)[0]

 if coba==0:
  im.clear(0xd8d8d8)
  im.text((0,c.size[1]),u'Menu',0x333333,(u'normal',(18)))
  app.menu=[(u'Change pattern',newcode),(u'Exit',quit)]
  if aps in [u'akncapserver']:
   if LockStatus()==1:
    switch_to_fg(apname)
    try:Unlock()
    except:pass
    coba=1
  else:pass

 if coba==1:
  app.menu=[(u'Refresh pattern',rest)]
  im.blit(ss)
  y1=0
  for j in range(9):
   if j%3==0:
    y1+=1
    x1=0
   else:x1+=1
   X=x1*axy
   Y=y1*axy
   pos=(w+X+margin_x,h+Y+margin_y)
   im.blit(point,mask=tomask(point),target=(pos[0],pos[1]))
  del y1
  if kode==openn:
   note(u'Unlocked!','conf')
   vpos=[]
   kode=[]
   tmp=[]
   sc=0
   coba=0
   switch_to_bg(apname)
  else:
   if aps not in [apname]:
    switch_to_fg(apname)
  if len(kode)>=len(openn):
   note(u'Wrong pattern\nPlease Try Again','error')
   vpos=[]
   kode=[]
   tmp=[]
   sc=0
  y1=0
  for j in range(9):
   if j%3==0:
    y1+=1
    x1=0
   else:x1+=1
   X=x1*axy
   Y=y1*axy
   pos=(w+X+margin_x,h+Y+margin_y)
   if key.has_key(sc):
    if key[sc]==j+1:
     if (pos,j) not in tmp:
      tmp+=[(pos,j)]
      kode+=[j]
      vpos=[]
      for k,v in tmp:
       rx,ry=k
       px,py=rx,ry
       vpos.append((px+point1.size[0]/2,py+point1.size[1]/2))
     try:
      if len(kode)<len(openn)+1:
       im.line(vpos,warna,width=ukuran_garis_pola)
       for i in vpos:
        im.blit(point1,mask=tomask(point1),target=(i[0]-point1.size[0]/2,i[1]-point1.size[1]/2))
     except:pass
     
#new pattern
 if coba==2:
  app.menu=[(u'Save',saved),(u'Refresh',rest)]
  app.exit_key_handler=canc
  im.blit(ss)
  im.text((0,c.size[1]),u'Draw new pattern',0xffffff,(u'normal',(18)))
  y1=0
  for j in range(9):
   if j%3==0:
    y1+=1
    x1=0
   else:x1+=1
   X=x1*axy
   Y=y1*axy
   pos=(w+X+margin_x,h+Y+margin_y)
   im.blit(point,mask=tomask(point),target=(pos[0],pos[1]))
  del y1
  y1=0
  for j in range(9):
   if j%3==0:
    y1+=1
    x1=0
   else:x1+=1
   X=x1*axy
   Y=y1*axy
   pos=(w+X+margin_x,h+Y+margin_y)
   if key.has_key(sc):
    if key[sc]==j+1:
     if (pos,j) not in tmp:
      tmp+=[(pos,j)]
      kode+=[j]
      vpos=[]
      for k,v in tmp:
       rx,ry=k
       px,py=rx,ry
       vpos.append((px+point1.size[0]/2,py+point1.size[1]/2))
     try:
      im.line(vpos,warna,width=ukuran_garis_pola)
      for i in vpos:
       im.blit(point1,mask=tomask(point1),target=(i[0]-point1.size[0]/2,i[1]-point1.size[1]/2))
     except:pass
     
 if aps in [apname]:
  c.blit(im)
  ao_sleep(0)