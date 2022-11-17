# *-* encoding:utf-8 *-*
import sys
import select
import tty 
import termios
import time
from sympy import true


#Fonctions permettant de tester le passage d'argument à travers le module Keyboard.
def test1(var1):
	print(var1)

def test2(var1, var2):
	print(str(var1)+str(var2))

def test3(var1, var2, var3):
	print(str(var1)+str(var2)+str(var3))

class Keyboard():
	
	def __init__(self):
		pass

		settings = termios.tcgetattr(sys.stdin)
		tty.setcbreak(sys.stdin.fileno())
		self.__alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"] #liste des touches classiques
		self.__keyboard={'alpha':self.__alpha, 'keys':[], 'functions':{'name':[],'arg1':[],'arg2':[], 'arg3':[], 'arg4':[]}, 'settings':settings}
		#settings est une variable qui va servir à quitter le terminal

	def updateArgument(self, touch, arg_index, new_arg):   
	#met à jour un argument des combinaisons touches / fonction -> numération classique (1 à x)
	#on spécifie le clavier, la touche et le numéro de l'argument, enfin on donne l'arguement mis à jour
		assert type(touch) is str
		assert type(arg_index) is int
	
		index = self.__keyboard['keys'].index(touch)

		if arg_index==1:
			self.__keyboard['functions']['arg1'][index]=new_arg
		if arg_index==2:
			self.__keyboard['functions']['arg2'][index]=new_arg
		if arg_index==3:
			self.__keyboard['functions']['arg3'][index]=new_arg
		if arg_index==4:
			self.__keyboard['functions']['arg4'][index]=new_arg

	def exit(self):
	#Quitte le programme


		print("Interruption du programme")
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.__keyboard['settings'])
		sys.exit()


	def receiveData(self): 
	#retourne True si appui sur une touche

		if (select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])):
			return True
		else:
			return False

	def getKey(self):
	#Récupère la touche pressée

		c = sys.stdin.read(1) #lit le 1er caractère
	
		for char in self.__keyboard['alpha']: #parcourt le tableau de caractère

			if c == char:
				return char

		if c==" ":
			return "SPACE"

		if c=="\n":
			return "ENTER"

		if c=="\t":				#tabulation
			return "TAB"

		c2 = sys.stdin.read(1)	#Lecture d'un 2ème caractère

		if c=='\x1b' and c2=="[": #Si on appuie sur un autre bouton que echap

			c = sys.stdin.read(1) #lit le caractère de direction
			termios.tcflush(sys.stdin.fileno(),termios.TCIFLUSH)

			if c == "A":
				return "UP"
			elif c == "B":
				return "DOWN"
			elif c == "C":
				return "RIGHT"
			elif c == "D":
				return "LEFT"

		else:
			termios.tcflush(sys.stdin.fileno(),termios.TCIFLUSH) #Vide le buffer
			return c	

	def waitingKey(self, key = None):
	#Attend qu'un utilisateur ait pressé une touch
		while True:
			if(self.receiveData()):
				c = self.getKey()
				if(key != None):
					if(c == key):
						termios.tcflush(sys.stdin.fileno(),termios.TCIFLUSH) #Vide le buffer
						return c
				else:
					termios.tcflush(sys.stdin.fileno(),termios.TCIFLUSH) #Vide le buffer
					return c

		return None


	def addSlot(self, key, function, arg1=None, arg2=None, arg3=None, arg4=None):
	#Associe une touche et une fonction ayant au maximaum 4 argument
		assert type(key) is str

		self.__keyboard['keys'].append(key)						#ajoute la clé -> touche du clavier
		self.__keyboard['functions']['name'].append(function)
		self.__keyboard['functions']['arg1'].append(arg1)
		self.__keyboard['functions']['arg2'].append(arg2)
		self.__keyboard['functions']['arg3'].append(arg3)
		self.__keyboard['functions']['arg4'].append(arg4)

	def Interact(self):
	#Lecture des évenements

		if(self.receiveData()):

			char = self.getKey() 
			nb_arg=0
			for slots in range(0,len(self.__keyboard['keys'])): #pour chaque carcatère, slot est un int

				if self.__keyboard['keys'][slots]==char: #Si caractère correspondant

					#recupere nombre argument
						if self.__keyboard['functions']['arg1'][slots]!=None:  #Au moins 1 arg
							nb_arg+=1
							if self.__keyboard['functions']['arg2'][slots]!=None:  #Au moins 1 arg
								nb_arg+=1
								if self.__keyboard['functions']['arg3'][slots]!=None:  #Au moins 1 arg
									nb_arg+=1
									if self.__keyboard['functions']['arg4'][slots]!=None:  #Au moins 1 arg
										nb_arg+=1

						if nb_arg==0:  #appel sans argument
							self.__keyboard['functions']['name'][slots] ()

						if nb_arg==1: #appel avec 1 arg
							self.__keyboard['functions']['name'][slots] (self.__keyboard['functions']['arg1'][slots])

						if nb_arg==2: #appel avec 2 arg
							self.__keyboard['functions']['name'][slots] (self.__keyboard['functions']['arg1'][slots], self.__keyboard['functions']['arg2'][slots])

						if nb_arg==3: #appel avec 3 arg
							self.__keyboard['functions']['name'][slots] (self.__keyboard['functions']['arg1'][slots], self.__keyboard['functions']['arg2'][slots], self.__keyboard['functions']['arg3'][slots])

						if nb_arg==4: #appel avec 4 arg
							self.__keyboard['functions']['name'][slots] (self.__keyboard['functions']['arg1'][slots], self.__keyboard['functions']['arg2'][slots], self.__keyboard['functions']['arg3'][slots], self.__keyboard['functions']['arg4'][slots])		


	def openCVInteract(self, key):
	#Lecture des évenements

		if(key!=255 and key!=None):

			nb_arg=0
			for slots in range(0,len(self.__keyboard['keys'])): #pour chaque caractère, slot est un int

				if(self.__keyboard['keys'][slots])==chr(key): #Si caractère correspondant
					#recupere nombre argument
					if self.__keyboard['functions']['arg1'][slots]!=None:  #Au moins 1 arg
						nb_arg+=1
						if self.__keyboard['functions']['arg2'][slots]!=None:  #Au moins 1 arg
							nb_arg+=1
							if self.__keyboard['functions']['arg3'][slots]!=None:  #Au moins 1 arg
								nb_arg+=1
								if self.__keyboard['functions']['arg4'][slots]!=None:  #Au moins 1 arg
									nb_arg+=1

						if nb_arg==0:  #appel sans argument
							self.__keyboard['functions']['name'][slots] ()

						if nb_arg==1: #appel avec 1 arg
							self.__keyboard['functions']['name'][slots] (self.__keyboard['functions']['arg1'][slots])

						if nb_arg==2: #appel avec 2 arg
							self.__keyboard['functions']['name'][slots] (self.__keyboard['functions']['arg1'][slots], self.__keyboard['functions']['arg2'][slots])

						if nb_arg==3: #appel avec 3 arg
							self.__keyboard['functions']['name'][slots] (self.__keyboard['functions']['arg1'][slots], self.__keyboard['functions']['arg2'][slots], self.__keyboard['functions']['arg3'][slots])

						if nb_arg==4: #appel avec 4 arg
							self.__keyboard['functions']['name'][slots] (self.__keyboard['functions']['arg1'][slots], self.__keyboard['functions']['arg2'][slots], self.__keyboard['functions']['arg3'][slots], self.__keyboard['functions']['arg4'][slots])		




if(__name__ == '__main__'):   #Jeux de tests
	
	keyboard = Keyboard()
	keyboard.addSlot("a", test1, "test avec un argument")
	keyboard.addSlot("z", test2, "test", " avec 2 arguments")
	keyboard.addSlot("e", test3, "test", " avec ", " 3 arguments")
	print("Veuillez cliquez sur la touche 'a', 'z' ou 'e'")

	
	while 1:

		keyboard.Interact()
		print(keyboard.getKey())

		
