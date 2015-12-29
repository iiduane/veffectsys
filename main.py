#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

exit_flag = 0

class myThread(threading.Thread):
	"""docstring for ClassName"""
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print "starting  thread: " + self.name
		print_time(self.name, self.counter, 5)
		print "Exiting  thread: " + self.name


def print_time(threadName, delay, counter):
	while counter:
		if exit_flag:
			thread.exit()
		time.sleep(delay)
		print "%s: time: %s\n" % (threadName, time.ctime(time.time()))
		counter -= 1


threadLock = threading.Lock()
threads = []

thread1 = myThread(1, "thread-1", 1)
thread2 = myThread(2, "thread-2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
	t.join()
print "Exiting Main Thread!"








 