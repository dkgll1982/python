from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

packet = io.BytesIO()

# 使用Reportlab创建一个新的PDF
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(10, 100, "Hello world")
can.save()

#buffer从偏移0开始
packet.seek(0)
new_pdf = PdfFileReader(packet)

#读取已有的PDF
existing_pdf = PdfFileReader(open(r"C:\Users\dkgll\Desktop\python目录\pdf\test.pdf", "rb"))
output = PdfFileWriter()

page = existing_pdf.getPage(0)
page.rotateClockwise(90)                #将第0页旋转90度
page.mergePage(new_pdf.getPage(0))
output.addPage(page)

# 最后，向目标的pdf写出
#查了资料，关于open()的mode参数： 
#'r'：读 
#'w'：写 
#'a'：追加 
#'r+' == r+w（可读可写，文件若不存在就报错(IOError)） 
#'w+' == w+r（可读可写，文件若不存在就创建） 
#'a+' ==a+r（可追加可写，文件若不存在就创建） 
#对应的，如果是二进制文件，就都加一个b就好啦： 
#'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+' 
outputStream = open(r"C:\Users\dkgll\Desktop\python目录\pdf\test2.pdf", "wb+")
output.write(outputStream)
outputStream.close()