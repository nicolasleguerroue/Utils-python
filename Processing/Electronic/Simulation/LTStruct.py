# -*- coding: utf-8 -*-
"""
@project générateur de fichier LTSpice avec implémentation de structures
@author Nicolas LE GUERROUE
@language PYTHON
@lv 3.7
@version 1.0
@presentation La bibliothèque LTSstruct permet de générer des fichiers LTSpice en commandes Python mais également de mettre en place des structures prédéfinies.
@presentation L'unité de placement des composants est une valeur entière qui, unitairement, représente le coefficient commun de taille des composants LTSpice
@presentation Ainsi, une résistance par exemple mesure 96*16.
@presentation Lorsque le placement d'un composant est à une distance de 1, cela veut dire que la distance représente 1/6 de celle de la longueur d'une résistance
@presentation Le curseur se déplacant de 16 en 16, cette unité de mesure introduite par la bibliothèque permet de toujours bien placer les composants pour qu'ils soient
@presentation accessibles par le curseur
@class LTSpice
@date 11 juin 2020
@parent LTSpice.py
"""

from LTSpice import LTSpice

class LTStruct(LTSpice):

	"""
	@begin
	@constructor
	@des 
	Le constructeur permet de créer une instance de la classe LTStruct
	@sed
	@input @string Nom du fichier LTSpice à générer (l'extension '.asc' est obligatoire)
	@example ltspice = LTStruct("Fichier_LTSPice.asc")
	@code
	"""
	def __init__(self, filename):

		super().__init__(filename)

		self.__automaticExtend = False 			#Allow to extend each cell to take all space needed

		self.__count_voltageDivider = 1
		self.__count_passiveHighPass = 1
		self.__count_passiveLowPass = 1
		self.__count_invertingAOP = 1
		self.__count_nonInvertingAOP = 1

	"""
	@end
	"""

	"""
	@begin
	@method setAutomaticExtend
	@des 
	Cette méthode permet de cascader les structures automatiquement pour éviter qu'elles dépassent les anciennes
	@sed
	@range publique
	@input @boolean Etat de l'extension
	@type_return @boolean
	@return La nouvelle valeur de l'état
	@example ltspice.setAutomaticExtend(True)
	@code
	"""
	def setAutomaticExtend(self, state):

		self.__automaticExtend = state
		return self.__automaticExtend

	"""
	@end
	"""

	
	"""
	@begin
	@method voltageDivider
	@des 
	Cette méthode permet de générer un pont diviseur avec deux résistances en série
	@sed
	@range publique
	@input @string Label d'entrée
	@input @string Label de sortie
	@input @float Valeur de la résistance supérieure 
	@input @float Valeur de la résistance inférieure 
	@input @int Direction du placement 
	@type_return @boolean
	@return False en cas de succès
	@example ltspice.voltageDivider("ve", "vs",  1000, 1200, ltspice.right())
	@code
	"""
	def voltageDivider(self, ve, vs, r1, r2, teta):

		assert type(ve) is str,str(type(ve))+" got, expected string"
		assert type(vs) is str,str(type(vs))+" got, expected string"
		assert type(teta) is int,str(type(teta))+" got, expected int"

		if(teta==self.right()):

			self.addNode(ve, False, self.getX(), self.getY())
			self.wire(self.right(), 2)
			self.addResistor("Rvd1_"+str(self.__count_voltageDivider),self.right(),r1)
			self.wire(self.right(), 2)
			self.addNode(vs)
			self.wire(self.down(), 2)
			self.addResistor("Rvd2_"+str(self.__count_voltageDivider), self.down(), r2)
			self.wire(self.down(), 2)
			self.addGround(self.down(), 2)
			self.setCursorToNode(self.getNode(vs))
			self.__count_voltageDivider +=1

		elif(teta==self.left()):

			self.addNode(ve, False, self.getX(), self.getY())
			self.wire(self.left(), 2)
			self.addResistor("Rvd1_"+str(self.__count_voltageDivider),self.left(),r1)
			self.wire(self.left(), 5)
			self.addNode(vs)
			self.wire(self.down(), 3)
			self.addResistor("Rvd2_"+str(self.__count_voltageDivider), self.down(), r2)
			self.wire(self.down(), 2)
			self.addGround(self.down(), 1)
			self.setCursorToNode(self.getNode(vs))
			self.__count_voltageDivider +=1

		else:
			print("ERROR")


		if(self.displayErrors):
			self.infos += " ["+self.pinkColor+ "STRUCT"+self.defaultColor+"]>>> New struct 'voltageDivider'\n"

	"""
	@end
	"""

	"""
	@begin
	@method passiveHighPass
	@des 
	Cette méthode permet de générer un filtre passe-haut d'ordre 1 consitué d'un condensateur et d'une résistance en série
	@sed
	@range publique
	@input @string Label d'entrée
	@input @string Label de sortie
	@input @float Valeur du condensateur 
	@input @float Valeur de la résistance 
	@type_return @boolean
	@return False en cas de succès
	@example ltspice.passiveHighPass("ve", "vs", 1000 1200)
	@code
	"""
	def passiveHighPass(self, ve, vs, c1, r1):

		assert type(ve) is str,str(type(ve))+" got, expected string"
		assert type(vs) is str,str(type(vs))+" got, expected string"


		self.addNode(ve, False, self.getX(), self.getY())#create first Sallen key
		self.wire(self.right(), 2)
		self.addCapacitor("Chp_"+str(self.__count_passiveHighPass),self.right(),c1)
		self.wire(self.right(), 2)
		self.addNode(vs)
		self.wire(self.down(), 2)
		self.addResistor("Rhp_"+str(self.__count_passiveHighPass), self.down(),r1)
		self.wire(self.down(), 2)
		self.addGround(self.down(), 2)
		self.setCursorToNode(self.getNode(vs))
		self.__count_passiveHighPass += 1


		if(self.displayErrors):
			self.infos += " ["+self.pinkColor+ "STRUCT"+self.defaultColor+"]>>> New struct 'passiveHighPass'\n"

	"""
	@end
	"""


	"""
	@begin
	@method passiveLowPass
	@des 
	Cette méthode permet de générer un filtre passe-bas d'ordre 1 consitué d'une résistance et d'un condensateur en série
	@sed
	@range publique
	@input @string Label d'entrée
	@input @string Label de sortie
	@input @float Valeur de la résistance 
	@input @float Valeur du condensateur 
	@type_return @boolean
	@return False en cas de succès
	@example ltspice.passiveLowPass("ve", "vs", 1000, 1, 1e-9)
	@code
	"""
	def passiveLowPass(self, ve, vs, c1, r1):



		self.addNode(ve, False, self.getX(), self.getY())#create first Sallen key
		self.wire(self.right(), 2)
		self.addResistor("Rlp_"+str(self.__count_passiveLowPass), self.right(), str(r1))
		self.wire(self.right(), 2)
		self.addNode(vs)
		self.wire(self.down(), 2)
		self.addCapacitor("Clp_"+str(self.__count_passiveLowPass),self.down(),str(c1))
		self.wire(self.down(), 3)
		self.addGround(self.down(), 2)
		self.setCursorToNode(self.getNode(vs))

	"""
	@end
	"""


	"""
	@begin
	@method invertingAop
	@des 
	Cette méthode permet de générer un montage à AOP inverseur
	@sed
	@range publique
	@input @string Label d'entrée
	@input @string Label de sortie
	@input @string Label d'alimentation positive
	@input @string Label d'alimentation négative (ou masse)
	@input @float Valeur de la résistance R1
	@input @float Valeur de la résistance R2 (contre-réaction)
	@type_return @boolean
	@return False en cas de succès
	@example ltspice.invertingAop("+VCC", "-VCC", 1000, 1000)
	@code
	"""
	def invertingAop(self, vcc, vee, r1, r2):



		self.addResistor("R1_inv_"+str(self.__count_invertingAOP), self.right(), str(r1))
		self.wire(self.right(),2)
		self.addNode("E-_"+str(self.__count_invertingAOP))
		self.wire(self.right(),2)
		self.addAop(name="U_inv_"+str(self.__count_invertingAOP), teta=self.down(), miror=0, link="-",vcc_label=vcc, vee_label=vee, other_input="GND") #AOp right, signal on -
		self.wire(self.right(), 3)
		self.wire(self.up(),1)
		self.addNode("Vs_inv_"+str(self.__count_invertingAOP))
		self.wire(self.up(), 11)
		self.wire(self.left(), 2)
		self.addResistor("R2_inv_"+str(self.__count_invertingAOP), self.left(), str(r2))
		self.wire(self.left(), 2)
		self.wireToNode(self.getNode("E-_"+str(self.__count_invertingAOP)))
		self.setCursorToNode(self.getNode("E+_0_"+str(self.__count_invertingAOP)))
		self.wire(self.left(),2)
		self.addGround(self.down(), 2)

		self.setCursorToNode(self.getNode("Vs_inv_"+str(self.__count_invertingAOP)))

		self.__count_invertingAOP +=1


	"""
	@end
	"""



	"""
	@begin
	@method nonInvertingAop
	@des 
	Cette méthode permet de générer un montage à AOP non-inverseur
	@sed
	@range publique
	@input @string Label d'entrée
	@input @string Label de sortie
	@input @string Label d'alimentation positive
	@input @string Label d'alimentation négative (ou masse)
	@input @float Valeur de la résistance R1
	@input @float Valeur de la résistance R2 (contre-réaction)
	@type_return @boolean
	@return False en cas de succès
	@example ltspice.nonInvertingAop("+VCC", "-VCC", 1000, 1000)
	@code
	"""
	def nonInvertingAop(self, vcc, vee, r1, r2):



		self.addAop(name="U_ninv_"+str(self.__count_nonInvertingAOP), teta=self.up(), miror=1, link="+",vcc_label=vcc, vee_label=vee, other_input="E_inv_"+str(self.__count_nonInvertingAOP)) #AOp right, signal on -
		self.wire(self.right(), 2)
		self.addNode("Vs_ninv_"+str(self.__count_nonInvertingAOP))
		self.wire(self.down(), 6)
		self.wire(self.left(), 1)
		self.addResistor("R2_ninv_"+str(self.__count_nonInvertingAOP), self.left(), str(r2))
		self.wire(self.left(),1)
		self.addNode("N_ninv_"+str(self.__count_nonInvertingAOP))
		self.wireToNode(self.getNode("E_inv_"+str(self.__count_nonInvertingAOP)))
		self.setCursorToNode(self.getNode("N_ninv_"+str(self.__count_nonInvertingAOP)))
		self.wire(self.left(),6)
		self.wire(self.down(),1)
		self.addResistor("R1_ninv_"+str(self.__count_nonInvertingAOP), self.down(), str(r1))
		self.addGround(self.down(),2)

		self.setCursorToNode(self.getNode("Vs_ninv_"+str(self.__count_nonInvertingAOP)))

		self.__count_nonInvertingAOP +=1


	"""
	@end
	"""



	"""
	@begin
	@method integrating
	@des 
	Cette méthode permet de générer un montage à AOP intégrateur
	@sed
	@range publique
	@input @string Label d'entrée
	@input @string Label de sortie
	@input @string Label d'alimentation positive
	@input @string Label d'alimentation négative (ou masse)
	@input @float Valeur de la résistance R1
	@input @float Valeur de la résistance R2 (contre-réaction)
	@type_return @boolean
	@return False en cas de succès
	@example ltspice.integrating("+VCC", "-VCC", 1000, 1000)
	@code
	"""
	def integrating(self, vcc, vee, r1, r2, c1):



		self.addAop(name="U_ninv_"+str(self.__count_nonInvertingAOP), teta=self.up(), miror=1, link="+",vcc_label=vcc, vee_label=vee, other_input="E_inv_"+str(self.__count_nonInvertingAOP)) #AOp right, signal on -
		self.wire(self.right(), 2)
		self.addNode("Vs_ninv_"+str(self.__count_nonInvertingAOP))
		self.wire(self.down(), 6)
		self.wire(self.left(), 1)
		self.addResistor("R2_ninv_"+str(self.__count_nonInvertingAOP), self.left(), str(r2))
		self.wire(self.left(),1)
		self.addNode("N_ninv_"+str(self.__count_nonInvertingAOP))
		self.wireToNode(self.getNode("E_inv_"+str(self.__count_nonInvertingAOP)))
		self.setCursorToNode(self.getNode("N_ninv_"+str(self.__count_nonInvertingAOP)))
		self.wire(self.left(),6)
		self.wire(self.down(),1)
		self.addResistor("R1_ninv_"+str(self.__count_nonInvertingAOP), self.down(), str(r1))
		self.addGround(self.down(),2)

		self.setCursorToNode(self.getNode("Vs_ninv_"+str(self.__count_nonInvertingAOP)))

		self.__count_nonInvertingAOP +=1


	"""
	@end
	"""

	"""
	@begin
	@method derivating
	@des 
	Cette méthode permet de générer un montage à AOP dérivateur
	@sed
	@range publique
	@input @string Label d'entrée
	@input @string Label de sortie
	@input @string Label d'alimentation positive
	@input @string Label d'alimentation négative (ou masse)
	@input @float Valeur de la résistance R1
	@input @float Valeur de la résistance R2 (contre-réaction)
	@type_return @boolean
	@return False en cas de succès
	@example ltspice.derivating("+VCC", "-VCC", 1000, 1000)
	@code
	"""
	def derivating(self, vcc, vee, r1, r2, c1):



		self.addAop(name="U_ninv_"+str(self.__count_nonInvertingAOP), teta=self.up(), miror=1, link="+",vcc_label=vcc, vee_label=vee, other_input="E_inv_"+str(self.__count_nonInvertingAOP)) #AOp right, signal on -
		self.wire(self.right(), 2)
		self.addNode("Vs_ninv_"+str(self.__count_nonInvertingAOP))
		self.wire(self.down(), 6)
		self.wire(self.left(), 1)
		self.addResistor("R2_ninv_"+str(self.__count_nonInvertingAOP), self.left(), str(r2))
		self.wire(self.left(),1)
		self.addNode("N_ninv_"+str(self.__count_nonInvertingAOP))
		self.wireToNode(self.getNode("E_inv_"+str(self.__count_nonInvertingAOP)))
		self.setCursorToNode(self.getNode("N_ninv_"+str(self.__count_nonInvertingAOP)))
		self.wire(self.left(),6)
		self.wire(self.down(),1)
		self.addResistor("R1_ninv_"+str(self.__count_nonInvertingAOP), self.down(), str(r1))
		self.addGround(self.down(),2)

		self.setCursorToNode(self.getNode("Vs_ninv_"+str(self.__count_nonInvertingAOP)))

		self.__count_nonInvertingAOP +=1


	"""
	@end
	"""