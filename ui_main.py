#!/usr/bin/python
# -*- coding: UTF-8 -*-
####### -*- coding: cp936 -*-
# for ui start

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')   ###  解决 读log文件时 UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 97: ordinal not in range(128)报错
## 此处如果使用 import Tkinter 会有一些参数 不识别
from Tkinter import *
#from xml.dom.minidom import *
import xml.dom.minidom



####  error collect #####

# UnicodeDecodeError: ‘utf-8’ codec can’t decode byte 0xbf in position 21: invalid start byte
# 这是因为所使用的编码不对所导致的，比如我这里使用的是UTF-8，而实际上应该采用GBK才对。
## http://blog.csdn.net/chenggong2dm/article/details/31386359
############# end  #############

#######   import support of tkdnd    ##############



#获取脚本文件的当前路径
curr_path = os.getcwd()
print "curr_path: " + curr_path
print "*******  >>>>  sys.executable:  " + sys.executable + "  sys.platform: " + sys.platform
if sys.platform == 'win32' or sys.platform == 'win64':
	print "get tkdnd library dir: "
	os.environ['TKDND_LIBRARY'] = os.path.join(curr_path, 'support_lib/tkdnd2.8')


#from vtkdnd import TkDND
from vtkdnd import *

######  end of tkdnd  #######################



####　class of xml parse   ############

## class logxmlparse(xml.sax.ContentHandler):

## xmlconfig_file_url = "F:/CreativePrj/python_prj/veffectsys/ext_keywords_config/main_parse.xml"
xmlconfig_file_url = os.path.join(curr_path, 'ext_keywords_config/main_parse.xml')
print "[xmlconfig_file_url]: " + xmlconfig_file_url
report_file_url = os.path.join(curr_path, 'report/report.log')
input_log_path = ""

class logparse():

	def __init__(self):
		logparse_name = ""
		logparse_savefile_url = "report.temp.log"
		file_type =".log"
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
	logparse_savefile_url = ""
	file_type = ""
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
		print "logparse_name = %s; file_type: %s, keyword = %s;  keyword_and=%s; type = %s;"  % (self.logparse_name, self.file_type, self.keyword, self.keyword_and, self.type)
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


if os.path.exists(xmlconfig_file_url):
	print "file exits url : %s" % xmlconfig_file_url
	try:
		print "start to parse xml"
		xml_domtree = xml.dom.minidom.parse(xmlconfig_file_url)
	except Exception, e:
		print "xml file is not a goot xml!"

else:
	print "file is not exits url: %s" % xmlconfig_file_url


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
	if subnode.hasAttribute("savefile_url"):
		xlogparse.logparse_savefile_url = subnode.getAttribute("savefile_url")
	xlogparse.file_type = subnode.getElementsByTagName('file_type')[0].childNodes[0].data
	xlogparse.keyword = subnode.getElementsByTagName('keyword')[0].childNodes[0].data
	logparse.keyword_and = subnode.getElementsByTagName('keyword_and')[0].childNodes[0].data
	#xlogparse.keyword_and = subnode.getElementsByTagName('keyword_and')[0].childNodes[0].data
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


rootui = Tk()

li =['c for title']

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
showtexts = ['Search keys:']
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

cmd_left_lb = Label(frm_command,text ='Command')
cmd_left_lb.pack(side=LEFT)

################################################################
#### # Python的标准库linecache模块非常适合这个任务
#### import linecache
#### the_line = linecache.getline('d:/FreakOut.cpp', 222)
#### print (the_line)
#### # linecache读取并缓存文件中所有的文本，
#### # 若文件很大，而只读一行，则效率低下。
#### # 可显示使用循环, 注意enumerate从0开始计数，而line_number从1开始
#### def getline(the_file_path, line_number):
####   if line_number < 1:
####     return ''
####   for cur_line_number, line in enumerate(open(the_file_path, 'rU')):
####     if cur_line_number == line_number-1:
####       return line
####   return ''
#### the_line = linecache.getline('d:/FreakOut.cpp', 222)
#### print (the_line)

#### ###################################################


def searchkey(fileurl, mode, logparse_list, fileout='F:/templog/report.temp.txt', outmode='a+'):
	if os.path.exists(fileurl):
		filefp = open(fileurl, mode)
	else:
		pass
		#print "Search file: " + fileurl + " is not exist!!!!"
		#return None
	fileoutfp = open(fileout, outmode)

	print "searching file_url: " + fileurl
	try:
		nline = 0
		keycnt = 0
		keylines = []
		for line_not_utf8 in filefp:
			line = line_not_utf8.decode('latin-1').encode("utf-8")  #  UnicodeDecodeError: 'utf8' codec can't decode byte 0xd4 in position 54: invalid continuation byte
			nline += 1
			for logk_item in logparse_list:
				##  print "KEYWORD: %s ; KEYWORDAND: %s" % (logk_item.keyword, logk_item.keyword_and)
				if (not logk_item.keyword=="") and  (not logk_item.keyword_and == ""):
					if (not (line.find(logk_item.keyword) == -1)) and (not (line.find(logk_item.keyword_and) == -1)):
						keycnt +=1
						print "sec nline:"
						print  nline
						print "sec line:"
						print line
						appendstrlist = [str(keycnt),str(nline), line]
						keylines.append(appendstrlist)
				elif not logk_item.keyword=="":
					if not (line.find(logk_item.keyword) == -1):
						keycnt +=1
						print "nline:"
						print  nline
						print "line:"
						print line
						appendstrlist = [str(keycnt),str(nline), line]

						#fileoutfp.writelines(str(keycnt) + str(nline) + line)
						#fileoutfp.flush()
						keylines.append(appendstrlist)
				else:
					print "search nothing!!"
					#appendstrlist = ["0","None", " Nothing Found!!!!"]
					#keylines.append(appendstrlist)

		# print out to outfiles.
		keylinesprint = ""
		keylcnt = 0
		for item in keylines:
			keylcnt +=1
			keylinesprint += "-[cnt]:  %s, linenum: %s \n-[lineContent]:\n%s" % (item[0], item[1], item[2])
		allprint = "\n[keyword]: %s ; [keywordand]:%s ; \n[keycnt]:%d ; \n[fileurl]:\n%s\n[keylinesfull]:\n -----------------------------------------------------------------\n%s\n**************************  split up and down  *******************************\n\n\n" % \
				   (logk_item.keyword, logk_item.keyword_and, keycnt, fileurl, keylinesprint)

		print allprint
		#只有匹配到时，才打印出来
		if keycnt == 0:
			print "Don't print "
		else:
			fileoutfp.writelines(allprint)
			fileoutfp.flush()
		return logk_item.keyword, logk_item.keyword_and, keycnt, keylines

	finally:
		filefp.close()
		fileoutfp.close()

def enter_hander_for_entry(event):
	print "bind hander str: " +  str_input.get()
	## str_input = command_lb.get()
	str_input.set(command_lb.get())
	input_log_path = str_input.get()
	if xlogparse.logparse_savefile_url == "":
		xlogparse.logparse_savefile_url = "default.report.log"

	input_log_path = os.path.join(input_log_path, xlogparse.logparse_savefile_url)
	print "bind hander after set : " +  str_input.get()
	# 从输入框获取 目录路径
	allthe_filelist = find_file_by_pattern(".*", str_input.get())
	result_list = []
	for item in allthe_filelist:
		#sresult = searchkey(item.decode('latin-1').encode("utf-8") , 'r', xmlnode_logparse_list)
		sresult = searchkey(item , 'r', xmlnode_logparse_list, input_log_path)
		if not sresult:
			print "file not exist! can't open"
			continue
		else:
			result_list.append(sresult)

	for item2 in result_list:
		print "\n\n----------- start ************"
		print item2[0]
		print type(item2[0])
		print item2[1]
		print type(item2[1])
		print item2[2]
		print type(item2[2])
		## print logparse.keyword, logparse.keyword_and, keycnt
		showinbox = "%s + %s  (%d)" % (str(item2[0]), item2[1], item2[2])  ####  多个变量一起打印，不加括号，会报错
		showtw.insert(END, showinbox)
		##showtw.update()
		##showtw.update_idletasks()
		print "--------------------- end ************"

	#rootui.update()
	##rootui.update_idletasks()

str_input = StringVar()
input_dnd = TkDND(frm_command)
command_lb = Entry(frm_command, textvariable = str_input, text="Text command", font=("Arial", 12), width= large_xsize-20)
str_input.set('Please input log url ,or drag and drop a directory containing log')
print "str input ********************"
print str_input.get()
# response for enter key.
command_lb.bind('<Return>', enter_hander_for_entry	)

command_lb.pack(side=LEFT, expand= YES, fill = X)

## support drag in commandlb entry.
def drag_handle(event):
	event.widget.insert(0, event.data)

input_dnd.bindtarget(command_lb, drag_handle, 'text/uri-list')



def func_enter_text():
	print "enter str: " +  str_input.get()
	## str_input = command_lb.get()
	str_input.set(command_lb.get())
	print "enter str after set : " +  str_input.get()


def func_clear_text():
	command_lb.delete(0, END)
	str_input.set("")

def func_get_text():
	lbstr = command_lb.get()
	print "lbstr: " + lbstr

enter_btn = Button(frm_command, text= "Enter", command = func_enter_text)
enter_btn.pack(side=LEFT)
clear_btn = Button(frm_command, text= "Clear", command = func_clear_text)
clear_btn.pack(side=LEFT)
get_btn = Button(frm_command, text= "Get", command = func_get_text)
get_btn.pack(side=LEFT)


#print "*******  >>>>  sys.executable:  " + sys.executable + "  sys.platform: " + sys.platform
#if sys.platform == 'win32' or sys.platform == 'win64':
#	print "get tkdnd library dir: "
#	os.environ['TKDND_LIBRARY'] = os.path.join(os.path.dirname(sys.executable), 'tkdnd2.7')
#
#print "os.getcwd() : " + os.getcwd()
###dnd = TkDND(frm_command)

#define  statusbar frame
frm_statusbar = Frame(frm_large, bg= 'grey')
frm_statusbar.pack()
statusbar_tw = Label(frm_statusbar, height=1, bg="pink",  width = large_xsize)
statusbar_tw.pack(expand = YES, fill = X)



frm_large.pack()

print "ui print start."

# 保持窗口实时更新

## rootui.update_idletasks()
rootui.mainloop()

print "ui print end."


