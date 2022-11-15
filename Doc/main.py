import time

#Debug 
from src.Utils.Debug.Debug import Debug

#Graphic
from src.Graphic.Menu.Menu import Menu
from src.Graphic.Board.Board import Board

from src.System.Monitoring.Computer import Computer

from Keyboard.Keyboard import Keyboard


from src.System.WebServer import WebServer
from src.System.ThreadHandler.ThreadHandler import ThreadHandler, ThreadHandlerMode

from src.Downloader.MusicDownloader.MusicDownloader import MusicDownloader



def callback_1():
	pass

def callback_2(args):
	print(">>> "+str(args[0]))
	print(">>> "+str(args[1]))
	print(">>> "+str(args[2]))
	pass


def main():

	#Debug
	d = Debug()
	d.println("INIT")

	#System
	system = System()
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

	time.sleep(5)


	#Threads
	myThread_1 = ThreadHandler(0,"Thread-1")
	myThread_1.setCallback(callback_1)
	myThread_1.setDuration(1.0)
	myThread_1.setMode(ThreadHandlerMode.PERIODIC)
	myThread_1.start()

	myThread_2 = ThreadHandler(1,"Thread-2")
	myThread_2.setCallback(callback_2)
	myThread_2.setArgs([1,2,3])
	myThread_2.setDuration(5.0)
	myThread_2.setMode(ThreadHandlerMode.PERIODIC)
	myThread_2.start()


	#Server
	server = Server()
	server.setLocationFile("Server/index.html")
	server.setPort(9001)
	server.run()

    # downloader = MusicDownloader()

    # downloader.loadFile()
    # downloader.loadSettings()
    # downloader.downloadMusics()

	# menu = Menu("#")
	# menu.setColorOn((0,200,0), (0,00,00))
	# menu.setColorOff((255,0,0),(100,0,0))

	# board = Board("menu", 100, 50)
	# board.generateMenu(menu,["A", "B"], 5)
	# board.changeBackground("menu.txt", "menu", True)	


	# menu.selectMenu(1, board)

	# menu.display(board)


	# print(menu.getMaxInputs())
	# print(menu.getCurrentSelection())

	# keyboard = Keyboard()
	# keyboard.addSlot("UP", menu.moveUp, board)
	# keyboard.addSlot("ENTER", enterMenu, menu, keyboard, board)
	# keyboard.addSlot("TAB", menu.nextSelection, board)				#Permet de changer de selection lors de l'appui de touche TAB
	# keyboard.addSlot("DOWN", menu.moveDown, board)		
	# #board.progressBar('+', 20, 2,0.1, (10,10), (0,255,10), (0,0,0))
	# menu.display(board)

	# while(1):
        
	# 	keyboard.Interact()
	# 	menu.display(board)
	# 	time.sleep(0.01)

if(__name__ == "__main__"):

    main()
