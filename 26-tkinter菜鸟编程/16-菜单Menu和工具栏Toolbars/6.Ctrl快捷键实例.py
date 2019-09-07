# encoding=utf-8
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import os
'''打开文件的功能目前不是很完善'''
 
filename = ''
def author():
	showinfo('helo', 'linlin')
 
def power(*args):
	showinfo('版权信息', '版权信息不保留，随便拷贝')
 
def myopen(*args):
	global filename
	filename = askopenfilename(defaultextension = '.txt')
	if filename == '':
		filename = None
	else:
		root.title('linlin-note' + os.path.basename(filename))
		textPad.delete(1.0, END)
		f = open(filename, 'r')
		textPad.insert(1.0, f.read())
		f.close()
 
def new(*args):
	global root, filename, textPad
	root.title('未命名文件')
	filename = None
	textPad.delete(1.0, END)
 
def save(*args):
	global filename
	try:
		f = open(filename, 'w')
		msg = textPad.get(1.0, 'end')
		f.write(msg)
		f.close()
	except:
		saveas()
 
def saveas(*args):
	f = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
	global filename
	filename = f
	fh = open(f, 'w')
	msg = textPad.get(1.0, END)
	fh.write(msg)
	fh.close
	root.title('linlin 记事本'+os.path.basename(f))
 
def cut(*args):
	global textPad
	textPad.event_generate('<<Cht>>')
 
def copy(*args):
	global textPad
	textPad.event_generate('<<Copy>>')
 
def paste(*args):
	global textPad
	textPad.event_generate('<<Paste>>')
 
def undo(*args):
	global textPad
	textPad.event_generate('<<Undo>>')
 
def redo(*args):
	global textPad
	textPad.event_generate('<<Redo>>')
 
def select_all(*args):
	global textPad
	textPad.event_generate('sel', '1.0', 'end')
 
def find(*args):
	global root
	t = Toplevel(root)
	t.title('查找')
	# 设置窗口大小
	t.geometry('260x60+200+250')
	t.transient(root)
	Label(t,text='查找:').grid(row=0, column=0, sticky='e')
	v = StringVar()
	e = Entry(t, width=20, textvariable=v)
	e.grid(row = 0, column=1, padx=2, pady=2, sticky='we')
	e.focus_set()
	c = IntVar()
	Checkbutton(t, text='不区分大小写', variable=c).grid(row=1, column=1, sticky='e')
	Button(t, text='查找所有', command=lambda:search(v.get(), c.get(), textPad, t, e)).grid(row=0, column=2,sticky='e' + 'w', padx=2, pady=2)
 
	def close_search():
		textPad.tag_remove('match', '1.0', END)
		t.destroy()
	t.protocol('WM_DELETE_WINDOW', close_search)
 
def search(needle, cssnstv, textPad, t, e):
	textPad.tag_remove('match', '1.0', END)
	count = 0
	if needle:
		pos = '1.0'
		while True:
			pos = textPad.search(needle, pos, nocase = cssnstv, stopindex=END)
			if not pos: break
			lastpos = pos + str(len(needle))
			textPad.tag_add('match', pos, lastpos)
			count += 1
			pos = lastpos
		textPad.tag_config('match', foreground = 'yellow', background='green')
		e.focus_set()
		t.title(str(count) + '个被匹配')
def popup(event):
	global editmenu
	editmenu.tk_popup(event.x_root, event.y_root)
 
 
root = Tk()
root.title('林林记事本第一版')
root.geometry('300x300+100+100')
menubar = Menu(root)
 
filemenu = Menu(menubar)
filemenu.add_command(label='新建', accelerator='Ctrl+N', command=new)
filemenu.add_command(label='打开', accelerator='Ctrl+O', command=myopen)
filemenu.add_command(label='保存', accelerator='Ctrl+S', command=save)
filemenu.add_command(label='另存为', accelerator='Ctrl+Shift+S', command=saveas)
menubar.add_cascade(label='文件', menu=filemenu)
 
editmenu = Menu(menubar)
editmenu.add_command(label='撤销', accelerator='Ctrl+Z', command=undo)
editmenu.add_command(label='重做', accelerator='Ctrl+Y', command=redo)
editmenu.add_separator()
editmenu.add_command(label='剪切', accelerator='Ctrl+X', command=cut)
editmenu.add_command(label='复制', accelerator='Ctrl+C', command=copy)
editmenu.add_command(label='粘贴', accelerator='Ctrl+V', command=paste)
editmenu.add_separator()
editmenu.add_command(label='查找', accelerator='Ctrl+F', command=find)
editmenu.add_command(label='全选', accelerator='Ctrl+A', command=select_all)
menubar.add_cascade(label='编辑', menu=editmenu)
 
aboutmenu = Menu(menubar)
aboutmenu.add_command(label='作者', command=author)
aboutmenu.add_command(label='版权', command=power)
menubar.add_cascade(label='关于', menu=aboutmenu)
 
root.config(menu = menubar)
# root['menu'] = menubar
 
shortcutbar = Frame(root, height=25, bg='light sea green')
shortcutbar.pack(expand=NO, fill=X)
lnlabel = Label(root, width=2, bg='antique white')
lnlabel.pack(side=LEFT, anchor='nw', fill=Y)
 
textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)
scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command = textPad.yview)
scroll.pack(side=RIGHT,fill=Y)
 
textPad.bind('<Control-N>',new)
textPad.bind('<Control-n>',new)
textPad.bind('<Control-O>',myopen)
textPad.bind('<Control-o>',myopen)
textPad.bind('<Control-S>',save)
textPad.bind('<Control-s>',save)
textPad.bind('<Control-A>',select_all)
textPad.bind('<Control-a>',select_all)
textPad.bind('<Control-F>',find)
textPad.bind('<Control-f>',find)
 
textPad.bind('<Button-3>',popup)
 
root.mainloop()