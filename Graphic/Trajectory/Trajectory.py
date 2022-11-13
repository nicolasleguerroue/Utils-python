#!/usr/bin/env python
# coding: utf8

from time import *
from math import *
import os
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
#Pour retrouver les styles : print(plt.style.available[:6])
#plt.style.use('seaborn-whitegrid')



class Trajectory():

	"""Classe servant à calculer des trajectoires en utilisant les équations horaires"""

	def __init__(self):
		"Methode permettant d'initialiser les variables"

		self.angle = 45				#angle initial
		self.speed= 20				#vitesse initiale
		self.color="r"				#couleur du graphique
		self.posX=0					#postion en X d'origine
		self.posY=0					#postion en Y d'origine
		self.gravity=9.81			#intensité de la pesanteur
		self.timeMax = 10			#temps d'étude de la trajectoire
		self.resolution = 0.100		#résolution de l'étude
		self.distanceMax=0			#distance maximal lors de la fin de l'étude
		self.dot="--"				#type de points 
		self.lineWidth = 1			#épaisseur de la courbe
		self.name = ""				#nom de l'étude
		
	def setSpeed(self, speed):
		self.speed = speed
		print("Vitesse : " + str(self.speed) + "m/s")

	def setAngle(self, angle): #Angle en degré
		self.angle = angle
		print("Angle de départ : " + str(self.angle) + "°")
		
	def setPosX(self, x):
		self.x = x
		print("Position en X: " + str(self.x) + " m")
		
	def setPosY(self, y):
		self.y = y
		print("Position en Y : " + str(self.y) + " m")

	def setGravity(self, gravity):
		self.gravity = gravity
		print("Gravité : " + str(self.gravity) + "m/s²")
		
	def setTimeMax(self, timeMax):
		self.timeMax = timeMax	
		print("Temps de l'étude : "+ str(self.timeMax) + " s")	
		
	def setResolution(self, resolution=0.1):
		self.resolution = resolution	
		print("Résolution : "+ str(self.resolution) + " s")	
		
	def setColor(self, color="r"):
		self.color = color
		print("Couleur : "+ color)	

	def setDot(self, dot):
		self.dot = dot
		print("Trait : "+ self.dot)		
		
	def setName(self, name):
		self.name=name
		print("Nom du projet : "+self.name)	
		os.system("mkdir Resultats")
		os.system("mkdir Resultats/"+self.name)			
		os.system("mkdir Resultats/"+self.name+"/"+"position")
		os.system("mkdir Resultats/"+self.name+"/"+"vitesse")
		os.system("mkdir Resultats/"+self.name+"/"+"energie")
	def getTime_X(self, X=0.0):

		time = X/(self.speed*cos(self.angle*2*pi/360))
		return time
		#print("Pour parcourir " + str(X) + " m, il faudra " + str(time) + " s")

	def getTime_Y(self, X=0.0):

		time = sqrt( (-self.speed*cos(self.angle*2*pi/360)*2/self.gravity ) )
		return time
		#print("Pour parcourir " + str(Y) + " m, il faudra " + str(time) + " s")
				
		
		
	def getX(self, time=0.0):
		
		X = self.speed*cos(self.angle*2*pi/360)*time
		return X
		#print("En " + str(time) + " s, l'objet aura parcourut  " + str(X) + " m horizontalement")
	
	def getY(self, time=0.0):
		
		Y = -0.5*self.gravity*time*time+self.speed*sin(self.angle*2*pi/360)*time+self.posY # On rajoute son image
		return Y
		#print("En " + str(time) + " s, l'objet aura parcourut  " + str(Y) + " m verticalement")
		
		
	def getVx(self, time=0.0): #retourne la vitesse de l'objet considéré comme un unique point
		
		Vx = self.speed*cos(self.angle*2*pi/360)
		return Vx
		#print("En " + str(time) + " s, l'objet aura parcourut  " + str(X) + " m horizontalement")
		
	def getVy(self, time=0.0): #retourne la vitesse de l'objet considéré comme un unique point
		
		Vy = self.speed*sin(self.angle*2*pi/360)+self.gravity*(-1)*time
		return Vy
		#print("En " + str(time) + " s, l'objet aura parcourut  " + str(X) + " m horizontalement")

	def getV(self, time=0.0): #retourne la vitesse de l'objet considéré comme un unique point
		
		V = sqrt( self.getVx(time)**2 + self.getVy(time)**2 )
		return V
		#print("En " + str(time) + " s, l'objet aura parcourut  " + str(X) + " m horizontalement")
		

		
	def initSetupFiles(self):#creer le fichier des paramètres dans le dossier nommé

		filePosition = open("Resultats/"+str(self.name)+"/parametres.txt", "w") #Ouverture et création du fichier filePosition
		
		filePosition.write( "##################################################################################\n") #saut de ligne
		filePosition.write( "##  ETUDE D'UNE TRAJECTOIRE    \n") #saut de ligne
		filePosition.write( "##################################################################################\n") #saut de ligne
		filePosition.write( "##  CONDITIONS INITIALES       \n") #saut de ligne	
		filePosition.write( "##################################################################################\n") #saut de ligne
		filePosition.write( "##  ANGLE DE VISÉE     : "+str(self.angle)+" °\n") #saut de ligne	
		filePosition.write( "##  VITESSE INITIALE   : "+str(self.speed)+" m/s\n") #saut de ligne	
		filePosition.write( "##  GRAVITÉ            : "+str(self.gravity)+" m/s²\n") #saut de ligne			
		filePosition.write( "##  COULEUR GRAPHIQUE  : "+str(self.color)+" \n") #saut de ligne
		filePosition.write( "##  POSITION X         : "+str(self.posX)+" m\n") #saut de ligne
		filePosition.write( "##  POSITION Y         : "+str(self.posY)+" m\n") #saut de ligne
		filePosition.write( "##  TEMPS DE L'ANALYSE : "+str(self.timeMax)+" s \n") #saut de ligne
		filePosition.write( "##  RESOLUTION         : "+str(self.resolution)+" \n") #saut de ligne
		filePosition.write( "##  NOMBRE DE POINTS   : "+str( self.timeMax/self.resolution)+" \n") #saut de ligne
		filePosition.write( "##  TYPE DE POINT      : "+str(self.dot)+" \n") #saut de ligne
		filePosition.write( "##  EPAISSEUR DE LIGNE : "+str(self.lineWidth)+" \n") #saut de ligne
		filePosition.write( "##################################################################################\n") #saut de ligne

		filePosition.close() #Fermeture du fichier FilePosition
		
		

	def displayPosition(self):
		
		#  X(t)   ######################### [OK]
		print("Génération du graphique de position pour X(t)...")
		
		t = [] #liste des abscisses -> temps (s)
		x = [] #liste des ordonnées - distance X (m)
		T = 0 # correspond au t de f(t) -> variable qui change dans le temps
		
		if(self.name==""):
			self.setName("projet")
			self.initSetupFiles()
		else:
			self.initSetupFiles()
		
		filePosition = open("Resultats/"+str(self.name)+"/position/X(t).txt", "w") #Ouverture et création du fichier filePosition

		for k in range(0, self.timeMax*int(1/self.resolution)): # On veut les points de 0 à TimeMax avec une résolution égale à 0.001 par exemple
			t.append(T+self.posX) #Calcul de l'abscisse (t)
			x.append(self.speed*cos(self.angle*2*pi/360)*T+self.posX) # On rajoute son image
			filePosition.write( "X(t="+str(t[k])+")="+str(x[k])+"\n") #écrit la valeur dans un fichier text
			T += self.resolution # on augmente t de 1 résolution pour passer au point suivant
				
		graph = plt.figure()
		graph.add_subplot(1,3,1) #Crée un tableau de 2 lignes et 1 colonnes et selectionne l'élément n°1
		graph.canvas.set_window_title('Graphique Position : X(t), Y(t), Y(X)')
		plt.title("X(t)")
		plt.xlabel('Temps t (s)')
		plt.ylabel("Distance X (m)")
		plt.plot(t, x,self.color+self.dot, linewidth=self.lineWidth)
		
		plt.text(s="X(t="+str(self.timeMax)+")="+str(x[len(x)-1]), x=(self.timeMax/2),y=(x[len(x)-1]/2), color='red') #Affiche une valeur remarquable (Ymax pour Xmax)
		filePosition.close() #Fermeture du fichier FilePosition
		
		# Y(t)   #########################
		print("Génération du graphique de position pour Y(t)...")
		
		t = [] #liste des abscisses -> temps (s)
		y = [] #liste des ordonnées - hauteur (m)
		T = 0 # correspond au t de f(t) -> variable qui change dans le temps		
		
		filePosition = open("Resultats/"+str(self.name)+"/position/Y(t).txt", "w") #Ouverture et création du fichier filePosition

		for k in range(0, self.timeMax*int(1/self.resolution)): # On veut les points de 0 à TimeMax avec une résolution égale à 0.001 par exemple
			t.append(T+self.posX) #Calcul de l'abscisse (t)
			y.append(-0.5*9.81*T*T+self.speed*sin(self.angle*2*pi/360)*T+self.posY) # On rajoute son image
			filePosition.write( "Y(t="+str(t[k])+")="+str(y[k])+"\n") #écrit la valeur dans un fichier text
			T += self.resolution # on augmente t de 1 résolution pour passer au point suivant

		graph.add_subplot(1,3,2) #Crée un tableau de 2 lignes et 1 colonnes et selectionne l'élément n°1
		plt.title("Y(t)")
		plt.xlabel('Temps t (s)')
		plt.ylabel("hauteur Y (m)")
		plt.plot(t, y,self.color+self.dot, linewidth=self.lineWidth)
		
		plt.text(s="Y(t="+str(self.timeMax)+")="+str(y[len(y)-1]), x=(self.timeMax/2), y=(y[len(y)-1]/2), color='red') #Affiche une valeur remarquable (Ymax pour Xmax)
		filePosition.close() #Fermeture du fichier FilePosition
		
		#  Y(X)   #########################
		print("Génération du graphique de position pour Y(X)...")
		X = [] 	#liste des abscisses -> distance par rapport à l'origine défine (self.posX) (s)
		Y = [] 	#liste des ordonnées - hauteur (m)
		self.distanceMax = int(self.speed*cos(self.angle*2*pi/360)*self.timeMax) #X = V0*cos(teta)*t
		if(self.distanceMax==0):
			print("ÉTUDE DIFFICILE DE LA TRAJECTOIRE POUR CAUSE DE VITESSE TROP PETITE OU BIEN D'ANGLE TROP PROCHE DE 90° AVEC UN TEMPS FAIBLE")
			exit()
		abscisse = self.posX 	# L'abscisse de départ est self.posX
		
		filePosition = open("Resultats/"+str(self.name)+"/position/Y(X).txt", "w") #Ouverture et création du fichier filePosition
		
		for k in range(0, self.distanceMax*int(1/self.resolution)): # On veut les points de 0 à TimeMax avec une résolution égale à 0.001 par exemple
			X.append(abscisse+self.posX)
			Y.append(-self.gravity / (2*(self.speed**2)*(cos(self.angle*2*pi/360)**2) ) * abscisse**2 + tan(self.angle*2*pi/360) * abscisse)# On rajoute l'abscisse et son image par la fonction cos aux listes
			filePosition.write( "Y(X="+str(X[k])+")="+str(Y[k])+"\n") #écrit la valeur dans un fichier text
			abscisse += self.resolution # on augmente abscisse de pas pour passer au point suivant

		graph.add_subplot(1,3,3) #Crée un tableau de 2 lignes et 1 colonnes et selectionne l'élément n°3
		plt.title("Y(X)")
		plt.xlabel('distance X (m)')
		plt.ylabel("Y")
		plt.plot(X, Y,self.color+self.dot, linewidth=self.lineWidth)
		#calcule la position Y extreme
		
		plt.text(s="Y(X="+str(self.distanceMax)+")="+str(Y[len(Y)-1]), x=(self.timeMax/2), y=(Y[len(Y)-1]/2), color='red') #Affiche une valeur remarquable (Ymax pour Xmax)
		plt.show()
		filePosition.close() #Fermeture du fichier FilePosition
		
	def displaySpeed(self):
		
		#  X(t)   #########################
		print("Génération du graphique de vitesse pour Vx(t)...")
		
		t = [] #liste des abscisses -> temps (s)
		vx = [] #liste des ordonnées - vitesse Vx (m/s)
		T = 0 # correspond au t de f(t) -> variable qui change dans le temps
		
		if(self.name==""):
			self.setName("projet")
			self.initSetupFiles()
		else:
			self.initSetupFiles()
			
		fileSpeed = open("Resultats/"+str(self.name)+"/vitesse/Vx(t).txt", "w") #Ouverture et création du fichier filePosition
	
		for k in range(0, self.timeMax*int(1/self.resolution)): # On veut les points de 0 à TimeMax avec une résolution égale à 0.001 par exemple
			t.append(T+self.posX) #Calcul de l'abscisse (t)
			vx.append(self.speed*cos(self.angle*2*pi/360)) # On rajoute son image
			fileSpeed.write( "Vx(t="+str(t[k])+")="+str(vx[k])+"\n") #écrit la valeur dans un fichier text
			T += self.resolution # on augmente t de 1 résolution pour passer au point suivant
	
		graph = plt.figure()			
		graph.canvas.set_window_title('Graphique Vitesse : Vx(t), Vy(t), V(t)')	
		graph.add_subplot(1,3,1) #Crée un tableau de 2 lignes et 1 colonnes et selectionne l'élément n°1

		plt.title("Vx(t)")
		plt.xlabel('Temps t (s)')
		plt.ylabel("Vitesse Vx (m/s)")
		plt.plot(t, vx,self.color+self.dot, linewidth=self.lineWidth)
		
		plt.text(s="Vx(t="+str(self.timeMax)+")="+str(vx[len(vx)-1]), x=(self.timeMax/2), y=vx[len(vx)-1], color='red') #Affiche une valeur
		fileSpeed.close() #Fermeture du fichier FilePosition
		
		#  Vy(t)   #########################
		print("Génération du graphique de vitesse pour Vy(t)...")
		
		t = [] #liste des abscisses -> temps (s)
		vy = [] #liste des ordonnées - vitesse (m/s)
		T = 0 # correspond au t de f(t) -> variable qui change dans le temps
		
		fileSpeed = open("Resultats/"+str(self.name)+"/vitesse/Vy(t).txt", "w") #Ouverture et création du fichier filePosition
		
		for k in range(0, self.timeMax*int(1/self.resolution)): # On veut les points de 0 à TimeMax avec une résolution égale à 0.001 par exemple
			t.append(T+self.posX) #Calcul de l'abscisse (t)
			vy.append(self.speed*sin(self.angle*2*pi/360)+self.gravity*(-1)*T) # On rajoute son image
			fileSpeed.write( "Vy(t="+str(t[k])+")="+str(vy[k])+"\n") #écrit la valeur dans un fichier text
			T += self.resolution # on augmente t de 1 résolution pour passer au point suivant
		
		graph.add_subplot(1,3,2) #Crée un tableau de 2 lignes et 1 colonnes et selectionne l'élément n°1
		plt.title("Vy(t)")
		plt.xlabel('Temps t (s)')
		plt.ylabel("Vitesse Vy (m/s)")
		plt.plot(t, vy,self.color+self.dot, linewidth=self.lineWidth)
		
		plt.text(s="Vy(t="+str(self.timeMax)+")="+str(vy[len(vy)-1]), x=self.timeMax/2, y=vy[len(vy)-1]/2, color='red') #Affiche une valeur remarquable (Ymax pour Xmax)
		fileSpeed.close() #Fermeture du fichier FilePosition

		#  Y(X)   #########################
		print("Génération du graphique de vitesse pour V(t)...")
		
		t = [] 	#liste des abscisses -> temps par rapport à l'origine défine (self.posX) (s)
		speed = [] 	#liste des ordonnées - hauteur (m)
		self.distanceMax = int(self.speed*cos(self.angle*2*pi/360)*self.timeMax) #X = V0*cos(teta)*t
		
		fileSpeed = open("Resultats/"+str(self.name)+"/vitesse/V(t).txt", "w") #Ouverture et création du fichier filePosition
		
		abscisse = self.posX 	# L'abscisse de départ est self.posX
		for k in range(0, self.timeMax*int(1/self.resolution)): # On veut les points de 0 à TimeMax avec une résolution égale à 0.001 par exemple
			t.append(abscisse+self.posX)
			speed.append(sqrt( (vx[k])*(vx[k]) + (vy[k])*(vy[k]) )) # On rajoute l'abscisse et son image par la fonction cos aux listes
			fileSpeed.write( "V(t="+str(t[k])+")="+str(speed[k])+"\n") #écrit la valeur dans un fichier text
			abscisse += self.resolution # on augmente abscisse de pas pour passer au point suivant

		graph.add_subplot(1,3,3) #Crée un tableau de 2 lignes et 1 colonnes et selectionne l'élément n°2
		plt.title("V(t)")
		plt.xlabel('Temps t (s)')
		plt.ylabel("Vitesse v (m/s)")
		plt.plot(t, speed,self.color+self.dot, linewidth=self.lineWidth)
		
		plt.text(s="V(t="+str(self.timeMax)+")="+str(speed[len(speed)-1]), x=(self.timeMax/2), y=(speed[len(speed)-1]/2), color='red') #Affiche une valeur remarquable (Ymax pour Xmax)
		plt.show()
		fileSpeed.close() #Fermeture du fichier FilePosition


	def displayEnergy(self):
		
		#  X(t)   #########################
		print("Génération du graphique de l'energie cinétique...")
		
		t = [] #liste des abscisses -> temps (s)
		e = [] #liste des ordonnées - energie (J)
		T = 0 # correspond au t de f(t) -> variable qui change dans le temps
		
		if(self.name==""):
			self.setName("projet")
			self.initSetupFiles()
		else:
			self.initSetupFiles()
			
		fileEnergy = open("Resultats/"+str(self.name)+"/energie/E(t)", "w") #Ouverture et création du fichier filePosition
	
		for k in range(0, self.timeMax*int(1/self.resolution)): # On veut les points de 0 à TimeMax avec une résolution égale à 0.001 par exemple
			t.append(T+self.posX) #Calcul de l'abscisse (t)
			e.append(self.getV(T)**2*0.5) # On rajoute son image
			fileEnergy.write( "Vx(t="+str(t[k])+")="+str(e[k])+"\n") #écrit la valeur dans un fichier text
			T += self.resolution # on augmente t de 1 résolution pour passer au point suivant
	
		graph = plt.figure()			
		graph.canvas.set_window_title('Graphique Energie : E(t)')	

		plt.title("E(t)")
		plt.xlabel('Temps t (s)')
		plt.ylabel("Energie (J)")
		plt.plot(t, e,self.color+self.dot, linewidth=self.lineWidth)
		
		plt.text(s="E(t="+str(self.timeMax)+")="+str(e[len(e)-1]), x=(self.timeMax/2), y=e[len(e)-1], color='red') #Affiche une valeur
		plt.show()
		fileEnergy.close() #Fermeture du fichier FilePosition

if __name__ == "__main__":

	t = Trajectory() #Definie une nouvelle trajectoire

	t.setSpeed(100) #définie la vitesse initiale
	t.setAngle(1) #définie l'angle de visé
	t.setGravity(9.81) #définie la valeur de l'accélération
	t.setName("Ball") #definie le nom du dossier

	t.setResolution(0.01) #temps entre chaque point étudié
	t.setColor("b") #définie la couleur du graphique
	t.setTimeMax(1) #temps de l'étude
	t.setPosX(0) #définie la position d'origine sur l'axe X
	t.setPosY(0) #définie la position d'origine sur l'axe Y

	print(t.getV(4))


	t.displayPosition()
	t.displayEnergy()
	t.displaySpeed()




		
		
		
		
	
