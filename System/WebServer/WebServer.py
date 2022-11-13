#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run
import webbrowser

class WebServer(object):
	"Init Server"

	def __init__(self, location="/home/nico", port=8090, ip='127.0.0.1'):

		self.__location = location
		self.__port = port
		self.__ip = ip
		self.__data = ""

	def setLocationFile(self, filename):

		self.__location = filename

	def setContent(self, data):
		self.__data = data

	def setPort(self, port):

		self.__port = port

	def setIP(self, ip):

		self.__ip = ip

	def run(self):

		@route('/') 
		def ok(): 
			fichier = open(self.__location, "r")
			data = fichier.read()
			fichier.close()

			return  data 

		print("Localisation : " + self.__location)
		print("Port : " + str(self.__port))
		print("Ip : " + self.__ip)
		run(host=str(self.__ip), port=self.__port)

def main():

	server = WebServer()
	server.setLocationFile("index.html")
	server.setPort(9000)

	server.run()
	webbrowser.open("index.html")

if __name__ == "__main__":
	
	main()
        

		
		






