
class CircularRing():

    def __init__(self, originalList):
        self.__originalList = originalList
        self.__size = len(self.__originalList)

    def __str__(self):
        return "<CircularRing : "+str(self.__originalList)+">"

    def size(self):
        return self.__size

    def original(self):
        return self.__originalList

    def startAtIndex(self, index):

        if(index>(len(self.__originalList)-1)):
            return None
        tmpArray = []
        tmpArray = list(self.__originalList[index:-1])
        tmpArray.append(self.__originalList[-1]) 
        tmpArray += list(self.__originalList[0:index])
        return tmpArray

