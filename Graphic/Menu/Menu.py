#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import Board
import Keyboard
import time

class Menu():

	def __init__(self, symbol):
	
		self.__menu = {
		'symbol':symbol,
		'txt_color_on':None,
		'bg_color_on':(255,100,100), 								#par défaut, le fond d'écran des éléments selectionné est noir
		'txt_color_off':None,
		'bg_color_off':(0,0,0), 						#par défaut, le fond d'écran des éléments non selectionné est noir
		'current_selection':1,								#l'index des sélection commence à 1
		'last_selection':0,
		'trigger':True,												#permet de savoir si le menu doit être ré-actualisé
		'nb_inputs':4												#Nombre de selection possible sur un même fond d'écran [nombre d'entrée du menu]

		}

	def setColorOn(self, txt_color, bg_color):	
	#définit les couleurs du menu lorsqu'il est activé

		assert type(txt_color) is tuple
		assert type(bg_color) is tuple

		self.__menu['txt_color_on']=txt_color
		self.__menu['bg_color_on']=bg_color

	
	def setColorOff(self, txt_color, bg_color):	
	#définit les couleurs du menu lorsqu'il est déactivé

		assert type(txt_color) is tuple
		assert type(bg_color) is tuple

		self.__menu['txt_color_off'] = txt_color
		self.__menu['bg_color_off'] = bg_color
	

	def getMaxInputs(self):				
		#récuprère le nombre d'entrée de menu max dans une fenetre

		return self.__menu['nb_inputs']

	def getCurrentSelection(self):
	#Récupère la sélection courante du menu
		return self.__menu['current_selection']

	def moveUp(self, board):							
		#décale l'entité selectionnée de 1 vers le haut

		if(self.__menu['current_selection']>1): #vérifie le dépassement d'index
			self.__menu['current_selection']-=1
			self.selectMenu(self.__menu['current_selection'], board)

	def moveDown(self, board):							
	#décale l'entité selectionnée de 1 vers le bas

		if(self.__menu['current_selection']<int(self.__menu['nb_inputs'])):  #vérifie le dépassement d'index
			self.__menu['current_selection']+=1	
			self.selectMenu(self.__menu['current_selection'], board)


	def selectMenu(self, choice, board):
	#Selectionne l'entrée du menu choisie

		assert type(choice) is int
	
		if choice<=0: #selection impossible
			return 0
		elif choice>self.__menu['nb_inputs']: #Dépassement de la capacité
			return 0
		else:
			self.__menu['current_selection']=choice
			self.__menu['trigger']=True
		#sauvegarde le choix courant du menu

	def nextSelection(self, board):						
	#décale l'entité selectionnée en faisant une boucle de tout le menu

		self.__menu['current_selection']+=1	
		if self.__menu['current_selection']>self.__menu['nb_inputs']: #Dépassement de la capacité
			self.__menu['current_selection']=1
		self.selectMenu(self.__menu['current_selection'], board)
	

	def display(self, board): 	
	#Permet de selectionner un choix de menu de 1 à x entrée

	#assert type(board) is dict	


		if(self.__menu['last_selection']!=self.__menu['current_selection'] or self.__menu['trigger']==True):
			#chaque menu est comrpis entre deux lignes de #############"
			lines_menu = []

			self.__menu['last_selection']=self.__menu['current_selection']
			self.__menu['trigger']=False

			for index, line in enumerate(board.getBackground()):

				#liste des lignes du menu
				if self.__menu['symbol'] in line:
					lines_menu.append(index)

			lines_menu.append(-1)
			inputs = []		#liste des boutons

			index=0

			while index<(len(lines_menu)-1): #ajoute un élement pour éviter le dépassement

				table=[] #table qui contient les lignes d'un bouton

				#ajout des lignes du 1er bouton
				while lines_menu[index] == int(lines_menu[index+1]-1):
					table.append(lines_menu[index])
					index+=1
				table.append(lines_menu[index])

				#ajout du bouton dans une liste de bouton
				inputs.append(table)
				index+=1 #mise à jour de l'index

			self.__menu['nb_inputs']=len(inputs)
			#remise à zero des boutons
			for a in range(0,self.__menu['nb_inputs']):

				for line in inputs[a]:		#parcourt tous les caractères qui vont changer de couleur

					for index, char in enumerate(board.getBackground()[line]): #pour les lignes concernées par le choix... 

						if char == "#":	#si caractère du menu selectionné

							position_seq = "\033["+str(line+1)+";"+str(index+1)+"H"   # LE PLUS EST IMPORTANT, LE DECALAGE DANS LE TERMINAL EST DE 1
							sys.stdout.write("\033[38;2;"+str(self.__menu['txt_color_off'][0])+";"+str(self.__menu['txt_color_off'][1])+";"+str(self.__menu['txt_color_off'][2])+"m\033[48;2;"+str(self.__menu['bg_color_off'][0])+";"+str(self.__menu['bg_color_off'][1])+";"+str(self.__menu['txt_color_off'][2])+"m"+position_seq+"#"+"\033[0m")	#écriture de la séquence


			#affichage du bouton selectionné
			a=[]
			for line in inputs[self.__menu['current_selection']-1]:		#parcourt tous les caractères qui vont changer de couleur
				#print("ligne "+str(line))

				for index, char in enumerate(board.getBackground()[line]): #pour les lignes concernées par le choix... 

					if char == "#":	#si caractère du menu selectionné

						position_seq = "\033["+str(line+1)+";"+str(index+1)+"H"   # LE PLUS EST IMPORTANT, LE DECALAGE DANS LE TERMINAL EST DE 1
						txt_color_seq="\033[38;2;"+str(self.__menu['txt_color_on'][0])+";"+str(self.__menu['txt_color_on'][1])+";"+str(self.__menu['txt_color_on'][2])+"m"
						bg_color_seq="\033[48;2;"+str(self.__menu['bg_color_on'][0])+";"+str(self.__menu['bg_color_on'][1])+";"+str(self.__menu['bg_color_on'][2])+"m"

						sys.stdout.write(txt_color_seq+bg_color_seq+str(position_seq)+"#")	#écriture de la séquence


			print("")	#PERMET D'AFFICHER LA TOTALITÉ DE LA SELECTION

def enterMenu(menu, keyboard, board):

	print(menu.getCurrentSelection())
	time.sleep(2)
	if(menu.getCurrentSelection() == 1) : 												#Choix de l'histoire du jeu
			board.clear()				#Affiche le menu Story
			keyboard.exit()			

if(__name__ == "__main__"):


	board = Board.Board("menu", 100, 50)
	board.changeBackground("menu.txt", "menu", True)	

	menu = Menu("#")
	menu.setColorOn((0,200,0), (0,00,00))
	menu.setColorOff((255,0,0),(100,0,0))
	menu.selectMenu(1, board)

	menu.display(board)

	keyboard = Keyboard.Keyboard()
	keyboard.addSlot("UP", menu.moveUp, board)
	keyboard.addSlot("ENTER", enterMenu, menu, keyboard, board)
	keyboard.addSlot("TAB", menu.nextSelection, board)				#Permet de changer de selection lors de l'appui de touche TAB
	keyboard.addSlot("DOWN", menu.moveDown, board)		
	#board.progressBar('+', 20, 2,0.1, (10,10), (0,255,10), (0,0,0))
	menu.display(board)

	while(1):
		keyboard.Interact()
		menu.display(board)
		time.sleep(0.01)
		

