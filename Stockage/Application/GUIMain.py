#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import matplotlib.pyplot as plt

from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from Tools.ThreadHandler import ThreadHandler, ThreadHandlerMode

import time
from PyQt5.QtCore import QIODevice
from PyQt5.QtCore import QTimer,QDateTime

import sys
from House import ConsumptionCalendar, House

from Power.SolarPlant import Panels, SunCalendar

from Storages.SaltPlant import SaltPlant
from Storages.HydrogenPlant import HydrogenPlant
from Storages.Battery import Battery
from Tools.Debug import Debug

from GUI import *  #Fenêtre générée par pyuic5


class MainWindow(QtWidgets.QMainWindow):
    
	def __init__(self, parent=None):
		super(MainWindow, self).__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.debug = Debug()

		self.__house = House()

		self.msgSc = QShortcut(QKeySequence('F5'), self).activated.connect(self.run)
		self.sLeft = QShortcut(QtCore.Qt.Key_Left, self).activated.connect(self.previousImage)
		self.sRight = QShortcut(QtCore.Qt.Key_Right, self).activated.connect(self.nextImage)
  
  
		self.indexToMonths = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Décembre"]
        
		self.ui.graph_battery.setBackground("white")
		self.ui.graph_hydrogen.setBackground("white")
		self.ui.graph_panels.setBackground("white")
		self.ui.graph_salt.setBackground("white")
		self.ui.graph_bilan.setBackground("white")
		#Power
		self.__power = []
		self.ui.pb_addPower.clicked.connect(self.addPower)
		#Storage
		self.__storage = []
		self.ui.pb_addStorage.clicked.connect(self.addStorage)
  
		self.ui.pb_animateStorage.clicked.connect(self.animateStorage)
		self.ui.pb_animatePower.clicked.connect(self.animatePower)
		self.ui.pb_animateBilan.clicked.connect(self.animateBilan)
  
		self.ui.pb_run.clicked.connect(self.run)
  
		self.__currentIndexPowerMonth = 0
		self.__currentIndexStorageMonth = 0
		self.__currentIndexBilanMonth = 0
		
		self.disableAllPowerSettings()
		self.disableAllStorageSettings()

		self.ui.pb_nextPower.clicked.connect(self.incrementMonthPower)
		self.ui.pb_previousPower.clicked.connect(self.DecrementMonthPower)
		self.ui.pb_nextStorage.clicked.connect(self.incrementMonthStorage)
		self.ui.pb_previousStorage.clicked.connect(self.DecrementMonthStorage)
		self.ui.pb_nextBilan.clicked.connect(self.incrementMonthBilan)
		self.ui.pb_previousBilan.clicked.connect(self.DecrementMonthBilan)
		#self.run()

	def incrementMonthPower(self):
		
		if(self.__currentIndexPowerMonth==11):
			self.__currentIndexPowerMonth = 0
		else:
			self.__currentIndexPowerMonth += 1
		self.displayCharts()
   
	def incrementMonthStorage(self):
		if(self.__currentIndexStorageMonth==11):
			self.__currentIndexStorageMonth = 0
		else:
			self.__currentIndexStorageMonth += 1
		self.displayCharts()
   
	def DecrementMonthPower(self):

		if(self.__currentIndexPowerMonth<=0):
			self.__currentIndexPowerMonth = 11
		else:
			self.__currentIndexPowerMonth -= 1
		self.displayCharts()
   
	def incrementMonthBilan(self):
		if(self.__currentIndexBilanMonth==11):
			self.__currentIndexBilanMonth = 0
		else:
			self.__currentIndexBilanMonth += 1
		self.displayCharts()
  
	def DecrementMonthStorage(self):
		
		if(self.__currentIndexStorageMonth<=0):
			self.__currentIndexStorageMonth = 11
		else:
			self.__currentIndexStorageMonth -= 1
		self.displayCharts()

   
	def DecrementMonthBilan(self):
		
		if(self.__currentIndexBilanMonth<=0):
			self.__currentIndexBilanMonth = 11
		else:
			self.__currentIndexBilanMonth -= 1
		self.displayCharts()
  
	def loadData(self):	
     
		self.debug.println("Loading consumption per month values")
		tmpList = []
		for i in range(0,12):
			tmpList.append(int(self.ui.tw_consumption.item(i,0).text()))
		self.__house.setConsumptionCalendar(ConsumptionCalendar(tmpList))
		self.__house.setAnnualEnergy(self.ui.sb__consumptionYear.value())
		
		self.debug.println("Loading sun per month values")
		tmpList = []
		for i in range(0,12):
			tmpList.append(float(self.ui.tw_sun.item(i,0).text()))
		self.__house.setSunCalendar(SunCalendar(tmpList))

		self.__house.rateHeat(self.ui.sb_rateHeat.value()/100)

		for s in self.__storage:
			self.__house.addStorage(s)
		for p in self.__power:
			self.__house.addPower(p)
   
	def addPower(self):
		
		if(not self.ui.cb_power.isEnabled()):
			return
		self.ui.tw_addPower.setRowCount(self.ui.tw_addPower.rowCount()+1)

		self.ui.tw_addPower.setCellWidget(self.ui.tw_addPower.rowCount()-1,0, QLabel(self.ui.cb_power.currentText()))
		pbEdit = QPushButton("  Éditer")
		pbEdit.setIcon(QtGui.QIcon('Images/gear.png'))
		pbEdit.setStyleSheet("background-color:grey;color:white;")
		tmpIndex = self.ui.tw_addPower.rowCount()-1
		pbEdit.clicked.connect(lambda: self.editPower(tmpIndex))
  
		pbDelete = QPushButton("  Supprimer")
		pbDelete.setStyleSheet("background-color:red;color:white;")
		pbDelete.setIcon(QtGui.QIcon('Images/trash.png'))
		tmpVar = self.ui.cb_power.currentText()
		tmpName = self.ui.tw_addPower.rowCount()-1
		pbDelete.clicked.connect(lambda: self.removePower(tmpName, tmpVar))
  
		self.ui.tw_addPower.setCellWidget(self.ui.tw_addPower.rowCount()-1,1, pbEdit)
		self.ui.tw_addPower.setCellWidget(self.ui.tw_addPower.rowCount()-1,2, pbDelete)
		self.ui.tw_addPower.show()
  
		if(self.ui.cb_power.currentText()=="Panneaux solaires"): 
			self.__power.append(Panels(250, 65, 1.608))
			self.ui.statusbar.setStyleSheet("color:green;")
			self.ui.statusbar.showMessage("Panneaux solaires ajoutés")
		
		self.ui.cb_power.removeItem(self.ui.cb_power.currentIndex())
  
		if(self.ui.cb_power.count()==0):
			self.ui.cb_power.setEnabled(False)


	def addStorage(self):
		
		if(not self.ui.cb_storage.isEnabled()):
			return
		self.ui.tw_addStorage.setRowCount(self.ui.tw_addStorage.rowCount()+1)

		self.ui.tw_addStorage.setCellWidget(self.ui.tw_addStorage.rowCount()-1,0, QLabel(self.ui.cb_storage.currentText()))
		pbEdit = QPushButton("  Éditer")
		pbEdit.setIcon(QtGui.QIcon('Images/gear.png'))
		pbEdit.setStyleSheet("background-color:grey;color:white;")
		tmpIndex = self.ui.tw_addStorage.rowCount()-1
		pbEdit.clicked.connect(lambda: self.editStorage(tmpIndex))
  
		pbDelete = QPushButton("  Supprimer")
		pbDelete.setStyleSheet("background-color:red;color:white;")
		pbDelete.setIcon(QtGui.QIcon('Images/trash.png'))
		tmpVar = self.ui.cb_storage.currentText()
		tmpName = self.ui.tw_addStorage.rowCount()-1
		pbDelete.clicked.connect(lambda: self.removeStorage(tmpName, tmpVar))
  
		self.ui.tw_addStorage.setCellWidget(self.ui.tw_addStorage.rowCount()-1,1, pbEdit)
		self.ui.tw_addStorage.setCellWidget(self.ui.tw_addStorage.rowCount()-1,2, pbDelete)
		self.ui.tw_addStorage.show()
		self.ui.statusbar.setStyleSheet("color:green;")
		if(self.ui.cb_storage.currentText()=="Hydrogène"):
			self.__storage.append(HydrogenPlant())
			self.ui.statusbar.showMessage("Centrale hydrogène ajouté")
		elif(self.ui.cb_storage.currentText()=="Batterie_plomb"):
			self.__storage.append(Battery(5,12,290))
			self.ui.statusbar.showMessage("Batterie ajoutée")
		elif(self.ui.cb_storage.currentText()=="Sel"):
			self.__storage.append(SaltPlant(10,300))
			self.ui.statusbar.showMessage("Centrale de sel ajoutée")
		else:
			pass

		self.ui.cb_storage.removeItem(self.ui.cb_storage.currentIndex())
  
		if(self.ui.cb_storage.count()==0):
			self.ui.cb_storage.setEnabled(False)
   
	def disableAllPowerSettings(self):

		self.ui.lbl_areaPanel.setVisible(False)
		self.ui.lbl_surface.setVisible(False)
		self.ui.lbl_power.setVisible(False)
		self.ui.dsb_area.setVisible(False)
		self.ui.dsb_areaPanel.setVisible(False)
		self.ui.dsb_powerPanel.setVisible(False)
		self.ui.dsb_area.setVisible(False)
		self.ui.lbl_unit_area.setVisible(False)
		self.ui.lbl_unit_areaPanel.setVisible(False)
		self.ui.lbl_unit_power.setVisible(False)
		self.ui.pb_savePower.setVisible(False)
  
	def disableAllStorageSettings(self):
		
		self.ui.lbl_cap.setVisible(False)
		self.ui.lbl_countBat.setVisible(False)
		self.ui.lbl_selfDischargeRate.setVisible(False)
		self.ui.lbl_voltage.setVisible(False)
		self.ui.lbl_volumeSalt.setVisible(False)
		self.ui.lbl_energySalt.setVisible(False)
		self.ui.lbl_volumeHydrogen.setVisible(False)
		self.ui.lbl_pressure.setVisible(False)

		self.ui.dsb_capacity.setVisible(False)
		self.ui.dsb_energyMCube.setVisible(False)
		self.ui.dsb_energySalt.setVisible(False)
		self.ui.dsb_voltage.setVisible(False)
		self.ui.dsb_discharge.setVisible(False)
		self.ui.sb_countBat.setVisible(False)
		self.ui.dsb_volumeHydrogen.setVisible(False)
		self.ui.cb_pressure.setVisible(False)
  
		self.ui.lbl_unit_capacity.setVisible(False)
		self.ui.lbl_unit_selfDischarge.setVisible(False)
		self.ui.lbl_unit_voltage.setVisible(False)
		self.ui.lbl_unit_energySalt.setVisible(False)
		self.ui.lbl_unit_volumeSalt.setVisible(False)
		self.ui.lbl_unitPressure.setVisible(False)
		self.ui.lbl_unitVolumHydrogen.setVisible(False)
		self.ui.pb_saveStorage.setVisible(False)
  
  
	def editPower(self, index):
		#Clear all settings
		self.disableAllPowerSettings()
		object = self.__power[index]
  
		# for a in self.__power:
		# 	print(a)
   
		if(type(object)==Panels):

			self.ui.lbl_areaPanel.setVisible(True)
			self.ui.lbl_surface.setVisible(True)
			self.ui.lbl_power.setVisible(True)
			self.ui.dsb_area.setVisible(True)
			self.ui.dsb_areaPanel.setVisible(True)
			self.ui.dsb_powerPanel.setVisible(True)
			self.ui.dsb_area.setVisible(True)
			self.ui.lbl_unit_area.setVisible(True)
			self.ui.lbl_unit_areaPanel.setVisible(True)
			self.ui.lbl_unit_power.setVisible(True)

			self.ui.dsb_area.setValue(object.getArea())
			self.ui.dsb_powerPanel.setValue(object.getPower())
			self.ui.dsb_areaPanel.setValue(object.getUnitArea())
			self.ui.pb_savePower.setVisible(True)
			self.ui.pb_savePower.clicked.connect(self.savePower)
			#Update value
   
	def editStorage(self, index):
     
		self.disableAllStorageSettings()
		object = self.__storage[index]

		if(type(object)==Battery):
			
			self.ui.lbl_cap.setVisible(True)
			self.ui.lbl_countBat.setVisible(True)
			self.ui.lbl_selfDischargeRate.setVisible(True)
			self.ui.lbl_voltage.setVisible(True)

			self.ui.dsb_capacity.setVisible(True)
			self.ui.dsb_voltage.setVisible(True)
			self.ui.dsb_discharge.setVisible(True)
			self.ui.sb_countBat.setVisible(True)
  
			self.ui.lbl_unit_capacity.setVisible(True)
			self.ui.lbl_unit_selfDischarge.setVisible(True)
			self.ui.lbl_unit_voltage.setVisible(True)
   
			self.ui.sb_countBat.setValue(object.getCount())
			self.ui.dsb_capacity.setValue(object.getCapacity())
			self.ui.dsb_voltage.setValue(object.getVoltage())
			self.ui.pb_saveStorage.setVisible(True)
			self.ui.pb_saveStorage.clicked.connect(lambda: self.saveStorage(index))
   
		elif(type(object)==HydrogenPlant):
		
			self.ui.pb_saveStorage.setVisible(True)
			self.ui.pb_saveStorage.clicked.connect(lambda :self.saveStorage(index))
			self.ui.lbl_volumeHydrogen.setVisible(True)
			self.ui.lbl_pressure.setVisible(True)
			self.ui.dsb_volumeHydrogen.setVisible(True)
			self.ui.cb_pressure.setVisible(True)
			self.ui.lbl_volumeHydrogen.setVisible(True)
			self.ui.lbl_unitPressure.setVisible(True)
			self.ui.lbl_unitVolumHydrogen.setVisible(True)

   
		elif(type(object)==SaltPlant):
			
			self.ui.lbl_energySalt.setVisible(True)
			self.ui.lbl_volumeSalt.setVisible(True)
			self.ui.lbl_unit_energySalt.setVisible(True)
			self.ui.lbl_unit_volumeSalt.setVisible(True)
			self.ui.dsb_energyMCube.setVisible(True)
			self.ui.dsb_energySalt.setVisible(True)
			self.ui.pb_saveStorage.setVisible(True)
			self.ui.pb_saveStorage.clicked.connect(lambda : self.saveStorage(index))
   
		else:
			pass
			
   
	def saveStorage(self, index):
     
		object = self.__storage[index]
		if(type(object)==Battery):
  
			object.setCount(self.ui.sb_countBat.value())
			object.setVoltage(self.ui.dsb_voltage.value())
			object.setCapacity(self.ui.dsb_capacity.value())
			object.setDischargeRate(self.ui.dsb_discharge.value()/100)

		elif(type(object)==SaltPlant):
			object.setVolume(self.ui.dsb_energySalt.value())
			object.setEnergyMCube(self.ui.dsb_energyMCube.value())
		elif(type(object)==HydrogenPlant):
			object.setPressure(int(self.ui.cb_pressure.currentText()))
			object.setMaxVolume(self.ui.dsb_volumeHydrogen.value())
		else:
			self.debug.println("ERREUR")

	def savePower(self, index):
		object = self.__power[index]
  
		if(type(object)==Panels):
  
			object.setPower(self.ui.dsb_powerPanel.value())
			object.setUnitArea(self.ui.dsb_areaPanel.value())
			object.setArea(self.ui.dsb_area.value())


	def removePower(self, index, name):
     
		self.__power.remove(self.__power[index])
		self.ui.tw_addPower.removeRow(index)
		if(len(self.__power)==0):
			self.disableAllPowerSettings()
		self.ui.cb_power.addItem(name)
		self.ui.cb_power.setEnabled(True)
		self.ui.cb_power.show()
   
	def removeStorage(self, index, name):

		self.ui.tw_addStorage.removeRow(index)
		if(len(self.__storage)==0):
			self.disableAllStorageSettings()
		else:
			self.__storage.remove(self.__storage[index])
		self.ui.cb_storage.addItem(name)
		self.ui.cb_storage.setEnabled(True)
		self.ui.cb_storage.show()

	def clearCharts(self):
     
		self.ui.graph_battery.clear()
		self.ui.graph_hydrogen.clear()
		self.ui.graph_panels.clear()
		self.ui.graph_salt.clear()
		self.ui.graph_bilan.clear()
  
	def stopAnimateStorage(self):
     
		self.timerAnimateStorage.stop()
		self.timerIncrementStorage.stop()
		self.ui.pb_animateStorage.setStyleSheet("background-color:white;color:black")
		self.ui.pb_animateStorage.setText("Animer")
		self.ui.pb_animateStorage.clicked.connect(self.animateStorage)
  
	def stopAnimatePower(self):
		self.timerAnimatePower.stop()
		self.timerIncrementPower.stop()
		self.ui.pb_animatePower.setStyleSheet("background-color:white;color:black")
		self.ui.pb_animatePower.setText("Animer")
		self.ui.pb_animatePower.clicked.connect(self.animatePower)
  
	def stopAnimateBilan(self):
     
		self.timerAnimateBilan.stop()
		self.timerIncrementBilan.stop()
		self.ui.pb_animateBilan.setStyleSheet("background-color:white;color:black")
		self.ui.pb_animateBilan.setText("Animer")
		self.ui.pb_animateBilan.clicked.connect(self.animateBilan)
  
	def animatePower(self):
		
		self.timerAnimatePower = QtCore.QTimer()
		self.timerAnimatePower.setInterval(self.ui.sb_animateTimePower.value())
		self.timerAnimatePower.timeout.connect(self.displayCharts)
		self.timerAnimatePower.start()

		self.ui.pb_animatePower.setStyleSheet("background-color:orange;color:white")
		self.ui.pb_animatePower.setText("Arrêter")
		self.ui.pb_animatePower.clicked.connect(self.stopAnimatePower)

		time.sleep(0.01)

		self.timerIncrementPower = QtCore.QTimer()
		self.timerIncrementPower.setInterval(self.ui.sb_animateTimePower.value())
		self.timerIncrementPower.timeout.connect(self.incrementMonthPower)
		self.timerIncrementPower.start()
  
	def animateStorage(self):
		
		
		self.timerAnimateStorage = QtCore.QTimer()
		self.timerAnimateStorage.setInterval(100)
		self.timerAnimateStorage.timeout.connect(self.displayCharts)
		self.timerAnimateStorage.start()

		self.ui.pb_animateStorage.setStyleSheet("background-color:orange;color:white")
		self.ui.pb_animateStorage.setText("Arrêter")
		self.ui.pb_animateStorage.clicked.connect(self.stopAnimateStorage)

		time.sleep(0.01)

		self.timerIncrementStorage = QtCore.QTimer()
		self.timerIncrementStorage.setInterval(self.ui.sb_animateTimeStorage.value())
		self.timerIncrementStorage.timeout.connect(self.incrementMonthStorage)
		self.timerIncrementStorage.start()
  
	def animateBilan(self):
		
		
		self.timerAnimateBilan = QtCore.QTimer()
		self.timerAnimateBilan.setInterval(100)
		self.timerAnimateBilan.timeout.connect(self.displayCharts)
		self.timerAnimateBilan.start()

		self.ui.pb_animateBilan.setStyleSheet("background-color:orange;color:white")
		self.ui.pb_animateBilan.setText("Arrêter")
		self.ui.pb_animateBilan.clicked.connect(self.stopAnimateBilan)

		time.sleep(0.01)

		self.timerIncrementBilan = QtCore.QTimer()
		self.timerIncrementBilan.setInterval(self.ui.sb_animateTimeBilan.value())
		self.timerIncrementBilan.timeout.connect(self.incrementMonthBilan)
		self.timerIncrementBilan.start()

	def nextImage(self):
     
		currentIndexPage = self.ui.tabWidget.currentIndex()
  
		if(currentIndexPage==3):
			self.incrementMonthStorage()
			self.displayCharts()
		elif(currentIndexPage==4):
			self.incrementMonthPower()
			self.displayCharts()
		elif(currentIndexPage==5):
			self.incrementMonthBilan()
			self.displayCharts()
   
	def previousImage(self):
     
		currentIndexPage = self.ui.tabWidget.currentIndex()
  
		if(currentIndexPage==3):
			self.DecrementMonthStorage()
			self.displayCharts()
		elif(currentIndexPage==4):
			self.DecrementMonthPower()
			self.displayCharts()
		elif(currentIndexPage==5):
			self.DecrementMonthBilan()
			self.displayCharts()
	def displayCharts(self):
		
		self.clearCharts()
		self.debug.println("Update of charts")
		self.ui.lbl_startPower.setText("Début de la simulation au mois de "+str(self.indexToMonths[self.__currentIndexPowerMonth]))
		self.ui.lbl_startStorage.setText("Début de la simulation au mois de "+str(self.indexToMonths[self.__currentIndexStorageMonth]))
		self.ui.lbl_startBilan.setText("Début de la simulation au mois de "+str(self.indexToMonths[self.__currentIndexBilanMonth]))
		#Battery
		try:
			
			graphDataX = self.graphes[0][self.__currentIndexStorageMonth].getData()[0]
			graphDataY = self.graphes[0][self.__currentIndexStorageMonth].getData()[1]
			title = self.graphes[0][self.__currentIndexStorageMonth].getData()[2]
			color = self.graphes[0][self.__currentIndexStorageMonth].getData()[3]
			legend = self.graphes[0][self.__currentIndexStorageMonth].getData()[5]
			self.ui.graph_battery.addLegend()
			self.ui.graph_battery.setBackground("white")
			self.ui.graph_battery.plot(graphDataX, graphDataY, pen=color, width=6, symbol="o", name=legend)
			self.ui.graph_battery.setTitle(title)
		except:
			print("erreur")

		try:
			graphDataX = self.graphes[1][self.__currentIndexPowerMonth].getData()[0]
			graphDataY = self.graphes[1][self.__currentIndexPowerMonth].getData()[1]
			title = self.graphes[1][self.__currentIndexPowerMonth].getData()[2]
			color = self.graphes[1][self.__currentIndexPowerMonth].getData()[3]
			legend = self.graphes[1][self.__currentIndexPowerMonth].getData()[5]
			self.ui.graph_panels.addLegend()
			self.ui.graph_panels.setBackground("white")
			self.ui.graph_panels.plot(graphDataX, graphDataY, pen=color, symbol="o", name=legend)
			self.ui.graph_panels.setTitle("Energie")
  
			graphDataX = self.graphes[3][self.__currentIndexPowerMonth].getData()[0]
			graphDataY = self.graphes[3][self.__currentIndexPowerMonth].getData()[1]
			title = self.graphes[3][self.__currentIndexPowerMonth].getData()[2]
			color = self.graphes[3][self.__currentIndexPowerMonth].getData()[3]
			legend = self.graphes[3][self.__currentIndexPowerMonth].getData()[5]
			self.ui.graph_panels.addLegend()
			self.ui.graph_panels.setBackground("white")
			self.ui.graph_panels.plot(graphDataX, graphDataY, pen=color, symbol="o", name=legend)
		except:
			self.ui.graph_panels.setTitle("Pas de données")
   
		try:
			graphDataX = self.graphes[2][self.__currentIndexStorageMonth].getData()[0]
			graphDataY = self.graphes[2][self.__currentIndexStorageMonth].getData()[1]
			title = self.graphes[2][self.__currentIndexStorageMonth].getData()[2]
			color = self.graphes[2][self.__currentIndexStorageMonth].getData()[3]
			legend = self.graphes[2][self.__currentIndexStorageMonth].getData()[5]
			self.ui.graph_salt.addLegend()
			self.ui.graph_salt.addLegend()
			self.ui.graph_salt.plot(graphDataX, graphDataY, pen=color, symbol="o", name=legend)
			self.ui.graph_salt.setTitle("Energie par stockage de sel")
		except:
			self.ui.graph_salt.setTitle("Pas de données")
   
		try:
			graphDataX = self.graphes[4][self.__currentIndexBilanMonth].getData()[0]
			graphDataY = self.graphes[4][self.__currentIndexBilanMonth].getData()[1]
			title = self.graphes[4][self.__currentIndexBilanMonth].getData()[2]
			color = self.graphes[4][self.__currentIndexBilanMonth].getData()[3]
			legend = self.graphes[4][self.__currentIndexBilanMonth].getData()[5]
			self.ui.graph_bilan.addLegend()
			self.ui.graph_bilan.addLegend()
			self.ui.graph_bilan.plot(graphDataX, graphDataY, pen=color, symbol="o", name=legend)
			self.ui.graph_bilan.setTitle("Bilan")
		except:
			self.ui.graph_bilan.setTitle("Pas de données")
   
		try:
			graphDataX = self.graphes[5][self.__currentIndexBilanMonth].getData()[0]
			graphDataY = self.graphes[5][self.__currentIndexBilanMonth].getData()[1]
			title = self.graphes[5][self.__currentIndexBilanMonth].getData()[2]
			color = self.graphes[5][self.__currentIndexBilanMonth].getData()[3]
			legend = self.graphes[5][self.__currentIndexBilanMonth].getData()[5]
			self.ui.graph_hydrogen.addLegend()
			self.ui.graph_hydrogen.addLegend()
			self.ui.graph_hydrogen.plot(graphDataX, graphDataY, pen=color, symbol="o", name=legend)
			self.ui.graph_hydrogen.setTitle("Volume d'hydrogène")
		except:
			self.ui.graph_hydrogen.setTitle("Pas de données")
	def run(self):
		
		self.loadData()
  
		message = self.__house.check()
		if(message):
			self.ui.statusbar.showMessage(message)
			self.ui.statusbar.setStyleSheet("color:red;")
		else:
			self.ui.statusbar.setStyleSheet("color:orange;")
			self.ui.statusbar.showMessage("Simulation en cours")
			self.graphes = self.__house.simulate() #All data
			self.displayCharts()
			self.ui.statusbar.setStyleSheet("color:green;")
			self.ui.statusbar.showMessage("Simulation terminée")
			self.debug.println("Simulation terminée", Debug.SUCCESS)
			self.__house.clearData()
def main():
	
	app = QtWidgets.QApplication(sys.argv) #Creation de l'application
	ihm = MainWindow()                      #Appel de notre classe principale
	ihm.show()                              #Affichage de l'interface
	sys.exit(app.exec_())                   #Loop


if __name__ == "__main__":              
    main()



