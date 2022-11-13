# -*- coding: utf-8 -*-
"""
@project générateur de fichier LTSpice
@author Nicolas LE GUERROUE
@language PYTHON
@lv 3.7
@version 1.0
@presentation La bibliothèque LTSpice permet de générer des fichiers LTSpice en commandes Python.
@presentation L'unité de placement des composants est une valeur entière qui, unitairement, représente le coefficient commun de taille des composants LTSpice
@presentation Ainsi, une résistance par exemple mesure 96*16.
@presentation Lorsque le placement d'un composant est à une distance de 1, cela veut dire que la distance représente 1/6 de celle de la longueur d'une résistance
@presentation Le curseur se déplacant de 16 en 16, cette unité de mesure introduite par la bibliothèque permet de toujours bien placer les composants pour qu'ils soient
@presentation accessibles par le curseur
@class LTSpice
@date 11 juin 2020
"""

import os

class LTSpice():

	"""
	@begin
	@constructor
	@des 
	Le constructeur permet de créer une instance de la classe LTSpice
	@sed
	@input @string Nom du fichier LTSpice à générer (l'extension '.asc' est obligatoire)
	@example ltspice = LTSPice("Fichier_LTSPice.asc")
	@code
	"""

	def __init__(self, filename):

		assert type(filename) is str,str(type(filename))+" got, expected string"

		self.__filename = filename 	#Filename of output LTSpice
		self.__step = 16			#standard step of LTSpice
		#Layout
		self.__nodes = [] 			#Each node has ["name", x%16, y%16, unique]
		self.__wires = [] 			#Each wire has [length%16, orientation%16]

		#Componants
		self.__resistors = [] 		#Each resistor has ["name", x%16, y%16, orientation%90, "value" || value]
		self.__capacitors = [] 		#Each capacitor has ["name", x%16, y%16, orientation%90, "value" || value]
		self.__inductors = [] 		#Each inductor has ["name", x%16, y%16, orientation%90, "value" || value]
		self.__aops = [] 			#..........

		#Current point of cursor
		self.__x = 0
		self.__y = 0

		#Componants size
		self.__resistor_size = 80       #resistor length 
		self.__offset_resistor = 16 	#half width of resistor

		self.__capacitor_size = 64		#capacitor length 
		self.__offset_capacitor = 16 	#half width of capacitor

		self.__inductor_size = 80       #inductor length 
		self.__offset_inductor = 16 	#half width of inductor

		self.__aop_width = 32
		self.__offset_aop_plus = 16

		#Componant orientation
		self.__UP = 180 			
		self.__DOWN = 0
		self.__RIGHT = 270
		self.__LEFT = 90

		self.__direction = {'0':"down", '90':"left", '180':"up", '270':"right"}

		#wires
		self.__last_teta = 0 			#To know the last orientation -> prediction of trajectory to node

		#data
		self.__header = "Version 4 \nSHEET 1 72 1172\n" 		#File header
		self.__stdout = "" 										#Content to print in output file
		self.stderr = " " 									#Data error
		self.__count_warnings = 0 								#Count error

		self.displayErrors = True 							#display data while generating
		self.infos = ""

		#colors
		self.pinkColor = '\033[95m'
		self.blueColor = '\033[94m'
		self.greenColor = '\033[92m'
		self.orangeColor = '\033[93m'
		self.redColor = '\033[91m'
		self.defaultColor = '\033[0m'
		self.bold = '\033[1m'
		self.underline = '\033[4m'

		#OS
		self.__osPath = 'C:\\Program Files\\LTC\\LTspiceXVII\\XVIIx64.exe' #default value on linux using LTSpice with Wine

	"""
	@end
	"""

	"""
	@begin
	@method getX
	@des 
	Cette méthode permet de retourner la position courante en x du curseur dans le fichier.
	@sed
	@range publique
	@type_return @integer
	@return La position du curseur en unité standard (unité=16)
	@example position_x = ltspice.x()
	@code
	"""

	def getX(self):
		return int(self.__x/16)

	"""
	@end
	"""

	"""
	@begin
	@method getY
	@range public
	@des 
	Cette méthode permet de retourner la position courante en y du curseur dans le fichier.
	@sed
	@type_return @integer
	@return La position du curseur en unité standard (unité=16)
	@example position_y = ltspice.y()
	@code
	"""

	def getY(self):
		return int(self.__y/16)

	"""
	@end
	"""

	"""
	@begin
	@method up
	@range public
	@des 
	Cette méthode permet de retourner l'angle de la position "up"
	@sed
	@type_return @integer
	@return L'angle lors du placement "up" des composants
	@example angle_up = ltspice.up()
	@code
	"""
	def up(self):
		return self.__UP

	"""
	@end
	"""

	"""
	@begin
	@method down
	@range public
	@des 
	Cette méthode permet de retourner l'angle de la position "down"
	@sed
	@type_return @integer
	@return L'angle lors du placement "down" des composants
	@example angle_down = ltspice.down()
	@code
	"""

	def down(self):
		return self.__DOWN

	"""
	@end
	"""

	"""
	@begin
	@method right
	@range public
	@des 
	Cette méthode permet de retourner l'angle de la position "right"
	@sed
	@type_return @integer
	@return L'angle lors du placement "right" des composants
	@example angle_right = ltspice.right()
	@code
	"""
	def right(self):
		return self.__RIGHT

	"""
	@end
	"""

	"""
	@begin
	@method left
	@range public
	@des 
	Cette méthode permet de retourner l'angle de la position "left"
	@sed
	@type_return @integer
	@return L'angle lors du placement "left" des composants
	@example angle_left = ltspice.left()
	@code
	"""

	def left(self):
		return self.__LEFT

	"""
	@end
	"""

	"""
	@begin
	@method addNode
	@range public
	@des 
	Cette méthode permet d'ajouter un label dans le schéma. Ce label, placé à un noeud du circuit, permet de revenir sur ce noeud plus tard, pour rajouter une autre branche de circuit.
Lorsque aucune coordonnée n'est donnée, le label se place aux coordonnées courantes.
	@sed
	@input @string Nom du label
	@input @boolean État de vérification : si True, le label devra être unique dans le circuit [defaut=False]
	@input @integer Position du label en x [coordonnées standard de LTSpice]  (argument optionnel)
	@input @integer Position du label en y [coordonnées standard de LTSpice]  (argument optionnel)
	@type_return @boolean
	@return False
	@example ltspice.addNode("Vin", True, 10, 10) #Place un label unique appelé "Vin" en (10,10)
	@code
	"""
	def addNode(self, name="", unique=False, x=-1, y=-1):
		assert type(name) is str,str(type(name))+" got, expected string"
		assert type(unique) is bool,str(type(unique))+" got, expected <bool>"
		assert type(x) is int,str(type(x))+" got, expected integer"
		assert type(y) is int,str(type(y))+" got, expected integer"

		tmp_x = self.__x
		tmp_y = self.__y

		#If data not passed to function
		if(not((x==-1 and y==-1))):
			tmp_x = x*self.__step
			tmp_y = y*self.__step

		#check node
		#A unique node can be generated to read voltage (check node allow to detect error)
		if(unique==True):
			for n in self.__nodes:
				if(name==n[0]):

					self.stderr += "["+self.orangeColor+self.bold+"WARNING"+self.defaultColor+"]>>> Node '"+name+"' already exists. Must be unique in the file.\n "
					self.__count_warnings += 1
		#update nodes
		self.__nodes.append([name, unique, tmp_x,tmp_y] )
		self.__stdout += "FLAG "+str(tmp_x)+" "+str(tmp_y)+" "+name+" \n"

		if(self.displayErrors):
			self.infos += " ["+self.blueColor+ "LAYOUT"+self.defaultColor+"]>>> New node called '"+name+"' \t\t [unique="+str(unique)+", x="+str(tmp_x*self.__step)+", y="+str(tmp_y*self.__step)+"]\n"

		return False


	"""
	@end
	"""

	"""
	@begin
	@method getNode
	@range public
	@des 
	Cette méthode permet de récuperer les informations d'un label
	@sed
	@input @string Nom du label
	@type_return @list
	@return Une liste ["name", checks_state, x, y] si le label est trouvé. Le cas échéant, une liste avec un label vide aux coordonnées d'origine (["", False, 0, 0])
	@example node = ltspice.getNode("Vin") 
	@code
	"""
	def getNode(self, name):

		assert type(name) is str,str(type(name))+" got, expected string"

		for n in self.__nodes:
			if(name==n[0]):
				return n

		return ["", False, 0, 0]
	"""
	@end
	"""
	"""
	@begin
	@method __convertValue
	@range private
	@des 
	Cette méthode permet de convertir une valeur de composant en une valeur exploitable par LTSpice
	@sed
	@input valeur du composant (Integer, Float ou String)
	@type_return @string
	@return La valeur sous forme de chaîne de caractère. Si la valeur en argument n'est pas exploitable, la valeur 'ERROR' est retournée
	@example value = self.__convertValue(145.8) #retourne "146"
	@code
	"""


	def __convertValue(self, value):
		""" Any assert as depending on type
		"""
		tmp_value=0

		if(isinstance(value, int)):

			tmp_value=str(value)

		elif(isinstance(value, float)):

			tmp_value = str(int(value))

		elif(isinstance(value, str)):

			tmp_value=value
		
		else:

			if(self.displayErrors):
				self.stderr += " ["+self.orangeColor + "WARNING"+self.defaultColor+"]>>> Type of componant value is not supported "+str(type(value))+"\n"
				return "ERROR"
		return tmp_value

	"""
	@end
	"""


	"""
	@begin
	@method addResistor
	@range public
	@des 
	Cette méthode permet d'ajouter une résistance dans le circuit. 
Lorsque aucune coordonnée n'est donnée, la résistance se place aux coordonnées courantes.
	@sed
	@input @string Nom de la résistance
	@input @integer Orientation de la résistance [UP, DOWN, RIGHT, LEFT]
	@input Valeur de la résistance en ohms ou sous forme de chaine de caractères [utilisation des préfixes 'k', 'meg', etc]
	@input @integer Position de la résistance en x [coordonnées standard de LTSpice]  (argument optionnel)
	@input @integer Position de la résistance en y [coordonnées standard de LTSpice]  (argument optionnel)
	@type_return @boolean
	@return False
	@example ltspice.addResistor(name="R1", teta=RIGHT, value="47k",x=5, y =12 ) #Place une résistance R1 de 47k Ohms en (5,12)
	@code
	"""

	def addResistor(self, name, teta, value, x=-1, y=-1):

		assert type(name) is str,str(type(name))+" got, expected string"
		assert type(x) is int,str(type(x))+" got, expected integer"
		assert type(y) is int,str(type(y))+" got, expected integer"
		assert type(teta) is int,str(type(teta))+" got, expected integer"
		assert (teta%90)==0,str(type(teta))+" Angle must be 0 or 90"


		value = self.__convertValue(value)  #convert of value

		tmp_x = self.__x
		tmp_y = self.__y
		if(not((x==-1 and y==-1))):
			tmp_x = x*self.__step
			tmp_y = y*self.__step


		#Update cursor
		if(teta==0): #Resistor to bottom
			self.__y+=self.__resistor_size
			#self.__x+=self.__offset_resistor
			tmp_x -=self.__offset_resistor
			tmp_y -=self.__offset_resistor
		if(teta==90):
			self.__x-=self.__resistor_size
			tmp_x += self.__offset_resistor
			tmp_y -= self.__offset_resistor
		if(teta==180): #Resistor to horizontal
			self.__y-=self.__resistor_size
			tmp_x += self.__offset_resistor
			tmp_y += self.__offset_resistor
		if(teta==270):
			self.__x+=self.__resistor_size
			tmp_x -= self.__offset_resistor
			tmp_y += self.__offset_resistor
		#Update resistors
		self.__resistors.append([name,teta, value, tmp_x,tmp_y] )
		self.__stdout += "SYMBOL res "+str(tmp_x)+" "+str(tmp_y)+" R"+str(teta)+"\n"
		self.__stdout += "SYMATTR InstName "+name+"\n"
		self.__stdout += "SYMATTR Value "+value+"\n"

		if(self.displayErrors):
			self.infos += " ["+self.greenColor+ "COMPONENT"+self.defaultColor+"]>>> New resistor called '"+name+"'   \t[x="+str(tmp_x)+", y="+str(tmp_y)+", value="+str(value)+"]\n"
	
		return False


	"""
	@end
	"""



	"""
	@begin
	@method addCapacitor
	@range public
	@des 
	Cette méthode permet d'ajouter un condensateur dans le circuit.
Lorsque aucune coordonnée n'est donnée, le condensateur se place aux coordonnées courantes.
	@sed
	@input @string Nom de la condensateur
	@input @integer Orientation du condensateur [UP, DOWN, RIGHT, LEFT]
	@input Valeur du condensateur en farad ou sous forme de chaine de caractères [utilisation des préfixes 'k', 'meg', etc]
	@input @integer Position du condensateur en x [coordonnées standard de LTSpice]  (argument optionnel)
	@input @integer Position du condensateur en y [coordonnées standard de LTSpice]  (argument optionnel)
	@type_return @boolean
	@return False
	@example ltspice.addCapacitor(name="C1", teta=RIGHT, value="1n",x=5, y =12 ) #Place un condensateur C1 de 1 nF en (5,12)
	@code
	"""

	def addCapacitor(self, name, teta, value, x=-1, y=-1):

		assert type(name) is str,str(type(name))+" got, expected string"
		assert type(x) is int,str(type(x))+" got, expected integer"
		assert type(y) is int,str(type(y))+" got, expected integer"
		assert type(teta) is int,str(type(teta))+" got, expected integer"
		assert type(value) is str,str(type(teta))+" got, expected string"
		assert (teta%90)==0,str(type(teta))+" Angle must be 0 or 90"


		value = self.__convertValue(value)

		tmp_x = self.__x
		tmp_y = self.__y
		if(not((x==-1 and y==-1))):
			tmp_x = x*self.__step
			tmp_y = y*self.__step
	
		#Update cursor
		if(teta==0): #Resistor to bottom
			self.__y+=self.__capacitor_size
			tmp_x -=self.__offset_capacitor
			#tmp_y -=self.__offset_capacitor
		if(teta==90):
			self.__x-=self.__capacitor_size
			tmp_x += self.__offset_capacitor
			tmp_y -= self.__offset_capacitor
		if(teta==180): #Resistor to horizontal

			self.__y-=self.__capacitor_size
			tmp_x += self.__offset_capacitor
			tmp_y += self.__offset_capacitor
		if(teta==270):
			self.__x+=self.__capacitor_size
			tmp_y += self.__offset_capacitor

		#Update capacitor
		self.__capacitors.append([name,teta, value, tmp_x,tmp_y] )
		self.__stdout += "SYMBOL cap "+str(tmp_x)+" "+str(tmp_y)+" R"+str(teta)+"\n"
		self.__stdout += "SYMATTR InstName "+name+"\n"
		self.__stdout += "SYMATTR Value "+str(value)+"\n"

		if(self.displayErrors):
			self.infos += " ["+self.greenColor+ "COMPONENT"+self.defaultColor+"]>>> New capacitor called '"+name+"' \t [x="+str(tmp_x)+", y="+str(tmp_y)+", value="+str(value)+"]\n"

		return False
	"""
	@end
	"""



	"""
	@begin
	@method addInductor
	@range public
	@des 
	Cette méthode permet d'ajouter une inductance dans le circuit.
Lorsque aucune coordonnée n'est donnée, l'inductance se place aux coordonnées courantes.
	@sed
	@input @string Nom de l'inductance
	@input @integer Orientation de l'inductance [UP, DOWN, RIGHT, LEFT]
	@input Valeur de l'inductance en henry ou sous forme de chaine de caractères [utilisation des préfixes 'k', 'meg', etc]
	@input @integer Position de l'inductance en x [coordonnées standard de LTSpice]  (argument optionnel)
	@input @integer Position de l'inductance en y [coordonnées standard de LTSpice]  (argument optionnel)
	@type_return @boolean
	@return False
	@example ltspice.addInductor(name="L1", teta=RIGHT, value="1m",x=5, y =12 ) #Place une inductance L1 de 1m Henry en (5,12)
	@code
	"""

	def addInductor(self, name, teta, value, x=-1, y=-1):

		assert type(name) is str,str(type(name))+" got, expected string"
		assert type(x) is int,str(type(x))+" got, expected integer"
		assert type(y) is int,str(type(y))+" got, expected integer"
		assert type(teta) is int,str(type(teta))+" got, expected integer"
		assert type(value) is str,str(type(teta))+" got, expected string"
		assert (teta%90)==0,str(type(teta))+" Angle must be 0 or 90"

		value = self.__convertValue(value)
		
		tmp_x = self.__x
		tmp_y = self.__y
		if(not((x==-1 and y==-1))):
			tmp_x = x*self.__step
			tmp_y = y*self.__step

		#Update cursor
		if(teta==0): #Resistor to bottom
			self.__y+=self.__inductor_size
			#self.__x+=self.__offset_inductor
			tmp_x -=self.__offset_inductor
			tmp_y -=self.__offset_inductor
		if(teta==90):
			self.__x-=self.__inductor_size
			tmp_x += self.__offset_inductor
			tmp_y -= self.__offset_inductor
		if(teta==180): #Resistor to horizontal
			self.__y-=self.__inductor_size
			tmp_x += self.__offset_inductor
			tmp_y += self.__offset_inductor
		if(teta==270):
			self.__x+=self.__inductor_size
			tmp_x -= self.__offset_inductor
			tmp_y += self.__offset_inductor

		#Update inductor
		self.__resistors.append([name,teta, value, tmp_x,tmp_y] )
		self.__stdout += "SYMBOL ind "+str(tmp_x)+" "+str(tmp_y)+" R"+str(teta)+"\n"
		self.__stdout += "SYMATTR InstName "+name+"\n"
		self.__stdout += "SYMATTR Value "+value+"\n"

		if(self.displayErrors):
			self.infos += " ["+self.greenColor+ "COMPONENT"+self.defaultColor+"]>>> New inductor called '"+name+"' \t [x="+str(tmp_x)+", y="+str(tmp_y)+", value="+str(value)+"]\n"

		return False
	"""
	@end
	"""

	"""
	@begin
	@method addAop
	@range public
	@des 
	Cette méthode permet d'ajouter un amplificateur opérationnel dans le circuit
Lorsque aucune coordonnée n'est donnée, l'AOP se place au coordonnées courante
	@sed
	@input @string Nom de l'AOP
	@input @integer Orientation de l'AOP [UP, DOWN]
	@input @string Entrée courante (Entrée nagative ou positive) de l'AOP [suite de la portion de circuit précédente] 
	@input @string Label d'alimentation positive. Si ce label existe, il viendra alimenter l'AOP
	@input @string Label d'alimentation négative (ou masse). Si ce label existe, il viendra alimenter l'AOP. Le label "0" va créer directement une masse
	@input @string Label de l'entrée opposée (si link="+", le label viendra se rattacher à l'entrée "-") - Si le lable vaut "GND", une masse sera automatiquement reliée
	@input @integer Position de l'Aop en x [coordonnées standard de LTSpice]  (argument optionnel)
	@input @integer Position de l'Aop en y [coordonnées standard de LTSpice]  (argument optionnel)
	@type_return @boolean
	@return False
	@example ltspice.addAop(name="U1", teta=lt.right(), link="+",vcc_label="+VCC", vee_label="GND", other_input="E-", x=5, y =12 ) 
	@code
	"""


	def addAop(self, name, teta, link="+", vcc_label="+VCC", vee_label="-VCC", other_input="E-", x=-1, y=-1):

		assert type(name) is str,str(type(name))+" got, expected string"
		assert type(link) is str,str(type(link))+" got, expected string"
		assert type(vcc_label) is str,str(type(vcc_label))+" got, expected string"   #automatic link to power supply
		assert type(vee_label) is str,str(type(vee_label))+" got, expected string"
		assert type(other_input) is str,str(type(other_input))+" got, expected string"
		assert type(x) is int,str(type(x))+" got, expected integer"
		assert type(y) is int,str(type(y))+" got, expected integer"
		assert type(teta) is int,str(type(teta))+" got, expected integer"

		tmp_teta = teta
		if(teta!=self.__LEFT and teta!=self.__RIGHT):

			print("ERROR")

		tmp_x = self.__x
		tmp_y = self.__y

		if(not((x==-1 and y==-1))):
			tmp_x = x
			tmp_y = y

		miror="R" #or 'M'
		
		#checking ground to supply
		if(vcc_label=="GND"):
			vcc_label="0"
		if (vee_label=="GND"):
			vee_label="0"

	
		#Update cursor
		if(link=="+"):

			if(teta==self.__RIGHT): 
				#print("HERE")
				tmp_x+=self.__aop_width
				tmp_y -=self.__offset_aop_plus
				teta = self.__DOWN

				#seach VCC+
				self.addNode(vcc_label,False, int(tmp_x/self.__step), int((tmp_y-32)/self.__step) )
				#seach VCC-
				self.addNode(vee_label, False, int(tmp_x/self.__step), int((tmp_y+32)/self.__step) )
				#search E-
				if(other_input=="GND" or other_input=="0"):
					self.setCursor( int((tmp_x-2*self.__step)/self.__step), int((tmp_y-self.__step)/self.__step))
					self.addGround(self.left(),2)
				else:
					self.addNode(other_input, False,  int((tmp_x-2*self.__step)/self.__step), int((tmp_y-self.__step)/self.__step))

				#set cursor to output of AOP
				self.setCursor( int((tmp_x+self.__aop_width)/self.__step), int(tmp_y/self.__step))


			if(teta==self.__LEFT):

				tmp_x-=self.__aop_width
				tmp_y-=self.__step
				teta = self.__DOWN
				miror="M"

				#seach VCC+
				self.addNode(vcc_label, False, int(tmp_x/self.__step), int((tmp_y-2*self.__step)/self.__step) )
				#seach VCC-
				self.addNode(vee_label,False, int(tmp_x/self.__step), int((tmp_y+2*self.__step)/self.__step) )
				#search E-
				if(other_input=="GND" or other_input=="0"):
					self.setCursor( int((tmp_x+2*self.__step)/self.__step), int((tmp_y-self.__step)/self.__step))
					self.addGround(self.right(),2)
				else:
					self.addNode(other_input, False,  int((tmp_x+2*self.__step)/self.__step), int((tmp_y-self.__step)/self.__step))

				#set cursor to output of AOP
				self.setCursor( int((tmp_x-2*self.__step)/self.__step), int(tmp_y/self.__step))





			self.__stdout += "SYMBOL Opamps\\UniversalOpamp2 "+str(tmp_x)+" "+str(tmp_y)+" "+miror+str(teta)+"\n"
			self.__stdout += "SYMATTR InstName "+name+"\n"



		elif(link=="-"):


			if(teta==self.__RIGHT): 
				#print("HERE")
				tmp_x+=self.__aop_width
				tmp_y +=self.__offset_aop_plus
				teta = self.__DOWN

				#seach VCC+
				self.addNode(vcc_label,False, int(tmp_x/self.__step), int((tmp_y-32)/self.__step) )
				#seach VCC-
				self.addNode(vee_label, False, int(tmp_x/self.__step), int((tmp_y+32)/self.__step) )
				#search E-
				if(other_input=="GND" or other_input=="0"):
					self.setCursor( int((tmp_x-2*self.__step)/self.__step), int((tmp_y+self.__step)/self.__step))
					self.addGround(self.left(),2)
				else:
					self.addNode(other_input, False,  int((tmp_x-2*self.__step)/self.__step), int((tmp_y+self.__step)/self.__step))

				#set cursor to output of AOP
				self.setCursor( int((tmp_x+self.__aop_width)/self.__step), int((tmp_y)/self.__step))




			if(teta==self.__LEFT):
				tmp_x-=self.__aop_width
				tmp_y+=(self.__step)
				teta = self.__DOWN
				miror="M"

				#seach VCC+
				self.addNode(vcc_label, False, int(tmp_x/self.__step), int((tmp_y-2*self.__step)/self.__step) )
				#seach VCC-
				self.addNode(vee_label,False, int(tmp_x/self.__step), int((tmp_y+2*self.__step)/self.__step) )
				#search E-
				if(other_input=="GND" or other_input=="0"):
					self.setCursor( int((tmp_x+2*self.__step)/self.__step), int((tmp_y+self.__step)/self.__step))
					self.addGround(self.right(),2)
					pass
				else:
					self.addNode(other_input, False,  int((tmp_x+2*self.__step)/self.__step), int((tmp_y-2*self.__step)/self.__step))

				#set cursor to output of AOP
				self.setCursor( int((tmp_x-2*self.__step)/self.__step), int((tmp_y)/self.__step))


			# if(teta==180): #Resistor to horizontal
			# 	tmp_x+=self.__aop_width
			# 	tmp_y -=self.__offset_aop_plus

			self.__stdout += "SYMBOL Opamps\\UniversalOpamp2 "+str(tmp_x)+" "+str(tmp_y)+" "+miror+str(teta)+"\n"
			self.__stdout += "SYMATTR InstName "+name+"\n"

			


		if(self.displayErrors):
			self.infos += " ["+self.greenColor+ "COMPONENT"+self.defaultColor+"]>>> New AOP called '"+name+"' \t[x="+str(tmp_x)+", y="+str(tmp_y)+", orientation="+str(self.__direction[str(tmp_teta)])+"]\n"

		self.__aops.append([name, tmp_x, tmp_y, teta, miror, link])

		return False

	"""
	@end
	"""
	"""
	@begin
	@method addText
	@range public
	@des 
	Cette méthode permet ajouter un commentaire dans le schéma
	@sed
	@input @string Commentaire
	@input @integer Position du texte en x [coordonnées standard de LTSpice]
	@input @integer Position du texte en y [coordonnées standard de LTSpice]
	@type_return @boolean
	@return False
	@example ltspice.addText("This file has been generated by Python", 10, 50)
	@code
	"""
	def addText(self, text, x, y):

		assert type(text) is str,str(type(text))+" got, expected string"
		assert type(x) is int,str(type(x))+" got, expected integer"
		assert type(y) is int,str(type(y))+" got, expected integer"

		self.__stdout += "TEXT "+str(x*self.__step)+" "+str(y*self.__step)+" Left 2 ;"+text+"\n"
		return False

	"""
	@end
	"""

	"""
	@begin
	@method addDirective
	@range public
	@des 
	Cette méthode permet ajouter un ordre de simulation
	@sed
	@input @string Ordre de simulation
	@input @integer Position du condensateur en x [coordonnées standard de LTSpice]
	@input @integer Position du condensateur en y [coordonnées standard de LTSpice]
	@type_return @boolean
	@return False
	@example ltspice.addDirective(".tran 1", 10, 50)
	@code
	"""

	def addDirective(self, order, x, y):

		assert type(order) is str,str(type(order))+" got, expected string"
		assert type(x) is int,str(type(x))+" got, expected integer"
		assert type(y) is int,str(type(y))+" got, expected integer"

		#print(">>> Add new DIRECTIVE at (",x, ",", y,")")
		self.__stdout += "TEXT "+str(x*self.__step)+" "+str(y*self.__step)+" Left 2 "+order+"\n"

	"""
	@end
	"""

	"""
	@begin
	@method drawOrigine
	@range public
	@des 
	Cette méthode permet de dessiner une origine en (0,0) 
	@sed
	@type_return @boolean
	@return False
	@example ltspice.drawOrigine()
	@code
	"""

	def drawOrigine(self):

		self.__stdout += "WIRE -500 0 500 0\n"
		self.__stdout += "WIRE 0 500 0 -500\n"
		return False

	"""
	@end
	"""

	"""
	@begin
	@method setCursorToNode
	@range public
	@des 
	Cette méthode permet de placer le curseur à la position d'un label
	@sed
	@input @list Information d'un label données par la méthode <a href='#getNode' class='water link-animation-water link-hover-water'>getNode</a>
	@type_return @boolean
	@return False
	@example ltspice.setCursorToNode(ltspice.getNode("Vin"))  #Place le curseur au label 'Vin'
	@code
	"""
	def setCursorToNode(self, node):

		assert type(node) is list,str(type(node))+" got, expected list"
		assert len(node)==4," Length of node must be 4 <passed "+len(node)+">"

		self.__x = node[2]
		self.__y = node[3]
		return False

	"""
	@end
	"""

	"""
	@begin
	@method setCursor
	@range public
	@des 
	Cette méthode permet de placer le curseur à la position souhaités
	@sed
	@input @integer Position du curseur en x [coordonnées standard de LTSpice]
	@input @integer Position du curseur en y [coordonnées standard de LTSpice]
	@type_return @boolean
	@return False
	@example ltspice.setCursor(10,10) 		#Place le curseur en (10,10)
	@code
	"""

	def setCursor(self, x, y):

		assert type(x) is int,str(type(x))+" got, expected integer"
		assert type(y) is int,str(type(y))+" got, expected integer"

		self.__x = x*self.__step
		self.__y = y*self.__step

	"""
	@end
	"""

	"""
	@begin
	@method wire
	@range public
	@des 
	Cette méthode permet de dessiner une connexion electrique (fil) depuis la position courante
	@sed
	@input @integer Inclinaison du fil [UP, DOWN, RIGHT, LEFT]
	@input @integer Longueur du fi [coordonnées standard de LTSpice]
	@type_return @boolean
	@return False
	@example ltspice.wire(UP,10)  		#Place un fil allant vers le haut long de 10
	@code
	"""
	def wire(self, teta, length):

		assert type(length) is int,str(type(length))+" got, expected integer"
		assert type(teta) is int,str(type(teta))+" got, expected integer"
		assert (teta%90)==0,str(type(teta))+" Angle must be 0 or 90"

		#print(">>> Add new wire")
		header = "WIRE " + str(self.__x) + " " +str(self.__y) +" " #x+16

		#Update wires
		if(teta==0): #Resistor to horizontal
			self.__wires.append([self.__x, self.__y, self.__x, self.__y+length*self.__step])
			self.__y += length*self.__step
		if(teta==90):
			self.__wires.append([self.__x, self.__y, self.__x-length*self.__step, self.__y])
			self.__x -= length*self.__step
		if(teta==180): #Resistor to horizontal
			self.__wires.append([self.__x, self.__y, self.__x, self.__y-length*self.__step])
			self.__y -= length*self.__step
		if(teta==270):
			self.__wires.append([self.__x, self.__y, self.__x+length*self.__step, self.__y])
			self.__x += length*self.__step

		self.__stdout += header + str(self.__x)+" "+ str(self.__y) + "\n"  #x+16

		#update last_teta
		self.__last_teta = teta

		if(self.displayErrors):
			self.infos += " ["+self.blueColor+ "LAYOUT"+self.defaultColor+"]>>> New wire  \t\t\t\t [length="+str(length)+", direction="+self.__direction[str(teta)] +"]\n"
		return False

	"""
	@end
	"""

	"""
	@begin
	@method wireToNode
	@range public
	@des 
	Cette méthode permet de placer une connexion electrique de la position courante jusqu'à un label
	@sed
	@input @list Information d'un label données par la méthode <a href='#getNode'>getNode()</a>
	@input @integer Type de chemin pris par le fil [1 ou 2]
	@type_return @boolean
	@return False
	@example ltspice.wireToNode(ltspice.getNode("Vin", 1))  #Place le fil jusqu'au label 'Vin' en rpenant le chemin n°1
	@code
	"""

	def wireToNode(self, node, path=1):

		assert type(node) is list,str(type(node))+" got, expected list"
		assert len(node)==4," Length of node must be 4 (passed "+len(node)+")"
		assert type(path) is int,str(type(path))+" got, expected list"

		delta_x = node[2]-self.__x
		delta_y = node[3]-self.__y

		if(self.__last_teta%180==0):
			#if vertical wire

			if(path==1):

				if(delta_x>0):
					self.wire(self.__RIGHT, int(delta_x/self.__step))
				if(delta_x<0):
					self.wire(self.__LEFT, int(-delta_x/self.__step))
				if(delta_x==0):
					pass


				if(delta_y>0):
					self.wire(self.__DOWN, int(delta_y/self.__step))
				if(delta_y<0):
					self.wire(self.__UP, int(-delta_y/self.__step))
				if(delta_y==0):
					pass

			if(path==2):

				if(delta_y>0):
					self.wire(self.__DOWN, int(delta_y/self.__step))
				if(delta_y<0):
					self.wire(self.__UP, int(-delta_y/self.__step))
				if(delta_y==0):
					pass


				if(delta_x>0):
					self.wire(self.__RIGHT, int(delta_x/self.__step))
				if(delta_x<0):
					self.wire(self.__LEFT, int(-delta_x/self.__step))
				if(delta_x==0):
					pass

		else:
			#if horizontal wire

			if(delta_y>0):
				self.wire(self.__DOWN, int(delta_y/self.__step))
			if(delta_y<0):
				self.wire(self.__UP, int(-delta_y/self.__step))
			if(delta_y==0):
				pass


			if(delta_x>0):
				self.wire(self.__RIGHT, int(delta_x/self.__step))
			if(delta_x<0):
				self.wire(self.__LEFT, int(-delta_x/self.__step))
			if(delta_x==0):
				pass

	"""
	@end
	"""

	"""
	@begin
	@method linkGround
	@range public
	@des 
	Cette méthode permet de relier une masse à un laebl donnée
	@sed
	@input @list Information d'un label données par la méthode <a href='#getNode' class='water link-animation-water link-hover-water'>getNode</a>
	@input @integer Orientation du fil de masse [UP, DOWN, RIGHT, LEFT]
	@input @integer Longueur du fil de masse [coordonnées standard de LTSpice]
	@type_return @boolean
	@return False
	@example ltspice.linkGround(ltspice.getNode('Vin'), LEFT, 2)  #Place une masse à deux unités à gauche du label 'Vin'
	@code
	"""
	def linkGround(self, node, teta, length):
		assert type(node) is list,str(type(node))+" got, expected list"
		assert len(node)==4," Length of node must be 4 (passed "+len(node)+""
		assert type(length) is int,str(type(length))+" got, expected integer"
		assert type(teta) is int,str(type(teta))+" got, expected integer"
		#print(">>> Add new ground")
		
		self.setCursor(int(node[2]/self.__step), int(node[3]/self.__step))
		self.wire(teta, length)
		self.addNode("0", False, int(self.__x/self.__step), int(self.__y/self.__step))

	"""
	@end
	"""

	"""
	@begin
	@method addGround
	@range public
	@des 
	Cette méthode permet d'ajouter une masse à la position courante'
	@sed
	@input @integer Orientation de la masse [UP, DOWN, RIGHT, LEFT]
	@input @integer Longueur du fil de masse [coordonnées standard de LTSpice]
	@type_return @boolean
	@return False
	@example ltspice.addGround(LEFT, 2)  #Place une masse à deux unités à gauche du label 'Vin'
	@code
	"""		

	def addGround(self, teta, length):
		""" draw GND from Node
		"""
		assert type(length) is int,str(type(length))+" got, expected integer"
		assert type(teta) is int,str(type(teta))+" got, expected integer"
		#print(">>> Add new ground")

		self.wire(teta, length)
		self.addNode("0", False, int(self.__x/self.__step), int(self.__y/self.__step))
		

	"""
	@end
	"""

	"""
	@begin
	@method addWaveFileInput
	@range public
	@des 
	Cette méthode permet d'ajouter un signal en provenance d'un fichier WAV
	@sed
	@input @string Nom du fichier WAV
	@input @string Nom du label associé (pour récuperer le signal dans le circuit)
	@input @integer Position du curseur en x [coordonnées standard de LTSpice] (facultatif)
	@input @integer Position du curseur en y [coordonnées standard de LTSpice] (facultatif)
	@type_return @boolean
	@return False
	@example ltspice.addWaveFileInput("input.wav", "input_wave", -5, -2) 
	@code
	"""		

	def addWaveFileInput(self, filename, name="V_WAVE", x=-1, y=-1):

		assert type(filename) is str,str(type(filename))+" got, expected string"
		assert type(name) is str,str(type(name))+" got, expected string"
		assert type(x) is int,str(type(x))+" got, expected integer"
		assert type(y) is int,str(type(y))+" got, expected integer"

		tmp_x = self.__x
		tmp_y = self.__y

		if(not((x==-1 and y==-1))):
			tmp_x = x*self.__step
			tmp_y = y*self.__step

		self.__stdout += "SYMBOL voltage "+str(tmp_x)+" "+str(tmp_y)+" R0 \n"
		self.__stdout += "WINDOW 123 24 44 Left 2\n"
		self.__stdout += "WINDOW 39 0 0 Left 2\n"
		self.__stdout += "SYMATTR Value2 wavefile=\""+filename+"\"\n"
		self.__stdout += "SYMATTR InstName "+name+"\n"
		self.__stdout += "SYMATTR Value \"\"\n"

		self.setCursor(int(tmp_x/self.__step), int((tmp_y+16)/self.__step))
		self.addNode(name)
		self.setCursor(int(tmp_x/self.__step), int((tmp_y+96)/self.__step))
		self.wire(self.down(), 1)
		self.addGround(self.down(), 2)

		return False


	"""
	@end
	"""

	"""
	@begin
	@method addDoubleSupply
	@range public
	@des 
	Cette méthode permet d'ajouter un alimentation double (symétrique ou non)
	@sed
	@input @float Tension d'alimentation positive
	@input @float Tension d'alimentation négative
	@input @string liste des labels d'alimentation (default=["+VCC","-VCC"])	
	@input @integer Position de l'alimentation en x [coordonnées standard de LTSpice] (facultatif)
	@input @integer Position de l'alimentation en y [coordonnées standard de LTSpice] (facultatif)
	@type_return @boolean
	@return False
	@example ltspice.addDoubleSupply(vcc=15.0, vee=15, name=['+VCC', "-VCC"], x=20, y=30) 
	@code
	"""		

	def addDoubleSupply(self, vcc, vee, name=["+VCC","-VCC"], x=-1, y=-1):

		assert type(vcc) is float,str(type(vcc))+" got, expected <float>"
		assert type(vee) is float,str(type(vee))+" got, expected <float>"
		assert type(name) is list,str(type(name))+" got, expected list"
		assert type(x) is int,str(type(x))+" got, expected integer"
		assert type(y) is int,str(type(y))+" got, expected integer"

		tmp_x = self.__x
		tmp_y = self.__y
		if(not((x==-1 and y==-1))):
			tmp_x = x*self.__step
			tmp_y = y*self.__step

		#create +VCC
		self.__stdout += "SYMBOL voltage "+str(tmp_x)+" "+str(tmp_y)+" R0 \n"
		self.__stdout += "WINDOW 123 24 44 Left 2\n"
		self.__stdout += "WINDOW 39 0 0 Left 2\n"
		self.__stdout += "SYMATTR InstName "+name[0]+"\n"
		self.__stdout += "SYMATTR Value "+str(vcc)+"\n"

		self.setCursor(int(tmp_x/self.__step), int((tmp_y+16)/self.__step))
		self.addNode(name[0])
		self.setCursor(int(tmp_x/self.__step), int((tmp_y+96)/self.__step))
		self.wire(self.down(), 1)
		self.addNode("gpower")
		self.linkGround(self.getNode("gpower"), self.left(), 2)


		self.setCursorToNode(self.getNode("gpower"))
		#create -VCC
		self.__stdout += "SYMBOL voltage "+str(self.__x)+" "+str(self.__y)+" R0 \n"
		self.__stdout += "WINDOW 123 24 44 Left 2\n"
		self.__stdout += "WINDOW 39 0 0 Left 2\n"
		self.__stdout += "SYMATTR InstName "+name[1]+"\n"
		self.__stdout += "SYMATTR Value "+str(vee)+"\n"

		self.setCursorToNode(self.getNode("gpower"))
		self.wire(self.down(), 1)
		self.setCursor(int(self.__x/self.__step), int((self.__y+80)/self.__step))
		self.addNode(name[1])
		
		
		return False

	"""
	@end
	"""


	"""
	@begin
	@method displayInfos
	@range public
	@des 
	Cette méthode permet de définir si la création du schéma doit être détaillé pendant la génération
	@sed
	@input @boolean Etat de l'affichage
	@type_return @boolean
	@return False
	@example ltspice.displayInfos(True)
	@code
	"""	
	def displayInfos(self, state):

		assert type(state) is bool,str(type(state))+" got, expected <bool>"

		self.displayErrors = state
		return False

	"""
	@end
	"""

	"""
	@begin
	@method exportFile
	@range public
	@des 
	Cette méthode permet de générer le fichier de sortie
	@sed
	@type_return @boolean
	@return False en cas de succès, True en cas d'erreur
	@example ltspice.displayInfos(True)
	@code
	"""	
	def exportFile(self):
		""" Generate .ac file
		"""
		try:
			tmp_file = open(self.__filename, "w")
			tmp_file.write(self.__header+self.__stdout)
			tmp_file.close()
		except Exception as e:
			print("impossible to write into file called '", self.__filename, "' ")
			print("Error : ", e)
			return True
		print(self.infos)

	
		#display warning
		print(self.stderr)
		print(" ["+self.orangeColor+ "WARNING"+self.defaultColor+"]>>> "+str(self.__count_warnings)+" warning(s)\n")
		print(" >>> "+self.greenColor+self.bold+ " File '"+self.__filename+"'  has been generated "+self.defaultColor+"\n")
		return False

	"""
	@end
	"""

	"""
	@begin
	@method setSourcePath
	@range public
	@des 
	Cette méthode setSourcePath permet de défnir l'emplacement de l'éxécutable LTSpice. Il varie selon le système d'exploitation
	@sed
	@type_return @boolean
	@return False
	@example ltspice.setSourcePath("path")
	@code
	"""	
	def setSourcePath(self, path):
		
		assert type(path) is bool,str(type(path))+" got, expected <string>"

		self.__osPath = path
		return False

	"""
	@end
	"""

	"""
	@begin
	@method run
	@range public
	@des 
	Cette méthode run permet de lancer la simulation en mode Batch
	@sed
	@type_return @boolean
	@return False en cas de succès, True en cas d'erreur
	@example ltspice.run()
	@code
	"""	
	def run(self):
		""" run .acs file
		"""
		print(" >>> "+self.greenColor+self.bold+ " Running '"+self.__filename+"' simulation..."+self.defaultColor)
		try:
			os.system("wine '"+self.__osPath+"' "+self.__filename+" -Run -ascii -b 2> log_ltspice_run.txt")

			#os.system("wine '"+self.__osPath+"' "+self.__filename+" -Run -b 2> log_ltspice_run.txt")

		except Exception as e:
			print("impossible to run file called '", self.__filename, "' ")
			print("Error : ", e)
			return True
		#display warning
		print(" >>> "+self.greenColor+self.bold+" Simulation is over"+self.defaultColor+"\n")
		return False

	"""
	@end
	"""
def main():


	"""
	@begin
	@method Code de démonstration
	@range public
	@des 
	Voici le code d'exemple associé à la bibliothèque
	@sed
	@type_return @none
	@return False
	@example lt = LTSpice("Project.asc")<br>lt.displayInfos(True)<br>lt.setCursor(0, 0)<br>lt.addNode("V_wave", True, lt.getX(), lt.getY())<br>lt.wire(RIGHT, 2)<br>lt.addResistor("R1", RIGHT,"1000")<br>lt.wire(RIGHT, 2)<br>lt.addNode("N1")<br>lt.wire(RIGHT, 2)<br>lt.addCapacitor("C1", RIGHT, "1000")<br>lt.wire(RIGHT, 2)<br>lt.addNode("N2")<br>lt.wire(DOWN, 2)<br>lt.addResistor("R3", DOWN, "1000")<br>lt.wire(DOWN, 2)<br>lt.addGround(DOWN, 2)<br>lt.setCursorToNode(lt.getNode("N2"))<br>lt.wire(RIGHT, 2)<br>lt.addAop(name="A1", teta=DOWN, miror=0, link="+", vcc_label="+VCC", vee_label="-VCC", negative_label="E1")<br>lt.wire(lt.right(), 2)<br>lt.addNode("Vs")<br>lt.setCursorToNode(lt.getNode("E1"))<br>lt.addGround(LEFT, 2)<br>lt.addText("This file has been automatically generated", -10,25)<br>lt.addDirective(".tran 11", -10, 5)<br>lt.addWaveFileInput(filename="son.wav", name="V_wave", x=-10, y=15)<br>lt.addDoubleSupply(vcc=15.0, vee=15.0, name=["+VCC", "-VCC"], x=-10, y=30)<br>lt.exportFile()
	@code
	"""		

	lt = LTSpice("Project.asc")
	lt.displayInfos(True) 				#Allow to display info on generation file

	lt.setCursor(0, 0) 									#Center of table drawing
	lt.addNode("V_wave", True, lt.getX(), lt.getY())			#create first Sallen key
	lt.wire(lt.right(), 2)
	lt.addResistor("R1",lt.right(),"1000")
	lt.wire(lt.right(), 2)
	lt.addNode("N1")
	lt.wire(lt.right(), 2)
	lt.addCapacitor("C1",lt.right(), "1000")
	lt.wire(lt.right(), 2)
	lt.addNode("N2")
	lt.wire(lt.down(), 2)
	lt.addResistor("R3", lt.down(), "1000")
	lt.wire(lt.down(), 2)
	lt.addGround(lt.down(), 2)
	lt.setCursorToNode(lt.getNode("N2"))
	lt.wire(lt.right(), 2)
	# lt.addAop(name="A1", teta=lt.left(), link="-", vcc_label="+VCC", vee_label="GND", other_input="0")
	# lt.addNode("Vs")
	# lt.setCursorToNode(lt.getNode("E1"))
	# lt.addGround(lt.left(), 2)

	lt.addText("This file has been automatically generated", -10,25)
	lt.addDirective(".tran 11", -10, 5)
	lt.addWaveFileInput(filename="son.wav", name="V_wave", x=-10, y=15)
	lt.addDoubleSupply(vcc=15.0, vee=15.0, name=["+VCC", "-VCC"], x=-10, y=30)


	lt.exportFile()

	return False

	"""
	@end
	"""

if __name__ == '__main__':
	main()



