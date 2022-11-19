
class HydrogenPlant:
    """Class HydrogenPlant"""
    
    def __init__(self):
        """Constructor"""
        self.__pressure = 50 #Bar
        self.__maxVolume = 20 #Max volume
        #538000 m^ (46 et 76 bar)=> 2860 MWh, 1 Kg d'hydro, il faut 70 kWh pour produire , rho=
        
    def getPressure(self):
        return self.__pressure
    
    def setPressure(self, pressure):
        self.__pressure = pressure
        
    def produceHydrogen(self, energy): #
        pass