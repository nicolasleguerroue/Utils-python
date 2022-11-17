
from Debug.Debug import Debug
from Graph.Graph import Graph, GraphColor, Line
from CircularRing import CircularRing

class ConsumptionCalendar():

    def __init__(self, consumptionCalendar):
        self.__consumptionCalendar = consumptionCalendar

    def data(self):
        return self.__consumptionCalendar

    def __str__(self) -> str:
        return "<ConsumptionCalendar : Store in array used energy of house per month, a list of 12 items>"

class EnergyHandler(Debug):

    def __init__(self, battery, panels, sunCalendar, consumptionCalendar, saltPlant=None):
        
        super().__init__()

        self.__battery = battery
        self.__panels = panels
        self.__sunCalendar = CircularRing(sunCalendar.data())
        self.__saltPlant = saltPlant
        
        #energy rate
        self.__percentOHeater = 0.7
        #print(self.__sunCalendar)
        self.__consumptionCalendar = CircularRing(consumptionCalendar.data())
        #print(self.__consumptionCalendar)
        self.__daysInMonth = 30


    def simulate(self):

        fullGraph = Graph()

        for s in range(0, 12):
            sun = self.__sunCalendar.startAtIndex(s)
            consumption = self.__consumptionCalendar.startAtIndex(s)
            self.__battery.resetLoses()
            self.__saltPlant.reset()

            g1 = Graph()
            g2 = Graph()
            g3 = Graph()
            g4 = Graph()
            g5 = Graph()
            g6 = Graph()
            g7 = Graph()
            g8 = Graph()
            graph = Graph()

            tmpFile = open("Analysis.txt", "a")
            energyProduced = 0
            for m in range(0, self.__sunCalendar.size()):

                self.println("Month "+str(m+1), Debug.SUCCESS)

                consumption_day = round(consumption[m]/self.__daysInMonth,1)
                production_day = self.__panels.produceByDay(sun[m])
                tmpFile.write("Month_"+str(m)+"\n")
                tmpFile.write("<Day_consumption : "+str(consumption_day)+", ")
                tmpFile.write("Day_production : "+str(production_day)+", ")
                for d in range(0, self.__daysInMonth):

                    #Store all energy of panels
                    self.__battery.charge(production_day)
                    #Consumption of electronic device without heater
                    self.__battery.discharge(consumption_day*(1-self.__percentOHeater))
                    
                    #We can use salt to heat house as enought energy
                    if(self.__saltPlant.energy()>consumption_day*(self.__percentOHeater)):
                        #self.println("USING", Debug.SUCCESS)
                        self.__saltPlant.useEnergy(consumption_day*(self.__percentOHeater))
                    else:
                        #We take energy from battery
                        #self.println("BAD", Debug.ERROR)
                        self.__battery.discharge(consumption_day*(self.__percentOHeater))
                    tmpFile.write("<Battery : "+str(self.__battery.percent())+"\n")

                #Self discharge 
                
                self.__battery.selfDischarge()
                #self.println(self.__battery.status())
                #data of percent
                g1.appendX(m)
                g1.appendY(self.__battery.percent())
                g1.setLine(Line.LINE)
                g1.setLegend("Level of battery (%)"+" - "+str(self.__battery.cells())+" batteries")
                g1.color(GraphColor.BLUE)
                #data of consumption
                g2.appendX(m)
                g2.appendY(consumption[m])
                g2.setLine(Line.LINE)
                g2.setLegend("Consumption per month (kWh)")
                g2.color(GraphColor.PURPLE)

                g3.appendX(m)
                g3.appendY(0)
                g3.setLine(Line.ALTERNATE)
                g3.setLegend("0%")
                g3.color(GraphColor.RED)

                g4.appendX(m)
                g4.appendY(100)
                g4.setLine(Line.ALTERNATE)
                g4.setLegend("100%")
                g4.color(GraphColor.GREEN)

                g5.appendX(m)
                sun2 = [i * 25 for i in sun]
                g5.appendY(sun2[m])
                g5.setLegend("Hours of sun per month (*25 h)")
                g5.setLine(Line.LINE)
                g5.color(GraphColor.BROWN)

                g6.appendX(m)
                g6.appendY(production_day*30)
                g6.setLine(Line.LINE)
                g6.setFill(False)
                g6.setLegend("Production per month (kWh)")
                energyProduced +=production_day*30
                g6.color(GraphColor.RED)
                
                g7.appendX(m)
                g7.appendY(self.__battery.loses()/10)
                g7.setLine(Line.LINE)
                g7.setLegend("Energy no stored (10e1 kWh)")
                g7.color(GraphColor.PINK)
          
                g8.appendX(m)
                g8.appendY(self.__saltPlant.volume())
                g8.setLine(Line.LINE)
                g8.setLegend("Volume of salt (m^3)")
                g8.color(GraphColor.RED)      


            graph.clear()
            graph.appendGraph(g1.getData())
            #graph.appendGraph(g2.getData())
            #graph.appendGraph(g3.getData())
            #graph.appendGraph(g4.getData())
            #graph.appendGraph(g5.getData())
            #graph.appendGraph(g6.getData())
            #graph.appendGraph(g7.getData())
            graph.appendGraph(g8.getData())
            graph.xLabel("Months")
            graph.yLabel("Amplitude")
            graph.addText(1,1, "Energy produced (kW) : "+str(round(energyProduced,1)))
            graph.display("simulate_"+str(s)+".png")
            
            #fullGraph.appendGraph(graph.getData())
        # fullGraph.title("Energy in battery vs month (%)")
        # fullGraph.xLabel("Months")
        # fullGraph.yLabel("Energy (%)")
        # fullGraph.display("simulate.png")