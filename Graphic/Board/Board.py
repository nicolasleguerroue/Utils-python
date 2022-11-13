 # *-* encoding:utf-8 *-*
import sys
import os
import time

class Board():

	def __init__(self, name , width , height):

		assert type(name) is str
		assert type(width) is int
		assert type(height) is int

		self.__board={
		'name':name,						#Nom du joueur
		'state':'menu',   					#Par défaut, l'état est menu -> lancement du programme principal
		'width_max':width, 					#Largeur maximal du terminal imposée par le jeu [< à la largeur maximale réelle du terminal]
		'height_max':height, 				#Hauteur maximal du terminal imposée par le jeu [< à la hauteur maximale réelle du terminal]
		'bg':[],							#Liste qui contient toutes les lignes du fond d'écran séléctionné
		'filename':None, 					#Nom du fichier qui contient le fond d'écran actuel

										#liste des symboles stockés pour choisir leur couleur
		'symbols':{	'element':[], 			#liste des symbole choisi
				'txt_color':[], 		#liste des couleurs de texte des symboles [tuple -> (r,g,b) avec r,g et b des entiers]
				'bg_color':[]}, 		#Liste des couleurs de fond des symboles [tuple -> (r,g,b) avec r,g et b des entiers]
										#Exemple : board['symbols']='{'symbols':['#', '+'], 'txt_color':[(120,200,50), (80,90,70)], 'bg_color':[(128,80,0), (8,90,0)]}''

		}#End dict
	
		self.setSize(width, height)	#définit la taille du terminal

	def setSize(self, x,y): 
	#Modifie la taille du terminal

		assert type(x) is int
		assert type(y) is int
		sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=y, cols=x))

	def getSize(self): 
	#Retourne la taille du terminal

		rows, columns = os.popen('stty size', 'r').read().split()
		height = int(rows)
		width = int(columns)
		return int(columns),int(rows)

	def setState(self, state):    
		#definit l'état du jeu

		assert type(state) is str
		self.__board['state']=state

	def getState(self):		
	#renvoie l'état du jeu
		return self.__board['state']


	def addColorElement(self, element, txt_color_rgb, bg_color_rgb) : 
	#définit une couleur pour un élement du fond d'écran: ~ -> bleu
	#txt_color_rgb est un tuple rgb
	#bg_color_rgb est un tuple rgb
	
		assert type(element) is str
		assert type(txt_color_rgb) is tuple
		assert type(bg_color_rgb) is tuple

		self.__board['symbols']['element'].append(element) 				#ajoute l'élement
		self.__board['symbols']['txt_color'].append(txt_color_rgb) 		#ajoute la couleur de police de l'élement
		self.__board['symbols']['bg_color'].append(bg_color_rgb) 		#ajoute la couleur de police de l'élement
 
	def getBackground(self):

		return self.__board["bg"]

	def generateMenu(self, menu, listItem, heightItem=5):

		x = self.__board['width_max']
		y = self.__board['height_max']

		spaceBetweenMenu = y%len(listItem)
		print(spaceBetweenMenu)
		if(y/len(listItem)>heightItem):
			#OK
			pass

		else:
			print("Impossible to generate menu -> try ")



	def changeBackground(self, filename, state, upload):
	#Récupèrele fond d'écran dans un fichier et l'affiche avec les couleurs passées en argument de addColorElement()

		assert type(filename) is str
		assert type(state) is str
		assert type(upload) is bool 	#upload précise si l'affichage doit être pris en compte ou bien on charge juste le fond d'écran dans le dictionniairte sasn l'afficher
		
		#sauvegarde le fond d'écran
		self.__board['filename']=filename
		self.__board['state']=state
		#efface l'écran
		self.clear()
		#vide le fond d'écran précedant
		self.__board['bg']=[]

		file = open(filename, "r")	#ouverture du fichier
		txt = file.read()			#Récupération du texte brut
		file.close() 				#Fermeture du fichier

		#séparation des lignes 
		lines = txt.splitlines()

		for index_l, line in enumerate(lines):    #parcourt chaque ligne

			self.__board['bg'].append(list(line))

			if upload==True:
		
				for index_r, element in enumerate(list(line)):  #parcourt chaque caractère d'une ligne
					# #regarde si on doit colorier le carcatère

					if element in self.__board['symbols']['element']:	#si l'élement à afficher possède une couleur, on l'affiche

						for index_char, char in enumerate(self.__board['symbols']['element']):

				
							if element == self.__board['symbols']['element'][index_char]:   #Couleur associée trouvée

								position_seq = "\033["+str(index_l+1)+";"+str(index_r+1)+"H"   # LE +1 EST IMPORTANT, LE DECALAGE DANS LE TERMINAL EST DE 1

								red = self.__board['symbols']['txt_color'][index_char][0];		#Récupération des couleurs du tuple - foreground
								green= self.__board['symbols']['txt_color'][index_char][1]
								blue = self.__board['symbols']['txt_color'][index_char][2]

								color_seq = "\033[38;2;"+str(red)+";"+str(green)+";"+str(blue)+"m"

								red = self.__board['symbols']['bg_color'][index_char][0];		#Récupération des couleurs du tuple - background
								green= self.__board['symbols']['bg_color'][index_char][1]
								blue = self.__board['symbols']['bg_color'][index_char][2]

								bg_seq = "\033[48;2;"+str(red)+";"+str(green)+";"+str(blue)+"m"	

								sys.stdout.write(position_seq+color_seq+bg_seq+element+"\033[0m")	#écriture de la séquence
						

					else : 							#l'élement ne possède pas de couleur

						position_seq = "\033["+str(index_l+1)+";"+str(index_r+1)+"H"   # LE PLUS EST IMPORTANT, LE DECALAGE DANS LE TERMINAL EST DE 1

						sys.stdout.write("\033[48;2;0;0;0m"+position_seq+element+"\033[0m")	#écriture de la séquence

				else: #On met à jour le fichier seulement
					pass

		print("")
		#affiche la 1ere selection du menu
		return 

	def getPositionChar(self, char):
		#retourne une liste de tuple avec les coordonnées du caractère

		assert type(char) is str

		char_list=[]
		for l in range(0,len(self.__board['bg'])):
			for m in range(0,len(self.__board['bg'][l])):
				if char == self.__board['bg'][l][m]:
					char_list.append([l,m])
		for elem in char_list:
			elem.reverse()
		return char_list  #retourne y,x


	def writeName(self, x,y):	
		#ecrit le nom passé en argument de main à l'emplacement voulu

		assert type(x) is int
		assert type(y) is int	

		position_seq = "\033["+str(x+1)+";"+str(y+1)+"H"   # LE PLUS EST IMPORTANT, LE DECALAGE DANS LE TERMINAL EST DE 1
		sys.stdout.write("\033[48;2;0;0;0m"+position_seq+self.__board['name']+"\033[0m")	#écriture de la séquence

	def write(self,string, x,y, txt_color, bg_color):	
		#écrit un élement à l'emplacement voulu

		assert type(x) is int
		assert type(y) is int	
		assert type(txt_color) is tuple
		assert type(bg_color) is tuple


		txt_color_seq="\033[38;2;"+str(txt_color[0])+";"+str(txt_color[1])+";"+str(txt_color[2])+"m"
		bg_color_seq="\033[48;2;"+str(bg_color[0])+";"+str(bg_color[1])+";"+str(bg_color[2])+"m"
		position_seq = "\033["+str(y+1)+";"+str(x+1)+"H"   # LE PLUS EST IMPORTANT, LE DECALAGE DANS LE TERMINAL EST DE 1
		sys.stdout.write(txt_color_seq+bg_color_seq+position_seq+str(string)+"\033[0m")	#écriture de la séquence


	def blink(self,string, x,y, txt_color, bg_color):	
		#Fait clignoter un élement à l'emplacement voulu

		assert type(x) is int
		assert type(y) is int	
		assert type(txt_color) is tuple
		assert type(bg_color) is tuple

		order="\033[5m"
		txt_color_seq="\033[38;2;"+str(txt_color[0])+";"+str(txt_color[1])+";"+str(txt_color[2])+"m"
		bg_color_seq="\033[48;2;"+str(bg_color[0])+";"+str(bg_color[1])+";"+str(bg_color[2])+"m"
		position_seq = "\033["+str(y+1)+";"+str(x+1)+"H"   # LE PLUS EST IMPORTANT, LE DECALAGE DANS LE TERMINAL EST DE 1
		sys.stdout.write(order+txt_color_seq+bg_color_seq+position_seq+str(string)+"\033[0m")	#écriture de la séquence


	def clear(self): 
	#nettoie le terminal

		sys.stdout.write("\033[0;0H")
		sys.stdout.write("\033[0m")
		sys.stdout.write("\033[2J")
		os.system('clear')


	def progressBar(self, char, length, height,step, position, txt_color, bg_color):
	#Affiche une barre de progression


		assert type(char) is str 			#motif de la barre
		assert type(length) is int  		#nombre de pas
		assert type(height) is int 			#hauteur de la barre de progression	
		assert type(step) is float 			#delai entre chaque pas
		assert type(position) is tuple		#position x y du début de la barre
		assert type(txt_color) is tuple 	#foreground
		assert type(bg_color) is tuple		#background

		for nb_step in range(0,length): #pour chaque symobole à afficher 

			for row in range(0,int(height)):

				x_char = position[0]+nb_step  #X position
				y_char = position[1]+row  #Y position

				position_seq = "\033["+str(y_char)+";"+str(x_char)+"H"
				txt_color_seq="\033[38;2;"+str(txt_color[0])+";"+str(txt_color[1])+";"+str(txt_color[2])+"m"
				bg_color_seq="\033[48;2;"+str(bg_color[0])+";"+str(bg_color[1])+";"+str(bg_color[2])+"m"
				sys.stdout.write(position_seq+txt_color_seq+bg_color_seq+char)
				print("")

			time.sleep(step) #delai entre chaque pas


	def getChar(self, x, y):
	#permet de retourner l'élement en x,y

		assert type(x) is int
		assert type(y) is int

		return self.__board['bg'][y][x]

if __name__ == '__main__':

	board = Board("menu", 100,20)
	#Clear
	board.clear()
	board.setSize(100,30)
	print(board.getSize())
	board.setState("menu")
	print(board.getState())

	a = board.generateMenu(["A", "B"], 5)



	#Write
	#print(board.write("TEST", 20,20, (255,255,255), (40,40,40)))
	
	# board.addColorElement('x', (255,255,0), (100,100,100))
	# board.addColorElement('y', (255,255,0), (100,100,100))
	#board.blink('x', 10,10 , (255,255,255), (200,200,200))
	#board.getPositionChar('x')
	time.sleep(2)
	board.clear()
	
	time.sleep(2)

	board.setSize(120,30)
