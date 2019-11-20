import zipfile
import glob,os

filezip = zipfile.ZipFile(r'C:\Users\dkgll\Desktop\python目录\zip.zip','w')
for name in glob.glob(r'C:\Users\dkgll\Desktop\python目录\pdf\*'):
    print(os.path.basename(name))
    filezip.write(name,os.path.basename(name),zipfile.ZIP_DEFLATED)

filezip.close()

listzipinfo = zipfile.ZipFile(r'C:\Users\dkgll\Desktop\python目录\zip.zip','r')
print(listzipinfo.namelist())
print('\n')
for info in listzipinfo.infolist():
    print(info.filename,info.file_size,info.compress_size)

listzipinfo.extractall(r'C:\Users\dkgll\Desktop\python目录\zipfile')
listzipinfo.close()
