
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

