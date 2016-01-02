#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# for ui start

## 此处如果使用 import Tkinter 会有一些参数 不识别
from Tkinter import *




rootui = Tk()

li =['c', 'python', 'php', 'html' , 'sql']

movie =['css', 'pyman', 'phper']


# set ui main parameter
rootui.title("veffectsys")
rootui.geometry('640x480')
rootui.resizable(width=False, height=True)

# define Lable.
l1 = Label(rootui, text="Label for Menu", bg="blue", font=("Arial", 12),  height=4)
l1.pack()

l2 = Label(rootui, text="Label for Notice", bg="green", font=("Arial", 12),  height=4)
l2.pack()



frm_large = Frame(rootui)

frm_left =Frame(frm_large)

frm_right =Frame(frm_large)

listb = Listbox(frm_left)
listb2 = Listbox(frm_right)

for item in li:
	listb.insert(0, item)

for item in movie:
	listb2.insert(0, item)

listb.pack()
listb2.pack()

frm_left.pack(side=LEFT)
frm_right.pack(side=RIGHT)
frm_large.pack()

print "ui print start."

rootui.mainloop()

print "ui print end."


