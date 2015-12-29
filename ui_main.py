#!/usr/bin/python
# -*- coding: UTF-8 -*-
# for ui start

import Tkinter

rootui = Tkinter.Tk()

li =['c', 'python', 'php', 'html' , 'sql']

movie =['css', 'pyman', 'phper']

frm_left = Tkinter.Frame(rootui)


listb = Tkinter.Listbox(rootui)
listb2 = Tkinter.Listbox(rootui)

for item in li:
	listb.insert(0, item)

for item in movie:
	listb2.insert(0, item)

# set ui main parameter
rootui.title("veffectsys")
rootui.geometry('640x480')
rootui.resizable(width=False, height=True)


listb.pack()
listb2.pack()

# define Lable.
l1 = Tkinter.Label(rootui, text="show this text", bg="blue", font=("Arial", 12),  height=4)
l1.pack()



print "ui print start."

rootui.mainloop()

print "ui print end."


