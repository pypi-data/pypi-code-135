from PIL import Image as i

l1=""
l2=""
l3=""
l4=""
l5=""
nl=""
sp=""

def set_layers(layers):
  global nl
  nl=layers

def set_directory(layer, path):
  global l1, l2, l3, l4, l5
  if layer == "1":
    l1=path
  if layer == "2":
    l2=path
  if layer == "3":
    l3=path
  if layer == "4":
    l4=path
  if layer == "5":
    l5=path

def save_to(path):
  global sp
  sp=path


def generate(code):
  global l1, l2, l3, l4, l5, nl, sp
  nl=int(nl)
  c=str(code)
  if len(c) != nl:
    return "Code too long/short"

  width = (l1.width - l1.width) // 2
  height = (l1.height - l1.height) // 2

  if nl == 2:
    ly1 = i.open(l1+c[0]+".png", 'r')
    ly2 = i.open(l2+c[1]+".png", 'r')
    
    ly1.paste(ly2, (width, height), ly2)
  elif nl == 3:
    ly1 = i.open(l1+c[0]+".png", 'r')
    ly2 = i.open(l2+c[1]+".png", 'r')
    ly3 = i.open(l3+c[2]+".png", 'r')

    ly1.paste(ly2, (width, height), ly2)
    ly1.paste(ly3, (width, height), ly3)
  elif nl == 4:
    ly1 = i.open(l1+c[0]+".png", 'r')
    ly2 = i.open(l2+c[1]+".png", 'r')
    ly3 = i.open(l3+c[2]+".png", 'r')
    ly4 = i.open(l4+c[3]+".png", 'r')

    ly1.paste(ly2, (width, height), ly2)
    ly1.paste(ly3, (width, height), ly3)
    ly1.paste(ly4, (width, height), ly4)
  elif nl == 5:
    ly1 = i.open(l1+c[0]+".png", 'r')
    ly2 = i.open(l2+c[1]+".png", 'r')
    ly3 = i.open(l3+c[2]+".png", 'r')
    ly4 = i.open(l4+c[3]+".png", 'r')
    ly5 = i.open(l5+c[4]+".png", 'r')

    ly1.paste(ly2, (width, height), ly2)
    ly1.paste(ly3, (width, height), ly3)
    ly1.paste(ly4, (width, height), ly4)
    ly1.paste(ly5, (width, height), ly5)

  l1.save(sp+c+".png", format="png")


def mass_generate(start_code, end_code):
  r=int(end_code)-int(start_code)
  r=r+1
  sk=0
  cn=0
  if cn != r:
    tg=int(start_code)+sk
    generate(tg)
    sk=sk+1
    cn=cn+1

def view(code):
  generate(code)
  im = i.open(sp+code+".png")
  im.show()

def possibilities():
  tpb=10**nl
  return tpb

def genewrite(code, text):
  global l1, l2, l3, l4, l5, nl, sp
  nl=int(nl)
  c=str(code)
  if len(c) != nl:
    return "Code too long/short"

  width = (l1.width - l1.width) // 2
  height = (l1.height - l1.height) // 2

  if nl == 2:
    ly1 = i.open(l1+c[0]+".png", 'r')
    ly2 = i.open(l2+c[1]+".png", 'r')
    
    ly1.paste(ly2, (width, height), ly2)
  elif nl == 3:
    ly1 = i.open(l1+c[0]+".png", 'r')
    ly2 = i.open(l2+c[1]+".png", 'r')
    ly3 = i.open(l3+c[2]+".png", 'r')

    ly1.paste(ly2, (width, height), ly2)
    ly1.paste(ly3, (width, height), ly3)
  elif nl == 4:
    ly1 = i.open(l1+c[0]+".png", 'r')
    ly2 = i.open(l2+c[1]+".png", 'r')
    ly3 = i.open(l3+c[2]+".png", 'r')
    ly4 = i.open(l4+c[3]+".png", 'r')

    ly1.paste(ly2, (width, height), ly2)
    ly1.paste(ly3, (width, height), ly3)
    ly1.paste(ly4, (width, height), ly4)
  elif nl == 5:
    ly1 = i.open(l1+c[0]+".png", 'r')
    ly2 = i.open(l2+c[1]+".png", 'r')
    ly3 = i.open(l3+c[2]+".png", 'r')
    ly4 = i.open(l4+c[3]+".png", 'r')
    ly5 = i.open(l5+c[4]+".png", 'r')

    ly1.paste(ly2, (width, height), ly2)
    ly1.paste(ly3, (width, height), ly3)
    ly1.paste(ly4, (width, height), ly4)
    ly1.paste(ly5, (width, height), ly5)

  ly1.text((230, 450), text)

  ly1.save(sp+c+".png", format="png")