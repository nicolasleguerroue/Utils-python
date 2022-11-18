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
        self.__unitArea = unitArea
        
        self.update()
    def __str__(self):
        return "<Panel "+str(self.__power)+">"
    
    def update(self):
        
        self.__countPanel = math.ceil(self.__area/self.__unitArea)
        self.__maxPower = self.__countPanel*self.__power  #kW
        
        self.__ratePower = 0.7

    def setArea(self, area) -> float:
        """Setter of attribut 'area'"""
        assert type(area) is float
        self.__area = area
        self.update()
        
    def getArea(self):
        """Getter of attribut 'area'"""
        return self.__area

    def setUnitArea(self, unitArea) -> float:
        """Setter of attribut 'unitArea'"""
    
        assert type(unitArea) is float
        self.__unitArea = unitArea
        self.update()
    
    def getUnitArea(self) -> float:
        """Getter of attribut 'unitArea'"""
        return self.__unitArea
    
    def setPower(self, power):
        """Setter of attribut 'power'"""
        self.__power = power
        self.update()
        
    def getPower(self):
        return self.__power

    def produceByDay(self, nbHourOfSun): #kWh
        self.update()
        return  self.__maxPower*nbHourOfSun*self.__ratePower
        
def main():

    solar = Panels(power_cret=250, area=65, unitArea=1.608)
    print(solar)

if(__name__ == "__main__"):
    main()

