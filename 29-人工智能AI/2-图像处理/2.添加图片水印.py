from PIL import Image, ImageDraw
  
def add_watermark_to_image(image, watermark):
  rgba_image = image.convert('RGBA')
  rgba_watermark = watermark.convert('RGBA')
  
  image_x, image_y = rgba_image.size
  watermark_x, watermark_y = rgba_watermark.size
  
  # 缩放图片
  scale = 10
  watermark_scale = max(image_x / (scale * watermark_x), image_y / (scale * watermark_y))
  new_size = (int(watermark_x * watermark_scale), int(watermark_y * watermark_scale))
  rgba_watermark = rgba_watermark.resize(new_size, resample=Image.ANTIALIAS)
  # 透明度
  rgba_watermark_mask = rgba_watermark.convert("L").point(lambda x: min(x, 180))
  rgba_watermark.putalpha(rgba_watermark_mask)
  
  watermark_x, watermark_y = rgba_watermark.size
  # 水印位置
  # rgba_image.paste(rgba_watermark, (image_x - watermark_x, image_y - watermark_y), rgba_watermark_mask) #右下角
  rgba_image.paste(rgba_watermark, (image_x - watermark_x, 0), rgba_watermark_mask) # 右上角
  
  return rgba_image
  
im_before = Image.open("my.jpg")
im_before.show()
  
im_watermark = Image.open("AJUN水印.png")
im_after = add_watermark_to_image(im_before, im_watermark)
im_after.show()