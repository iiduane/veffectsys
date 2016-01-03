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
# define window size.
# rootui.geometry('640x480')
rootui.resizable(width=False, height=False)


large_xsize = 140

frm_large = Frame(rootui)

# for menu place
frm_menu = Frame(frm_large, width= 800 , bg='yellow')
frm_menu.pack(side=TOP, expand =YES, fill= X)
#for tool box place
frm_tool = Frame(frm_large)
frm_tool.pack(side=TOP, expand =YES, fill= X)
#for notify place
frm_notify = Frame(frm_large)
frm_notify.pack(side=TOP, expand =YES, fill= X)

# define Lable for menu tool notify
menu_lb = Label(frm_menu, text="Label for Menu", bg="blue", font=("Arial", 12), width  = large_xsize)
menu_lb.pack(expand = YES, fill =X)
tool_lb = Label(frm_tool, text="Label for tool .....................", bg="green", font=("Arial", 12),  height=1)
tool_lb.pack(expand = YES,  fill =X)
notify_lb = Label(frm_notify, text="Label for Notice", bg="yellow", font=("Arial", 12),  height=1)
notify_lb.pack(expand = YES,  fill =X)

# define middle window frame
frm_middle = Frame(frm_large)
middle_ysize = 28

frm_leftsel =Frame(frm_middle,  bg='yellow')
frm_leftsel.pack(side=LEFT, expand = YES, fill = Y)
leftsel_lb = Label(frm_leftsel, text="Label Y", bg="green", font=("Arial", 12), height= middle_ysize, width= 8)
leftsel_lb.pack(side=LEFT, expand= YES, fill = Y)

frm_mright =Frame(frm_middle)
# define mright x size
mright_xsize = 128
listb = Listbox(frm_mright, height= middle_ysize, width = 40)
for item in li:
	listb.insert(0, item)
listb.pack(side=LEFT, expand = NO, fill = Y)

# frm_right_text = Frame(frm_mright)
# frm_right_text.pack(side= TOP)
showtexts = ['one text show', 'two text show', 'three text show', 'four text show']
for showtext in showtexts:
	showtw = Text(frm_mright, height=1,  width = mright_xsize)
	showtw.insert(1.0, showtext)
	showtw.pack()

frm_mright.pack(side=LEFT, expand=YES, fill =Y)

frm_middle.pack()

# define command frame and input entry
frm_command = Frame(frm_large, bg='red')
frm_command.pack()  ##  如果要独占一行 就不要使用 side expand fill 这些参数指定值
command_lb = Entry(frm_command, text="Text command", bg="orange", font=("Arial", 12), width= large_xsize)
command_lb.pack( expand= YES, fill = X)

frm_statusbar = Frame(frm_large, bg= 'grey')
frm_statusbar.pack()
statusbar_tw = Label(frm_statusbar, height=1, bg="pink",  width = large_xsize)
statusbar_tw.pack(expand = YES, fill = X)


frm_large.pack()

print "ui print start."

rootui.mainloop()

print "ui print end."


