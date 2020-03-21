#NOTES
#SOURCE CODE INI DIPERKENANKAN UNTUK DIKEMBANGKAN ATAUPUN DIMODIFIKASI SESUAI KEBUTUHAN USER
#THIS SOURCE CODE CAN BE DEVELOPED OR MODIFIED ACCORDING TO USER REQUIREMENTS
#ORIGINAL SOURCE : COSMOTZ.BLOGSPOT.COM

#PUT THIS FILE IN !:\PRIVATE\88888804

from e32 import ao_sleep as AS
from appuifw2 import app as AP
from appuifw import Listbox as LB, note as NT
from envy import set_app_system as sa
from os import path
from keycapture import KeyCapturer as KCR
from graphics import screenshot as SCR, Image as IG
import ini
from sys import argv
from sysinfo import display_pixels as dpx
from time import strftime as SF
import mbm as m
mf = argv[0][ : 3]
mg = argv[0][ : -10]
del argv
sa(1)
class utama :
 __module__ = __name__
 def __init__(q):
  q.mfo = (mf + 'CosmoTech\\FScreen\\')
  q.st = ini.read((q.mfo + 'position'))
  q.name = u'F-Screen'
  q.w1 = m.image((q.mfo + 'watermark'), 0)
  q.w2 = m.image((q.mfo + 'watermark'), 1)
  q.hc = q.sc = 0
  sz = q.w1.size
  q.im, q.ss = (IG.new(sz), IG.new(dpx()))
  q.cap = KCR(q.key)
  q.lo = (mg + 'fdrive.dat')
  q.cap.keys = (q.load(q.lo)[1], )
  q.cap.start()
  if q.load(q.lo)[0] == u'':
   q.b='None'
  else: q.b=q.load(q.lo)[0]
  if q.load(q.lo)[2] == u'':
   q.w='None'
  else: q.w=q.load(q.lo)[2]
  if q.load(q.lo)[1] == 8 : 
   ke = u'C (Delete)'
  else : 
   ke = u'Green Key/Call'
  q.list = [(u'Status', u'Active'), (u'Shot Button', ke), (u'Watermark & Background', unicode(q.w[:-4]+' | '+path.split(q.b)[1])), (u'About', q.un('\xc2\xa9 2018, Cosmo TechZone'))]
  q.lb = LB(q.list, q.sel)
  AP.body = q.lb
  AP.title = u'F-Screen'
  AP.exit_key_handler = q.mi
  AP.menu_key_text = u'Options'
  AP.exit_key_text = u'Minimize'
  AP.menu = [(u'Change Watermark', q.cwm), (u'Change Background', q.cbg), (u'Clear Background', q.clr), (u'Exit', q.ex)]
  try :
   sw = q.load(q.lo)[0]
   q.bg = IG.open(sw).resize(sz)
  except :
   pass

 def cu(q):
  from appuifw import popup_menu as P, Content_handler as C
  li = [u'Watermark', u'Background']
  ok = P(li, u'Selected:')
  if ok == 0 :
   C().open(q.mfo+'watermark')
  elif ok == 1 :
   C().open(q.b)

 def ex(q):
  if q.hc == q.sc : 
   AP.set_exit()
  else : 
   NT(u'Busy, retry again later')


 def save(q, dir, cnt):
  f = open(dir, 'wt')
  f.write(repr(cnt))
  f.close()


 def load(q, di):
  if path.exists(di) : 
   f = open(di, 'rt')
   fr = f.read()
   data = eval(fr)
   f.close()
  return data


 def get(q):
  s = SCR()
  try :
   restu = q.st['adscreen']
   ads=1
  except :
   restu = dpx()
   ads=0
  q.hc += 1
  NT(u'Screenshot Saved !', 'conf', 1)
  ti = unicode(SF('%Y%m%d-%H%M%S'))
  try :
   q.im.blit(q.bg)
  except :
   pass
  if ads == 1 : 
   q.ss.blit(s)
   ssx = q.ss.resize(restu)
  else : 
   ssx = s
  q.im.blit(ssx, target = (q.st['x'], q.st['y']))
  q.im.blit(q.w1, mask = q.w2)
  q.im.save((mf + 'CosmoTech\\Captured\\FScreen-' + ti + '.png'), compression = 'best')
  q.sc += 1


 def key(q, press):
  if press == q.load(q.lo)[1] : 
   q.get()


 def un(q, x):
  f = x.decode('utf-8')
  return f


 def config(q):
  from appuifw import popup_menu as pm
  sbt = [u'Green Key/Call', u'C (Delete)']
  pil = pm(sbt, u'Shot button :')
  if pil == 0 : 
   q.save(q.lo, [q.load(q.lo)[0], 63586, q.load(q.lo)[2]])
   q.list[1] = (u'Shot button', sbt[0])
   q.lb.set_list(q.list, 1)
   q.cap.keys = (q.load(q.lo)[1], )
  elif pil == 1 : 
   q.save(q.lo, [q.load(q.lo)[0], 8, q.load(q.lo)[2]])
   q.list[1] = (u'Shot button', sbt[1])
   q.lb.set_list(q.list, 1)
   q.cap.keys = (q.load(q.lo)[1], )

 def clr(q):
  import laa
  if q.load(q.lo)[0] == u'':
   NT(u'No Background','error')
   return 0
  pass
  q.save(q.lo, [u'', q.load(q.lo)[1], q.load(q.lo)[2]])
  NT(u'Background Cleared !')
  laa.execute(-2004318203)
  AP.set_exit()

 def cbg(q):
  import fy_manager as fm
  import laa
  try :
   d= fm.Manager().AskUser(ext=['.png', '.jpg'])
   if d == None : 
    return None
   q.save(q.lo, [d, q.load(q.lo)[1], q.load(q.lo)[2]])
   NT(u'Background Changed !', 'conf')
   laa.execute(-2004318203)
   AP.set_exit()
  except Exception, err : 
   NT((u'' + str(err)), 'error')


 def sel(q):
  ib = q.lb.current()
  if ib == 0 : 
   if q.list[0][1] == u'Active' : 
    q.list[0] = (u'Status', u'Deactive')
    q.cap.stop()
    q.lb.set_list(q.list, 0)
   elif q.list[0][1] == u'Deactive' : 
    q.list[0] = (u'Status', u'Active')
    q.cap.start()
    q.lb.set_list(q.list, 0)
   pass
  elif ib == 1 : 
   q.config()
  elif ib == 2 : 
   q.cu()
  elif ib == 3 : 
   q.abo()


 def cwm(q):
  from appuifw import selection_list as SL
  from os import listdir as listdir
  from zipfile import ZipFile as ZF
  import laa
  AP.title=(unicode(q.w))
  exe = (q.mfo + 'WMStore\\')
  zif = []
  alf = listdir(exe)
  for h in alf:
   if h.lower().endswith('.fsw') : 
    zif.append((u'' + h))
  cse = SL(zif, 1)
  if cse == None :
   AP.title= u'F-Screen' 
   return None
  try :
   NT(u'Loading watermark...')
   a = ZF((exe + zif[cse]), 'r')
   for i in a.namelist():
    b = open((q.mfo + i), 'wb')
    b.write(a.read(i))
    b.close()
   w=zif[cse]
   q.save(q.lo, [q.load(q.lo)[0], q.load(q.lo)[1], w])
   laa.execute(-2004318203)
   AP.set_exit()
  except Exception, err : 
   NT((u'' + str(err)), 'error')


 def mi(q):
  from appswitch import switch_to_bg as STB
  STB(u'F-Screen')


 def abo(q):
  from globalui import global_msg_query as GMQ
  GMQ(q.un(('F-Screen (v2.0)\n.::Screenshot will be saved in ' + mf + 'CosmoTech\\Captured\\\n\nCopyright \xc2\xa9 2018, Cosmo TechZone\nhttp://cosmotz.blogspot.com')), u'About')

utama()
