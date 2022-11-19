
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
        
        for s in range(0, 12):
            sun = self.__sunCalendar.startAtIndex(s)
            consumption = self.__consumptionCalendar.startAtIndex(s)
            
            if(self.__battery):
                self.__battery.resetLoses()
            if(self.__saltPlant):
                self.__saltPlant.reset()

            g1 = Graph()
            g2 = Graph()
            g5 = Graph()
            g6 = Graph()
            g8 = Graph()

            energyProduced = 0
            for m in range(0, self.__sunCalendar.size()):

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
                    #We can use salt to heat house as enought energy
                    if(self.__saltPlant):
                        if(self.__saltPlant.energy()>consumption_day*(self.__percentOfHeater)):
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
                    g1.appendX(m)
                    g1.appendY(self.__battery.getPercent())
                    g1.setLine(Line.LINE)
                    g1.setLegend("Niveau de batterie (%)"+" - "+str(self.__battery.getCount())+" batteries")
                    g1.color(GraphColor.BLUE)
                    #data of consumption
                    
                g2.appendX(m)
                g2.appendY(consumption[m])
                g2.setLine(Line.LINE)
                g2.setLegend("Consommation souhaitée par mois (kWh)")
                g2.color(GraphColor.PURPLE)

                g5.appendX(m)
                sun2 = [i * 25 for i in sun]
                g5.appendY(sun2[m])
                g5.setLegend("Heure de soleil par jour (*25 h)")
                g5.setLine(Line.LINE)
                g5.color(GraphColor.BROWN)

                g6.appendX(m)
                g6.appendY(production_day*30)
                g6.setLine(Line.LINE)
                g6.setFill(False)
                g6.setLegend("Production photovoltaïque par mois (kWh)")
                energyProduced +=production_day*30
                g6.color(GraphColor.RED)

                if(self.__saltPlant):
                    g8.appendX(m)
                    g8.appendY(self.__saltPlant.getPercent())
                    g8.setLine(Line.LINE)
                    g8.setLegend("Niveau de sel disponible (%)")
                    g8.color(GraphColor.RED)      
           
            allGraphesBattery.append(g1)
            allGraphConsumption.append(g2)
            allGraphProduction.append(g6)
            allGraphSun.append(g5)
            allGraphSalt.append(g8)
           
        allGraph.append(allGraphesBattery)
        allGraph.append(allGraphProduction)
        allGraph.append(allGraphSalt)
        allGraph.append(allGraphSun)
        allGraph.append(allGraphConsumption)
        
        return allGraph
            #fullGraph.appendGraph(graph.getData())
        # fullGraph.title("Energy in battery vs month (%)")
        # fullGraph.xLabel("Months")
        # fullGraph.yLabel("Energy (%)")
        # fullGraph.display("simulate.png")