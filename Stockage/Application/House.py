
from Tools.Debug import Debug
from Tools.Graph import Graph, GraphColor, Line
from Tools.CircularRing import CircularRing
from Power.SolarPlant import Panels
from Storages.Battery import Battery
from Storages.SaltPlant import SaltPlant
from Storages.HydrogenPlant import HydrogenPlant

class ConsumptionCalendar():

    def __init__(self, consumptionCalendar):
        self.__consumptionCalendar = consumptionCalendar

    def data(self):
        return self.__consumptionCalendar

    def __str__(self) -> str:
        return "<ConsumptionCalendar : Store in array used energy of house per month, a list of 12 items>"


class House(Debug):

    def __init__(self):
        
        super().__init__()

        """Constructor"""
        self.__annualEnergy = 0
        
        #Object in Storages folder
        self.__storages = []
        
        #objects in Power dir
        self.__powers = []
        
        self.__battery = None
        self.__panels = None
        self.__sunCalendar = None
        self.__saltPlant = None
        self.__hydrogenPlant = None
        
        #energy rate
        self.__percentOfHeater = 0.7
        #print(self.__sunCalendar)
        self.__consumptionCalendar = None
        #print(self.__consumptionCalendar)
        self.__daysInMonth = 30
    
    def rateHeat(self, rate):
        self.__percentOfHeater = rate
    def check(self):
        
        message = 0
        if(self.__consumptionCalendar == None):
            self.println("Veuillez ajouter un calendrier de consommation en utilisant la methode 'setConsumptionCalendar'", Debug.ERROR)
            message = "Veuillez ajouter un calendrier de consommation"
        if(self.__sunCalendar == None):
            self.println("Veuillez ajouter un calendrier de soleil en utilisant la methode 'setSunCalendar'", Debug.ERROR)
            message = "Veuillez ajouter un calendrier de soleil"
        if(self.__annualEnergy == 0):
            message = "Veuillez ajouter la consommation annuelle en kWh"
            self.println("Veuillez ajouter la consommation annuelle en kWh en utilisant la méthode 'setAnnualEnergy'", Debug.ERROR)
        
        if(len(self.__storages)==0):
            message = "Veuillez ajout un moyen de stockage"
            self.println("Veuillez ajout un moyen de stockage", Debug.ERROR)

        return message
    def setConsumptionCalendar(self, consumptionCalendar):
        
        self.__consumptionCalendar = CircularRing(consumptionCalendar.data())
        
    def setSunCalendar(self, sunCalendar):
        
        self.__sunCalendar = CircularRing(sunCalendar.data())
    
    def setAnnualEnergy(self, energy):
        """Getter of attribut 'annualEnergy'"""
        self.__annualEnergy = energy
        
    def getAnnualEnergy(self) -> int:
        """Getter of attribut 'annualEnergy'"""
        return self.__annualEnergy

    def addStorage(self, storage) -> None:
        """Setter of attribut 'storage'"""
        self.println(">>> Storage has been added : ", Debug.SUCCESS)
        self.println(str(storage))
        self.__storages.append(storage)
    
    def addPower(self, power) -> None:
        """Setter of attribut 'addPower'"""
        self.println(">>> Power has been added : ", Debug.SUCCESS)
        self.println(str(power))
        self.__powers.append(power)
        
    def clearData(self):
        self.__powers = []
        self.__storages = []
        self.__battery = None
        self.__panels = None
        self.__saltPlant = None
        self.__hydrogenPlant = None
        
    def initData(self):
        
        if(len(self.__powers)!=0):
            for p in self.__powers:
                if(type(p)==Panels):
                    self.__panels = p
                    
        if(len(self.__storages)!=0):
            for s in self.__storages:
                if(type(s)==Battery):
                    self.__battery = s
                if(type(s)==SaltPlant):
                    self.__saltPlant = s
                if(type(s)==HydrogenPlant):
                    self.__hydrogenPlant = s               
    
    def simulate(self):
        
        if(self.check()):
            return 
        self.initData()
        
        if(self.__battery):
            self.__battery.fullCharge()
        
        allGraph = []

        allGraphesBattery = []
        allGraphConsumption = []
        allGraphProduction = []
        allGraphSalt = []
        allGraphSun = []
        allGraphHydrogen = []
        
        for s in range(0, 12):
            
            sun = self.__sunCalendar.startAtIndex(s)
            consumption = self.__consumptionCalendar.startAtIndex(s)
            
            graphBatt = Graph()
            
            if(self.__battery):
                self.__battery.resetLoses()
                graphBatt.setLine(Line.LINE)
                graphBatt.setLegend("Niveau de batterie (%)"+" - "+str(self.__battery.getCount())+" batteries")
                graphBatt.color(GraphColor.BLUE)
                
            if(self.__saltPlant):
                self.__saltPlant.reset()
                
            if(self.__hydrogenPlant):
                self.__hydrogenPlant.reset()


            
            graphConsumption = Graph()
            graphConsumption.setLine(Line.LINE)
            graphConsumption.setLegend("Consommation souhaitée par mois (kWh)")
            graphConsumption.color(GraphColor.PURPLE)
            
            graphSun = Graph()
            graphSun.setLegend("Heure de soleil par jour (*25 h)")
            graphSun.setLine(Line.LINE)
            graphSun.color(GraphColor.GREEN)
            
            graphProduction = Graph()
            graphProduction.setLine(Line.LINE)
            graphProduction.setFill(False)
            graphProduction.setLegend("Production photovoltaïque par mois (kWh)")
            graphProduction.color(GraphColor.RED)       
             
            graphSalt = Graph()
            graphSalt.setLine(Line.LINE)
            graphSalt.setLegend("Niveau de sel disponible (%)")
            graphSalt.color(GraphColor.RED)      
            
            graphHydrogen = Graph()
            graphHydrogen.setLine(Line.LINE)
            graphHydrogen.setLegend("Niveau d'hydrogène (%)")
            graphHydrogen.color(GraphColor.GREEN)  


            energyProduced = 0
            energyUsed = 0
            
            for m in range(0, self.__sunCalendar.size()): #For each month

                consumption_day = round(consumption[m]/self.__daysInMonth,1)
                production_day=0
                
                if(self.__panels!=None):
                    production_day = self.__panels.produceByDay(sun[m])
                    
                for d in range(0, self.__daysInMonth):

                    #Store all energy of panels
                    
                    if(self.__battery):
                        
                        self.__battery.charge(production_day)
                        
                        #Consumption of electronic device without heater
                        if(self.__saltPlant):
                            self.__battery.discharge(consumption_day*(1-self.__percentOfHeater))
                        else:
                            self.__battery.discharge(consumption_day)
                            
                        
                    else:
                        pass
                    #We can use salt to heat house as enought energy
                    if(self.__saltPlant):
                        if(self.__saltPlant.getEnergy()>consumption_day*(self.__percentOfHeater)):
                            #self.println("USING", Debug.SUCCESS)
                            self.__saltPlant.useEnergy(consumption_day*(self.__percentOfHeater))
                        else:
                            #We take energy from battery
                            #self.println("BAD", Debug.ERROR)
                            if(self.__battery):
                                self.__battery.discharge(consumption_day*(self.__percentOfHeater))

                #Self discharge 
                if(self.__battery):
                    self.__battery.selfDischarge()
                    graphBatt.appendX(m)
                    graphBatt.appendY(self.__battery.getPercent())
                    #data of consumption
                    
                    
                if(self.__hydrogenPlant):
                    self.__hydrogenPlant.produceEnergy(-self.__battery.loses())
                    graphHydrogen.appendX(m)
                    graphHydrogen.appendY(self.__hydrogenPlant.getPercent())
                    self.__battery.resetLoses()
                    
                graphConsumption.appendX(m)
                graphConsumption.appendY(consumption[m])

                graphSun.appendX(m)
                sun2 = [i * 25 for i in sun]
                graphSun.appendY(sun2[m])

                graphProduction.appendX(m)
                graphProduction.appendY(production_day*30)
                energyProduced +=production_day*30

                if(self.__saltPlant):
                    graphSalt.appendX(m)
                    graphSalt.appendY(self.__saltPlant.getPercent())

           
            allGraphesBattery.append(graphBatt)
            allGraphConsumption.append(graphConsumption)
            allGraphProduction.append(graphProduction)
            allGraphSun.append(graphSun)
            allGraphSalt.append(graphSalt)
            allGraphHydrogen.append(graphHydrogen)
           
        allGraph.append(allGraphesBattery)
        allGraph.append(allGraphProduction)
        allGraph.append(allGraphSalt)
        allGraph.append(allGraphSun)
        allGraph.append(allGraphConsumption)
        allGraph.append(allGraphHydrogen)
        
        return allGraph
