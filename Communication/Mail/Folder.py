# -*- coding: utf-8 -*-

class Folder():

    def __init__(self, name="Folder", hasChildren=False):

        self.__name = name
        self.__child = []
        self.__parent = None
        self.__hasChildren = hasChildren

        #mails
        self.__mails = []

    def hasChildren(self):
        return self.__hasChildren

    def child(self):
        return self.__child

    def name(self):
        return self.__name

    def addChild(self, child):

        self.__child.append(child)

    def addMail(self, mail):

        self.__mails.append(mail)

    def __str__(self):

        return "Folder <'"+str(self.__name)+"'> with "+str(len(self.__child))+" children(s) and "+str(len(self.__mails))+" mail(s)"

def main():
        pass
    
    
if( __name__ == "__main__"):
    main()