from PIL import Image, ImageDraw, ImageFont
im = Image.open(r"C:\Users\dkgll\Desktop\python目录\image\card_num\33052219960919454X.png")
logo=Image.open(r"C:\Users\dkgll\Desktop\python目录\image\sy.png") 

layer=Image.new('RGBA', im.size, (0,0,0,0))

layer.paste(logo, (im.size[0]-logo.size[0],im.size[1]-logo.size[1]))

out=Image.composite(layer,im,layer)

out.show()