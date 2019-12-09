import subprocess

#打开文本
subprocess.Popen(["notepad.exe", r"backup\备忘录.txt"])

#打开QQ
#subprocess.Popen(r'D:\应用程序\Tencent\QQ\Bin\QQScLauncher.exe')

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write('print(1) \n'.encode("utf-8"))
obj.stdin.write('print(2) \n'.encode("utf-8"))
obj.stdin.write('print(3) \n'.encode("utf-8"))
obj.stdin.write('print(4) \n'.encode("utf-8"))
obj.stdin.close()
cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()
print(cmd_out)
print(cmd_error)