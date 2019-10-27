from PIL import Image, ImageDraw, ImageFont

def add_num(img,logo):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-250, 5), 'Hu huahua', font=myfont, fill=fillcolor)  

    # #添加图片 
    layer = Image.new('RGBA', img.size, (0,0,0,0)) 
    layer.paste(logo, (img.size[0]-logo.size[0],img.size[1]-logo.size[1])) 
    out = Image.composite(layer,img,layer)    
    #保存图片到目录下 
    out.save(r'C:\Users\dkgll\Desktop\python目录\image\result.jpg','jpeg')
    out.show()  

if __name__ == '__main__':
    image = Image.open(r"C:\Users\dkgll\Desktop\python目录\image\card_num\330522200509102025.png")
    logo=Image.open(r"C:\Users\dkgll\Desktop\python目录\image\sy.png") 
    add_num(image,logo)
    #image.show()