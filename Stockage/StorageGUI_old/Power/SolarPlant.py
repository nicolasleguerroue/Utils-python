import math

from Tools.Debug import Debug

class SunCalendar():

    def __init__(self, sunCalendar):
        self.__sunCalendar = sunCalendar

    def data(self):
        return self.__sunCalendar

    def __str__(self) -> str:
        return "<SunCalendar : Store in array number of sun hours per month, a list of 12 items>"

class Panels(Debug):

    def __init__(self, power_cret=250, area=65, unitArea=1.608): #W, m^2, m^2

        super().__init__()

        self.__power = power_cret/1000      #kW
        self.__area = area
        self.__countPanel = math.ceil(self.__area/unitArea)
        self.__maxPower = self.__countPanel*self.__power  #kW
        self.println("Power of panels : "+str(self.__maxPower)+" kW")
        self.__ratePower = 0.7

    def power(self):
        return self.__maxPower

    def produceByDay(self, nbHourOfSun): #kWh
        return  self.__maxPower*nbHourOfSun*self.__ratePower
        
def main():

    solar = Panels(power_cret=250, area=65, unitArea=1.608)
    print(solar)

if(__name__ == "__main__"):
    main()

