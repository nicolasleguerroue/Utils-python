#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

from PyQt5.QtCore import QIODevice
from PyQt5.QtCore import QTimer,QDateTime

import sys
from EnergyHandler import ConsumptionCalendar, House

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
  
		#Power
		self.__power = []
		self.ui.pb_addPower.clicked.connect(self.addPower)
		#Storage
		self.__storage = []
		self.ui.pb_addStorage.clicked.connect(self.addStorage)
		
		self.loadData()
		self.disableAllPowerSettings()
		self.disableAllStorageSettings()
		#self.run()


	def loadData(self):	
     
		self.debug.println("Loading consumption per month values")
		tmpList = []
		for i in range(0,12):
			tmpList.append(int(self.ui.tw_consumption.item(0,i).text()))
		self.__house.setConsumptionCalendar(ConsumptionCalendar(tmpList))
		self.__house.setAnnualEnergy(self.ui.sb__consumptionYear.value())
		
		self.debug.println("Loading sun per month values")
		tmpList = []
		for i in range(0,12):
			tmpList.append(float(self.ui.tw_sun.item(0,i).text()))
		self.__house.setSunCalendar(SunCalendar(tmpList))



	def addPower(self):
		
		
		self.ui.tw_addPower.setRowCount(self.ui.tw_addPower.rowCount()+1)

		self.ui.tw_addPower.setCellWidget(self.ui.tw_addPower.rowCount()-1,0, QLabel(self.ui.cb_power.currentText()))
		pbEdit = QPushButton("Éditer")
		pbEdit.setStyleSheet("background-color:blue;color:white;")
		pbEdit.clicked.connect(lambda: self.editPower(index=self.ui.tw_addPower.rowCount()-1))
  
		pbDelete = QPushButton("Supprimer")
		pbDelete.setStyleSheet("background-color:red;color:white;")
		pbDelete.clicked.connect(lambda: self.removePower(index=self.ui.tw_addPower.rowCount()-1))
  
		self.ui.tw_addPower.setCellWidget(self.ui.tw_addPower.rowCount()-1,1, pbEdit)
		self.ui.tw_addPower.setCellWidget(self.ui.tw_addPower.rowCount()-1,2, pbDelete)
		self.ui.tw_addPower.show()
  
		if(self.ui.cb_power.currentText()=="Panneaux solaires"): 
			self.__power.append(Panels(250, 20, 1.608))
		
		self.ui.cb_power.removeItem(self.ui.cb_power.currentIndex())
   

	def addStorage(self):
		
		self.ui.tw_addStorage.setRowCount(self.ui.tw_addStorage.rowCount()+1)

		self.ui.tw_addStorage.setCellWidget(self.ui.tw_addStorage.rowCount()-1,0, QLabel(self.ui.cb_storage.currentText()))
		pbEdit = QPushButton("Éditer")
		pbEdit.setStyleSheet("background-color:blue;color:white;")
		pbEdit.clicked.connect(lambda: self.editStorage(index=self.ui.tw_addStorage.rowCount()-1))
  
		pbDelete = QPushButton("Supprimer")
		pbDelete.setStyleSheet("background-color:red;color:white;")
		pbDelete.clicked.connect(lambda: self.removeStorage(index=self.ui.tw_addStorage.rowCount()-1))
  
		self.ui.tw_addStorage.setCellWidget(self.ui.tw_addStorage.rowCount()-1,1, pbEdit)
		self.ui.tw_addStorage.setCellWidget(self.ui.tw_addStorage.rowCount()-1,2, pbDelete)
		self.ui.tw_addStorage.show()
  
		if(self.ui.cb_storage.currentText()=="Hydrogène"):
			self.__storage.append(HydrogenPlant())
		elif(self.ui.cb_storage.currentText()=="Batterie_plomb"):
			self.__storage.append(Battery(20,12,290))
		elif(self.ui.cb_storage.currentText()=="Sel"):
			self.__storage.append(SaltPlant(10,300))
		else:
			pass

		self.ui.cb_storage.removeItem(self.ui.cb_storage.currentIndex())
  
	def disableAllPowerSettings(self):
     
		self.ui.lbl_areaPanel.setVisible(False)
		self.ui.lbl_surface.setVisible(False)
		self.ui.lbl_volume.setVisible(False)
		self.ui.lbl_power.setVisible(False)
		self.ui.dsb_area.setVisible(False)
		self.ui.dsb_areaPanel.setVisible(False)
		self.ui.dsb_powerPanel.setVisible(False)
		self.ui.dsb_volume.setVisible(False)
		self.ui.dsb_area.setVisible(False)
		self.ui.lbl_unit_area.setVisible(False)
		self.ui.lbl_unit_areaPanel.setVisible(False)
		self.ui.lbl_unit_volume.setVisible(False)
		self.ui.lbl_unit_power.setVisible(False)
		self.ui.pb_savePower.setVisible(False)
  
	def disableAllStorageSettings(self):
		
		self.ui.lbl_cap.setVisible(False)
		self.ui.lbl_countBat.setVisible(False)
		self.ui.lbl_selfDischargeRate.setVisible(False)
		self.ui.lbl_voltage.setVisible(False)
		self.ui.lbl_volumeSalt.setVisible(False)
		self.ui.lbl_energySalt.setVisible(False)

		self.ui.dsb_capacity.setVisible(False)
		self.ui.dsb_energyMCube.setVisible(False)
		self.ui.dsb_energySalt.setVisible(False)
		self.ui.dsb_voltage.setVisible(False)
		self.ui.dsb_volume.setVisible(False)
		self.ui.dsb_discharge.setVisible(False)
		self.ui.sb_countBat.setVisible(False)
  
		self.ui.lbl_unit_capacity.setVisible(False)
		self.ui.lbl_unit_selfDischarge.setVisible(False)
		self.ui.lbl_unit_voltage.setVisible(False)
		self.ui.lbl_unit_energySalt.setVisible(False)
		self.ui.lbl_unit_volumeSalt.setVisible(False)
		self.ui.lbl_unit_energySalt.setVisible(False)

		self.ui.pb_saveStorage.setVisible(False)
  
  
	def editPower(self, index):
		#Clear all settings
		self.disableAllPowerSettings()
		print(index)
		object = self.__power[index]
  
		for a in self.__power:
			print(a)
   
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
     
		print("")
		self.disableAllStorageSettings()
 
	def savePower(self, index):
		object = self.__power[index]
  
		if(type(object)==Panels):
  
			object.setPower(self.ui.dsb_powerPanel.value())
			object.setUnitArea(self.ui.dsb_areaPanel.value())
			object.setArea(self.ui.dsb_area.value())
			self.debug.println("Update of Panel")
			for a in self.__power:
				print(a)

	def removePower(self, index):
		self.__power.remove(self.__power[index])
		self.ui.tw_addPower.removeRow(index)
		if(len(self.__power)==0):
			self.disableAllPowerSettings()
   
	def removeStorage(self, index):
		self.__storage.remove(self.__storage[index])
		self.ui.tw_addStorage.removeRow(index)
		if(len(self.__storage)==0):
			self.disableAllPowerSettings()
  
	def run(self):
     
		self.__house.simulate()

def main():
	
	app = QtWidgets.QApplication(sys.argv) #Creation de l'application
	ihm = MainWindow()                      #Appel de notre classe principale
	ihm.show()                              #Affichage de l'interface
	sys.exit(app.exec_())                   #Loop


if __name__ == "__main__":              
    main()



