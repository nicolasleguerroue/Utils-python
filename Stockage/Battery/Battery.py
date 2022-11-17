import math
from Debug.Debug import Debug
class CellStatus():

    FULL = 0
    USED = 1
    DISCHARGED = 2
    STATUS = ["FULL", "USED", "DISCHARGED"]

class Cell():

    COUNTER = 1

    def __init__(self, voltage=12, maxCapacity=290):

        self.__voltage = voltage                            #Volt
        self.__maxCapacity = maxCapacity                    #Ah
        self.__maxEnergy = voltage*maxCapacity/1000         #kWh
        self.__energy = self.__maxEnergy
        self.__percent = 100
        self.__id = Cell.COUNTER
        self.__status = CellStatus.FULL
        Cell.COUNTER +=1
    
    def status(self):
        return self.__status

    def energy(self):
        return self.__energy

    def voltage(self):

        return self.__voltage

    def charge(self, energy):
        """return loss in kWh"""
        self.__energy += energy
        self.__percent = self.percent()
        losses = 0 #Kwh

        if(self.__percent<0):
            self.__status = CellStatus.DISCHARGED
        elif(self.__percent<100.0):
            self.__status = CellStatus.USED
        else:
            self.__status = CellStatus.FULL
            losses = self.__maxEnergy - self.__energy
            self.__energy = self.__maxEnergy
        return losses

        

    def discharge(self, energy):

        self.__energy -= energy
        self.__percent = self.percent()

        if(self.__percent<0):
            self.__status = CellStatus.DISCHARGED
            self.__energy = 0
            self.__percent = self.percent()
        elif(self.__percent<100.0):
            self.__status = CellStatus.USED
        else:
            self.__status = CellStatus.FULL
            self.__energy = self.__maxEnergy

    def percent(self):
        return round(self.__energy/self.__maxEnergy*100, 1)

    def id(self):
        return self.__id

    def __str__(self):
        return "<Cell_"+str(self.__id)+", "+str(self.__voltage)+"V, "+str(self.__maxCapacity)+"Ah, "+str(self.__percent)+"%>"


class Battery(Debug):

    def __init__(self, cellCount, voltage, capacity, dischargeRate=0.2):

        super().__init__()

        self.__cellCount = cellCount
        self.__cells = []
        self.__dischargeRate = dischargeRate
        self.__loses = 0

        #Append cells
        for c in range(0, cellCount):
            cell = Cell(voltage, capacity)
            self.__cells.append(cell)

    def resetLoses(self):
        self.__loses = 0
    def loses(self):
        return self.__loses
    
    def status(self):

        return "<Battery status : "+str(CellStatus.STATUS[self.__cells[0].status()])+", "+str(self.__cells[0].percent())+"%>"

    def discharge(self, discharge):
        """Discharge in kWh"""

        #self.println("Discharging battery : "+str(discharge)+" kWh")
        oneCellDischarge = discharge/self.__cellCount

        for c in self.__cells:
            c.discharge(oneCellDischarge)

    def selfDischarge(self):
        """Remove self_discharge value of energy"""
        self.discharge(self.energy()*self.__dischargeRate)

    def percent(self):
        return self.__cells[0].percent()
    def cells(self):
        return self.__cellCount
    def charge(self, charge):
        """Charge in kWh"""

        #self.println("Charging battery : "+str(charge)+" kWh")
        oneCellDischarge = charge/self.__cellCount
        losses = 0
        for c in self.__cells:
            losses += c.charge(oneCellDischarge)
            
        self.__loses += losses

        

    def battery(self):
        return self.__cells[0].percent()

    def energy(self):
        return self.__cells[0].energy()*self.__cellCount

def main():

    battery = Battery(10,12,290)
    print(battery.status())
    battery.discharge(3.4)
    print(battery.status())
    battery.charge(3.4)
    print(battery.status())
    

if(__name__ == "__main__"):
    main()