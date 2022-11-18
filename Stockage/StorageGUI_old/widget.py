# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QWidget, QStatusBar, QToolBar, QMenuBar
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from EnergyHandler import ConsumptionCalendar, House

from Power.SolarPlant import Panels, SunCalendar

from Storages.SaltPlant import SaltPlant
from Storages.HydrogenPlant import HydrogenPlant
from Storages.Battery import Battery
from Tools.Debug import Debug

class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()
        self.debug = Debug()
        self.load_ui()
        self.init()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def init(self):
        self.debug.println("Init")
        self.createStatusBar()
        #self.initArrays()


    def createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)
        


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
