# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QStatusBar
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from ui_mainwindow import Ui_MainWindow

from EnergyHandler import ConsumptionCalendar, House

from Power.SolarPlant import Panels, SunCalendar

from Storages.SaltPlant import SaltPlant
from Storages.HydrogenPlant import HydrogenPlant
from Storages.Battery import Battery
from Tools.Debug import Debug


class MainWindow(QMainWindow):
    def __init__(self):
        
        super(MainWindow, self).__init__()
        #self.load_ui()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.debug = Debug()
        self.init()

    def init(self):
        
        self.debug.println("Init")
        #self.createStatusBar()
        #self.initArrays()


    # def createStatusBar(self):
    #     status = QStatusBar()
    #     status.showMessage("Application : Started")
    #     self.setStatusBar(status)
        

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
