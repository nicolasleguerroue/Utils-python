#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import time

result = ""
indexCommands = 0
countCommands = 0
allCommands = []

class Serial (threading.Thread):
	"""Class for multithreading"""

	def __init__(self, threadID, name, ):
		"""Constructor of class"""
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.isRunning = True
		
	def initSerial(self, serialObject, commands):
		"""Init serial communication"""
		assert type(commands) is list

		global allCommands
		global countCommands
		global indexCommands

		self.serialObject = serialObject
		allCommands = commands
		indexCommands = 0
		
	def run(self):
		"""Start multithreading"""
		global allCommands
		global countCommands
		print("Starting " + self.name)
		countCommands = len(allCommands)
		while (self.isRunning==True): 	
			readData(self.serialObject, self.isRunning )
		#Stop 
		self.serialObject.write("G28 Z F4\n")
		print("<stop> ")
		
	def stop(self):
		"""Stop multithreading"""
		self.isRunning = False
		return True
		

		
def readData(serialObject):
	"""Start next command when 'ok' received"""

	char=serialObject.read() 	#Reading char by char
	global result
	global indexCommands
	global countCommands
	global allCommands
	if char=='\n': 				
		result=""
	else: 	

		result=result+char		#Concat
		if("ok" in result):		#Run next command if available
				
			if(indexCommands+1>=countCommands):
				print("All commands have been called, do nothing")
			else:
				print(">>> Command : "+str(allCommands[indexCommands]))
				serialObject.write(allCommands[indexCommands]+"\n")
				indexCommands+=1
				time.sleep(0.050)
			result = ""
			
		
