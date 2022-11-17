import math
from Battery.Battery import Battery
from EnergyHandler import ConsumptionCalendar, EnergyHandler
from SolarPlant.SolarPlant import Panels, SunCalendar
from SaltPlant.SaltPlant import SaltPlant
from HydrogenPlant.HydrogenPlant import HydrogenPlant

sunCalendar = SunCalendar([1.2, 3.4, 5.5, 7.5, 6.4, 6.3, 6.9, 5.2, 3, 1.8,1.5,0.7])
consumptionCalendar = ConsumptionCalendar([590,542,560,472,436,407,413,420,439,491,520,551])

battery = Battery(20, 12, 290)
panels = Panels(power_cret=250,area=65, unitArea=1.7)
salt = SaltPlant(10,300)

energyHandler = EnergyHandler(battery=battery, panels=panels, sunCalendar=sunCalendar, consumptionCalendar=consumptionCalendar, saltPlant=salt)

energyHandler.simulate()