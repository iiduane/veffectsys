#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# for ui start

## 此处如果使用 import Tkinter 会有一些参数 不识别
from Tkinter import *




def vframe(root, side):
	w = Frame(root)
	w.pack(side=side,expand=YES, fill=BOTH)
	return w

def vbutton(root, side, text, command=None):
	w =Button(root, text=text, command=command)
	w.pack(side=side, expand=YES, fill=BOTH)
	return w

xroot = Tk()

# create vframe

frame1 = Frame(xroot)
frame_error = vframe(frame1, side=LEFT)
#frame_error.
frame_hourglass = vframe(frame1, side=LEFT)


frame2 = Frame(xroot)
frame_info = vframe(frame1, side=LEFT)
frame_info.configure(bg='green', bd=40)
frame_question = vframe(frame1, side=LEFT)


frame3 = Frame(xroot)
frame_warning = vframe(frame3, side=LEFT)
frame_gray75 = vframe(frame3, side=RIGHT)

frame1.pack(side=LEFT)
frame2.pack(side=RIGHT)
frame3.pack(side=LEFT)



# create Label
xlable =Label(frame_error, fg='blue', bg='yellow', text='Text error:')
xlable.pack()
xlable =Label(frame_error, bitmap='error')
xlable.pack()
xlable =Label(frame_hourglass, text='hourglass: ')
xlable.pack()
xlable =Label(frame_hourglass, bitmap='hourglass')
xlable.pack()
xlable =Label(frame_info, fg='blue', bg='yellow', text='text info:')
xlable.pack()
xlable =Label(frame_info, bitmap='info')
xlable.pack()
xlable =Label(frame_question, text='question:')
xlable.pack()
xlable =Label(frame_question, bitmap='question')
xlable.pack()
xlable =Label(frame_warning, fg='blue', bg='yellow', text='text warning:')
xlable.pack()
xlable =Label(frame_warning, bitmap='warning')
xlable.pack()
Checkbutton(frame_warning, text='set warning').pack()
xlable =Label(frame_gray75, text='gray75:')
xlable['background']='red'
xlable.pack()
xlable =Label(frame_gray75, bitmap='gray75')
xlable.pack()
Checkbutton(frame_gray75, text='set gray75').pack()

varstr = StringVar()
xtextinput = Entry(frame_gray75, textvariable =varstr)
varstr.set("good end.")
xtextinput.pack()

icnt = 0
def button_click():
	global icnt
	icnt +=1
	str(icnt)
	xt.insert('1.0', str(icnt)+": insert \n")
	print "insert.."

xt =Text()
xt.pack()

xbtn = Button(xroot, text = "InsertBtn", command = button_click)
xbtn.pack()

# frame_error.pack()
# frame_hourglass.pack()
# frame_info.pack()
# frame_question.pack()
# frame_warning.pack()
# frame_gray75.pack()



xroot.title('Ui study title')
xroot.mainloop()


