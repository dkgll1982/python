import shutil
f1 = open(r"backup\note.txt","r")
f2 = open(r"backup\note2.txt","a+")
shutil.copyfileobj(f1,f2,length=1024)

shutil.copytree(r"backup\pdf",r'backup\pdf2')
