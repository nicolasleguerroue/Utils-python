
class HydrogenPlant:
    """Class HydrogenPlant"""
    
    def __init__(self):
        """Constructor"""
        self.__pressure = 700 #Bar
        self.__maxVolume = 20 #Max volume
        
        self.__volume = 0
        self.__energy = 0
        self.__maxEnergy = 0
        self.setMaxEnergy()
        
    def setMaxVolume(self, volume):
        self.__maxVolume = volume
        
        self.setMaxEnergy()
        
    def setPressure(self, pressure):
        self.__pressure = pressure
        
        self.setMaxEnergy()
            
    def setMaxEnergy(self):
        
        if(self.__pressure==700):
            self.__maxEnergy = self.__maxVolume*42*33
        elif(self.__pressure==500):
            self.__maxEnergy = self.__maxVolume*42*22
        elif(self.__pressure==300):
            self.__maxEnergy = self.__maxVolume*42*15
        else:
            self.__maxEnergy 
            
        print(self.__maxEnergy)
        
    def getEnergy(self):
        return self.__energy
    
    def getVolume(self):
        return self.__volume
    
    def getPressure(self):
        return self.__pressure
    
    def reset(self):
        self.__energy = 0
    
    def produceEnergy(self, energyInkWh):
        
        newMass = (energyInkWh)/70
        print(newMass)
        if(self.__pressure==700):
            print("700 bars")
            self.__energy  += newMass*33
        elif(self.__pressure==500):
            self.__energy += newMass*22
        elif(self.__pressure==300):
            self.__energy += newMass*15
        else:
            self.__energy +=0
            
        if(self.__energy>self.__maxEnergy):
            self.__energy = self.__maxEnergy
        else:
            pass    
        
    def useEnergy(self, energy):
        if(energy <= self.__energy):
            self.__energy -= energy
            return self.__energy
        else:
            if(self.__energy>0):
                tmpEnergy = self.__energy
                self.__energy = 0
                return tmpEnergy
            else:
                return 0
            

    def getPercent(self):
        
        return self.__energy/self.__maxEnergy*100

def main():
    
    hydro = HydrogenPlant()
    hydro.setMaxVolume(20)
    hydro.setPressure(700)
    
    hydro.produceEnergy(70*42)
    print(hydro.getEnergy())
    

    
    
    
if(__name__ == "__main__"):
    main()