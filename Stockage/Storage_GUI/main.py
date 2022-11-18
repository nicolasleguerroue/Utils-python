
from EnergyHandler import ConsumptionCalendar, House

from Power.SolarPlant import Panels, SunCalendar

from Storages.SaltPlant import SaltPlant
from Storages.HydrogenPlant import HydrogenPlant
from Storages.Battery import Battery

sunCalendar = SunCalendar([1.2, 3.4, 5.5, 7.5, 6.4, 6.3, 6.9, 5.2, 3, 1.8,1.5,0.7])
consumptionCalendar = ConsumptionCalendar([590,542,560,472,436,407,413,420,439,491,520,551])

battery = Battery(20, 12, 290)
panels = Panels(power_cret=250,area=65, unitArea=1.7)
salt = SaltPlant(10,300)

#house = House(annualEnergy=5840)

house = House(battery=battery, panels=panels, sunCalendar=sunCalendar, saltPlant=salt)

#house.setConsumptionCalendar(consumptionCalendar)
house.addStorage(battery)
house.addStorage(salt)


house.addPower(panels)
house.simulate()