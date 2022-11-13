# -*- coding: utf-8 -*-

from Utils.Debug.Debug import Debug
import time

from System.Monitoring.Computer import main as mainComputer
from System.WebServer.WebServer import main as mainWebServer

from Processing.Electronic.Simulation.LTSpice import main as mainLTSpice

debug = Debug()

debug.println("Checking of directory", Debug.INFO)

debug.println("Running 'Computer' module", Debug.INFO)
mainComputer()
time.sleep(2)

debug.println("Running 'LTSpice' module", Debug.INFO)
mainLTSpice()
time.sleep(2)


debug.println("Running 'WebServer' module", Debug.INFO)
mainWebServer()
time.sleep(2)



