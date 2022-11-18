import math


from Tools.Debug import Debug

class SaltPlantStatus():

    FULL = 0
    USED = 1
    DISCHARGED = 2
    STATUS = ["FULL", "USED", "DISCHARGED"]


class SaltPlant(Debug):
    #10 m^3 = 3000kWh
    
    def __init__(self, volume=10, energyPerMCube=300): #m^2, kWh

        super().__init__()

        self.__volume = volume
        self.__energy = volume*energyPerMCube
        self.__maxEnergy = self.__energy
        self.__status = SaltPlantStatus.FULL
        self.println("Energy stored by salt : "+str(self.__energy)+" kW")

    def energy(self):

        return self.__energy
    
    def useEnergy(self, energy):
        """If enougth energy, return energy"""
        
        startEnergy = self.__energy
        returnEnergy = energy
        
        self.__energy -= energy

        if(self.__energy<0):
            self.__status = SaltPlantStatus.DISCHARGED
            returnEnergy = startEnergy
        elif(self.__energy<self.__maxEnergy):
            self.__status = SaltPlantStatus.USED
        else:
            self.__status = SaltPlantStatus.FULL
            self.__energy = self.__maxEnergy     
            
        return returnEnergy
    
    def volume(self):
        
        return self.__volume
    
    def reset(self):
        self.__energy = self.__maxEnergy
    def __str__(self):
        return "<SaltPlant object, volume="+str(self.__volume)+">"   
    
def main():

    salt = SaltPlant(volume=10, energyPerMCube=300)
    print(salt)

if(__name__ == "__main__"):
    main()

