
#!/usr/bin/env python3
#-- coding: utf-8 --

import os
import netifaces
import psutil

from .Temperature import Temperature
from .Memory import Memory
from .Interface import Interface
from .User import User


class Computer:

	def __init__(self):

		self.__localIP = None

		#Display settings
		cpus = psutil.cpu_count(logical=True)
	

	def temperatures(self):
		"""Temperatures handler"""

		temperatures = []
		for key in psutil.sensors_temperatures():
			temperatures.append(Temperature(key, float(psutil.sensors_temperatures()[key][0][1])))
		
		return temperatures


	def disk(self):
		"""Disk handler"""

		disk = psutil.disk_usage('/')

		total = round(disk.total/1024.0/1024.0,1)
		percent = disk.percent

		return percent

	def users(self):

		"""Users handler"""
		users = psutil.users()
		usersArray = []
		for u in users:
			usersArray.append(User(u.name, u.started))

		return usersArray

	def cpu(self):

		""" Check CPU value"""
		return int(psutil.cpu_percent())

	def memory(self):

		"""Check memory usage"""

		raw_memory = psutil.virtual_memory()

		available = round(raw_memory.available/1024.0/1024.0,1)
		used = round(raw_memory.used/1024.0/1024.0,1)
		all = round(raw_memory.total/1024.0/1024.0,1)
		percent = raw_memory.percent

		return Memory(available, used, all, percent)


	def webServer(self):

		response = None

		if(self.__localIP != None):
			response = os.system("ping -c 1 "+str(self.__localIP))
			return response
		return response

	
	def network(self):
		"""Network handler"""

		self.__key_network = 2 #key of dict when network is used
		self.__interfaces = []

		interfacesName = netifaces.interfaces() 

		interfaces = []
		for i in interfacesName:
			
			interface = netifaces.ifaddresses(i)
			keys = interface.keys()
			addresses = []
			if(2 in keys):

				for k in keys:
					addresses.append(interface[k][0]['addr'])
			interfaces.append(Interface(i, addresses))
		return interfaces

def main():

	#System
	system = Computer()
	print(">>> Temperatures : ")
	for temp in system.temperatures():
		print("\t'"+str(temp.name)+"' => "+str(temp.temperature)+" °C")

	print(">>> Disk usage : "+str(system.disk())+" %")
	print(">>> Users : ")

	for u in system.users():
		print("\t'"+str(u.name)+"' => "+str(u.ttl)+" s")

	print(">>> CPU : "+str(system.cpu())+" %")

	print(">>> Memory : ")
	memory = system.memory()
	print("\t"+str(memory.percent)+" % => "+str(memory.used)+"/"+str(memory.all))

	print(">>> Interfaces : ")
	interfaces = system.network()

	for i in interfaces:
		print("\tInterface : '"+str(i.name)+"'")
		for a in i.addresses:
			print("\t\t Address : "+str(a))

	print(">>> Web server : "+str(system.webServer()))

if(__name__ == "__main__"):
	
	main()