#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# for ui start

import os
## 此处如果使用 import Tkinter 会有一些参数 不识别
from Tkinter import *
#from xml.dom.minidom import *
import xml.dom.minidom



####　class of xml parse   ############

## class logxmlparse(xml.sax.ContentHandler):

file_url = "F:/CreativePrj/python_prj/veffectsys/ext_keywords_config/main_parse.xml"

class logparse():

	def __init__(self):
		logparse_name = ""
		keyword = ""
		keyword_and = ""
		type = ""
		priority = ""
		wholeword = ""
		casesense = ""
		line_before = "0"
		line_before_keyword = ""
		line_after = "0"
		line_after_keyword = ""
		related_name = ""
		description = " This is init in class logparse!!"
		print "init completed."
	logparse_name = ""
	keyword = ""
	keyword_and = ""
	type = ""
	priority = ""
	wholeword = ""
	casesense = ""
	line_before = ""
	line_before_keyword = ""
	line_after = ""
	line_after_keyword = ""
	related_name = ""
	description = ""

	def print_all(self):
		print "\n**** logparse print all ****"
		print "logparse_name = %s; keyword = %s;  keyword_and=%s; type = %s;"  % (self.logparse_name, self.keyword, self.keyword_and, self.type)
		print "priority = [%s]  wholeword = [%s]  casesense = [%s]" % (self.priority, self.wholeword, self.casesense)
		print "line_before = [%s]  line_before_keyword = [%s]  line_after = [%s]" % (self.line_before, self.line_before_keyword, self.line_after)
		print "line_after_keyword = [%s] related_name = [%s]  description = [%s] " % (self.line_after_keyword, self.related_name, self.description)
		print "******** end of log print all ******\n"

	def tagvalues(self):
		tag_list = [self.logparse_name, self.keyword, self.keyword_and, self.type, \
self.priority, self.wholeword, self.casesense, \
self.line_before, self.line_before_keyword, self.line_after, \
self.line_after_keyword, self.related_name, self.description ]
		return tag_list  ## return a list contain self. xxx .


if os.path.exists(file_url):
	print "file exits url : %s" % file_url
	try:
		print "start to parse xml"
		xml_domtree = xml.dom.minidom.parse(file_url)
	except Exception, e:
		print "xml file is not a goot xml!"

else:
	print "file is not exits url: %s" % file_url


xmlnode = xml_domtree.documentElement

if xmlnode.hasAttribute("title"):
	keywords_title = xmlnode.getAttribute("title")
	print "Root element: %s" % keywords_title

subnodes = xmlnode.getElementsByTagName("logparse_set")

cntsub = 0
xmlnode_logparse_list = []
for subnode in subnodes:
	print "***** sub [%d]  ****** " % cntsub
	xlogparse = logparse()
	if subnode.hasAttribute("name"):
		xlogparse.logparse_name = subnode.getAttribute("name")
	xlogparse.keyword = subnode.getElementsByTagName('keyword')[0].childNodes[0].data
	xlogparse.type = subnode.getElementsByTagName('type')[0].childNodes[0].data
	xlogparse.priority = subnode.getElementsByTagName('priority')[0].childNodes[0].data
	xlogparse.wholeword = subnode.getElementsByTagName('wholeword')[0].childNodes[0].data
	xlogparse.casesense = subnode.getElementsByTagName('casesense')[0].childNodes[0].data
	xlogparse.line_before = subnode.getElementsByTagName('line_before')[0].childNodes[0].data
	xlogparse.line_before_keyword = subnode.getElementsByTagName('line_before_keyword')[0].childNodes[0].data
	xlogparse.line_after = subnode.getElementsByTagName('line_after')[0].childNodes[0].data
	xlogparse.line_after_keyword = subnode.getElementsByTagName('line_after_keyword')[0].childNodes[0].data
	xlogparse.related_name = subnode.getElementsByTagName('related_name')[0].childNodes[0].data
	xlogparse.description = subnode.getElementsByTagName('description')[0].childNodes[0].data
	xlogparse.print_all()
	xmlnode_logparse_list.append(xlogparse)
	print "append xlogparse[%d] \n\n" % cntsub
	cntsub += 1


####  end of xml parse   #########


#### search keys  ####
def find_file_by_pattern(pattern='.*', base="bbklog", circle=True):
	'''查找给定文件夹下面所有 '''
	re_file = re.compile(pattern)
	if base == ".":
		base = os.getcwd()

	final_file_list = []
	print base
	cur_list = os.listdir(base)
	for item in cur_list:
		if item == ".svn" or item == ".repo" or item ==".git":
			continue

		full_path = os.path.join(base, item)
		if full_path.endswith(".doc") or \
			full_path.endswith(".bmp") or \
			full_path.endswith(".wpt") or \
			full_path.endswith(".dot"):
			continue

		# print full_path
		bfile = os.path.isfile(item)
		if os.path.isfile(full_path):
			if re_file.search(full_path):
				final_file_list.append(full_path)
		else:
			final_file_list += find_file_by_pattern(pattern, full_path)
	return final_file_list


####  end search keys ####

search_dir_url = "F:/CreativePrj/python_prj/veffectsys"
file_list = find_file_by_pattern(".xml", search_dir_url)
print file_list

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
frm_menu.pack_propagate(0)  ## 使得 frame 不随 内部控件大小而变化


def menu_of_open():
	print 'Open file'

def menu_of_edit():
	print 'Open edit'

def menu_of_set():
	print 'Open set'

def menu_of_help():
	print 'Open help'
# create menu
# menu_dict = { '打开':menu_of_open, '编辑':menu_of_edit, '设置': menu_of_set, '帮助':menu_of_help}

menuname_list = ['打开','编辑','设置','帮助']
menufunc_list = [menu_of_open, menu_of_edit, menu_of_set, menu_of_help]

menu_bar = Menu(frm_menu)
## for ikey, ivalue in menu_dict.items():
for ikey, ivalue in zip(menuname_list, menufunc_list):
	print 'ikey: ' + ikey + '  ivalue: ' + str(ivalue)
	menu_bar.add_command(label = ikey, command = ivalue)

rootui['menu'] = menu_bar


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
mright_xsize = 148

# anchor   justfy 的含义还不明确
keywords_titlelb = Label(frm_mright, text="KeyWords Title:  " + keywords_title, bg="green", font=("Arial", 12), height= 1, anchor='w', justify="left" )
keywords_titlelb.pack(side =TOP)
listb = Listbox(frm_mright, height= middle_ysize, width = 20)
for item in li:
	listb.insert(0, item)
listb.pack(side=LEFT, expand = NO, fill = Y)

# frm_right_text = Frame(frm_mright)
# frm_right_text.pack(side= TOP)
showtexts = ['one text show', 'two text show', 'three text show', 'four text show']
for showtext in showtexts:
	showtw = Text(frm_mright, height=10,  width = mright_xsize)
	showtw.insert(1.0, showtext)
	showtw['state'] = 'disabled'  ## 设置 text 只读状态
	showtw.pack()

frm_mright.pack(side=LEFT, expand=YES, fill =Y)

frm_middle.pack()

# define command frame and input entry
frm_command = Frame(frm_large, bg='red')
frm_command.pack()  ##  如果要独占一行 就不要使用 side expand fill 这些参数指定值
command_lb = Entry(frm_command, text="Text command", bg="orange", font=("Arial", 12), width= large_xsize)
command_lb.pack( expand= YES, fill = X)

print "*******  >>>>  sys.executable:  " + sys.executable + "  sys.platform: " + sys.platform
if sys.platform == 'win32' or sys.platform == 'win64':
	print "get tkdnd library dir: "
	os.environ['TKDND_LIBRARY'] = os.path.join(os.path.dirname(sys.executable), 'tkdnd2.7')

print "os.getcwd() : " + os.getcwd()
##dnd = TkDND(frm_command)

#define  statusbar frame
frm_statusbar = Frame(frm_large, bg= 'grey')
frm_statusbar.pack()
statusbar_tw = Label(frm_statusbar, height=1, bg="pink",  width = large_xsize)
statusbar_tw.pack(expand = YES, fill = X)



frm_large.pack()

print "ui print start."

rootui.mainloop()

print "ui print end."


