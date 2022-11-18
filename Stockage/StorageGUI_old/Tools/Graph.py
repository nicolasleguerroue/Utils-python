import matplotlib.pyplot as plt

class GraphColor():

    COLORS = ["green", "blue", "red", "purple", "black", "brown", "pink"]
    GREEN = COLORS[0]
    BLUE = COLORS[1]
    RED = COLORS[2]
    PURPLE = COLORS[3]
    BLACK = COLORS[4]
    BROWN = COLORS[5]
    PINK = COLORS[6]


class Line():

    DOT = "."
    LINE = '-'
    BIG_LINE = '--' 
    ALTERNATE = '-.'
    DOUBLE = ':'

class Graph():

    def __init__(self):

        self.__x = []
        self.__y = []
        self.__title = "Title"
        self.__color = GraphColor.COLORS[0]
        #plt.figure()
        self.__subGraph = []
        self.__line = Line.LINE
        self.__label = "Default"
        self.__filled = False
        #self.__f = plt.figure()

    def setLegend(self, label):

        self.__label = label
        
    def getData(self):
        return [self.__x, self.__y, self.__title, self.__color, self.__line, self.__label, self.__filled]

    def appendGraph(self, graphResult):
        self.__subGraph.append(graphResult)
    def appendX(self, x):
        self.__x.append(x)

    def appendY(self, y):
        self.__y.append(y)

    def color(self, color=GraphColor.COLORS[0]):
        self.__color = color

    def title(self, title):

        self.__title = title
        plt.title(self.__title)

    def xLabel(self, xlabel):

        plt.xlabel(xlabel)

    def yLabel(self, ylabel):

        plt.ylabel(ylabel)

    def setLine(self, line):

        self.__line = line

    def setFill(self, filled=True):
        self.__filled = filled
    def clear(self):

        self.__subGraph = []
        plt.clf()

    def display(self, filename=""):

        plt.grid(color='black', linestyle='--', linewidth=0.25)
        if(len(self.__subGraph)==0):
            #plt.fill()
            if(self.__filled):
                plt.fill(self.__x, self.__y, c=self.__color, ls=self.__line, lw=0.75)
            else:
                plt.plot(self.__x, self.__y, c=self.__color, ls=self.__line, lw=0.75)
        else:
            for s in self.__subGraph:
                #plt.fill()
                if(s[6]):
                    plt.fill(s[0], s[1], c=s[3], ls=s[4], lw=0.75, label=s[5])
                else:
                    plt.plot(s[0], s[1], c=s[3], ls=s[4], lw=0.75, label=s[5])

        plt.legend(loc="upper right")
        if(filename!=""):
            plt.savefig(filename)
        #plt.close(self.__f)

    def addText(self, x, y, text):
        
        plt.text(x,y, text)

def main():

    g1 = Graph()
    g1.appendX(1)
    g1.appendX(2)
    g1.appendX(3)
    g1.appendY(2)
    g1.appendY(2)
    g1.appendY(2)
    #g1.display()

    g2 = Graph()
    g2.appendX(1)
    g2.appendX(2)
    g2.appendX(3)
    g2.appendY(-2)
    g2.appendY(-2)
    g2.appendY(-2)

    g = Graph()
    g.appendGraph(g1.getData())
    g.appendGraph(g2.getData())
    g.display()
    #g2.display()


if(__name__ == "__main__"):

    main()
