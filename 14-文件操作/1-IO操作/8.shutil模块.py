import shutil
f1 = open(r"C:\Users\dkgll\Desktop\python目录\note.txt","r")
f2 = open(r"C:\Users\dkgll\Desktop\python目录\note2.txt","a+")
shutil.copyfileobj(f1,f2,length=1024)

shutil.copytree(r"C:\Users\dkgll\Desktop\python目录\pdf",r'C:\Users\dkgll\Desktop\python目录\pdf2')
