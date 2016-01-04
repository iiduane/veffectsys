#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# for ui start

import os
import sys
from Tkinter import *
#获取脚本文件的当前路径
curr_path = os.getcwd()
print "curr_path: " + curr_path
print "*******  >>>>  sys.executable:  " + sys.executable + "  sys.platform: " + sys.platform
if sys.platform == 'win32' or sys.platform == 'win64':
	print "get tkdnd library dir: "
	os.environ['TKDND_LIBRARY'] = os.path.join(curr_path, 'support_lib/tkdnd2.8')
	#os.environ['TKDND_LIBRARY'] = os.path.join(os.path.dirname(sys.executable), 'tkdnd2.8')
	#os.environ['TKDND_LIBRARY'] = "C:/Python27/tkdnd2.8"


#from vtkdnd import TkDND
from vtkdnd import *

############### file DnD.py  ###############################################################

'''Python wrapper for the tkDnD tk extension.'''


def test(root):
    dnd = DnD(root)
    Label(root, text='Drop files from your file manager into the listbox').pack(side='top')
    l = Listbox(root)
    l.pack(side='top', fill='both', expand=1)
    root.update()# may be necessary on unix
    # now make the listbox a drop target:

    def drag(action, actions, type, win, X, Y, x, y, data):
        return action

    def drag_enter(action, actions, type, win, X, Y, x, y, data):
        l.focus_force()
        return action

    def drop(action, actions, type, win, X, Y, x, y, data):
        files = data.split()
        for f in files:
            l.insert('end', f)

    dnd.bindtarget(l, 'text/uri-list', '<Drag>', drag, ('%A', '%a', '%T', '%W', '%X', '%Y', '%x', '%y', '%D'))
    dnd.bindtarget(l, 'text/uri-list', '<DragEnter>', drag_enter, ('%A', '%a', '%T', '%W', '%X', '%Y', '%x', '%y', '%D'))
    dnd.bindtarget(l, 'text/uri-list', '<Drop>', drop, ('%A', '%a', '%T', '%W', '%X', '%Y', '%x', '%y','%D'))



# first example --------
root = Tk()

dnd = TkDND(root)

entry = Entry()
entry.pack(side=TOP, expand =YES, fill = 'both')

def handle(event):
    event.widget.insert(0, event.data)

dnd.bindtarget(entry, handle, 'text/uri-list')

## second example
test(root)

root.mainloop()