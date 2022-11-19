import math
#from Tools.Debug import Debug

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
        self.__percent = 100.0
        self.__id = Cell.COUNTER
        self.__status = CellStatus.FULL
        Cell.COUNTER +=1
    
    def getVoltage(self):
        return self.__voltage
    def setVoltage(self, voltage):
        self.__voltage = voltage

    def getMaxEnergy(self):
        return self.__maxEnergy
    
    def getCapacity(self):
        return self.__maxCapacity
    def setCapacity(self, capacity):
        self.__maxCapacity = capacity      
    
    def getStatus(self):
        return self.__status
    def setStatus(self, status):
        self.__status = status
        
    def getEnergy(self):
        return self.__energy
    def setEnergy(self, energy):
        self.__energy = energy
    
    def getPercent(self):
        #print(self.__maxEnergy)
        return round(self.__energy/self.__maxEnergy*100, 1)

    def id(self):
        return self.__id
    
    def charge(self, energy):
        """return loss in kWh"""
        self.__energy += energy
        self.__percent = self.getPercent()
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
        self.__percent = self.getPercent()

        if(self.__percent<0):
            self.__status = CellStatus.DISCHARGED
            self.__energy = 0
            self.__percent = self.getPercent()
        elif(self.__percent<100.0):
            self.__status = CellStatus.USED
        else:
            self.__status = CellStatus.FULL
            self.__energy = self.__maxEnergy

    def __str__(self):
        return "<Cell_"+str(self.__id)+", "+str(self.__voltage)+"V, "+str(self.__maxCapacity)+"Ah, "+str(self.__percent)+"%>"

class Battery():

    def __init__(self, cellCount=10, voltage=12, capacity=290, dischargeRate=0.2):

        super().__init__()

        #Common
        self.__voltage = 0
        self.__cellCount = cellCount
        self.__cells = []
        self.__dischargeRate = dischargeRate
        self.__loses = 0

        #Append cells
        for c in range(0, cellCount):
            cell = Cell(voltage, capacity)
            self.__cells.append(cell)
            
        self.__capacity = self.getCapacity()
        
    def fullCharge(self):
        for c in self.__cells:
            c.charge(c.getMaxEnergy())
            
    def __str__(self) -> str:
        return "<Battery with "+str(self.getCount())+" cells, nominal capacity of "+str(self.getCapacity())+" Ah, voltage of "+str(self.getVoltage())+" V and discharge rate of "+str(self.__dischargeRate)+">"
    
    def setDischargeRate(self, rate) -> float:
        """Setter of attribut 'setDischargeRate'"""
        self.__dischargeRate = rate

    def getPercent(self):
        return self.__cells[0].getPercent()
      
    def getCount(self):
        return self.__cellCount
    
    def setCount(self, count):
        
        self.__cellCount = count
        for c in self.__cells:
            c = Cell(self.__voltage, self.__capacity)
            
    def getCapacity(self):
        return self.__cells[0].getCapacity()
    
    def setCapacity(self, capacity):
        
        for c in self.__cells:
            c.setCapacity(capacity)
    
    def getVoltage(self):
        return self.__cells[0].getVoltage()
    
    def setVoltage(self, v):
        for c in self.__cells:
            c.setVoltage(v)
            
    def resetLoses(self):
        self.__loses = 0
    def loses(self):
        return self.__loses
    
    def status(self):

        return "<Battery status : "+str(CellStatus.STATUS[self.__cells[0].getStatus()])+", "+str(self.__cells[0].getPercent())+"%>"

    def discharge(self, discharge):
        """Discharge in kWh"""

        #self.println("Discharging battery : "+str(discharge)+" kWh")
        oneCellDischarge = discharge/self.__cellCount

        for c in self.__cells:
            c.discharge(oneCellDischarge)

    def selfDischarge(self):
        """Remove self_discharge value of energy"""
        self.discharge(self.energy()*self.__dischargeRate)


    def charge(self, charge):
        """Charge in kWh"""

        #self.println("Charging battery : "+str(charge)+" kWh")
        oneCellDischarge = charge/self.__cellCount
        losses = 0
        for c in self.__cells:
            losses += c.charge(oneCellDischarge)
            
        self.__loses += losses

        

    def battery(self):
        return self.__cells[0].getPercent()

    def energy(self):
        return self.__cells[0].getEnergy()*self.__cellCount

def main():

    battery = Battery(10,12,290)
    print(battery)
    battery.setCount(20)
    print(battery)
    battery.discharge(10)
    print(battery.status())
    battery.selfDischarge()
    print(battery.status())
    
    

if(__name__ == "__main__"):
    main()