#!/usr/bin/python
# -*- coding: utf-8 -*-

class Debug():

    #Types
    INFO = "Info"
    ERROR = "Error"
    WARNING = "Warning"
    SUCCESS = "Success"

    def __init__(self):


         #Status
        self.__displayErrors = True
        #Colors
        self.__blueColor = '\033[94m'
        self.__greenColor = '\033[92m'
        self.__orangeColor = '\033[93m'
        self.__redColor = '\033[91m'
        self.__defaultColor = '\033[0m'
        self.__bold = '\033[1m'   

        #prompt
        self.__displayPromptError = "["+self.__redColor+"Error"+self.__defaultColor+"] >>> "
        self.__displayPromptWarning = "["+self.__orangeColor+"Warning"+self.__defaultColor+"] >>> "
        self.__displayPromptSuccess = "["+self.__greenColor+"Success"+self.__defaultColor+"] >>> "
        self.__displayPromptInfo = "["+self.__blueColor+"Info"+self.__defaultColor+"] >>> "
        self.__displayPromptInput = "["+self.__bold+"Input"+self.__defaultColor+"] >>> "

    def displayErrors(self, displayErrorStatus=True):

        self.__displayErrors = displayErrorStatus

    def println(self, message, type=INFO):

        if(not self.__displayErrors):
            return 
        if(type==Debug.INFO):
            print(self.__displayPromptInfo+message)
        elif(type==Debug.ERROR):
            print(self.__displayPromptError+message)
        elif(type==Debug.WARNING):
            print(self.__displayPromptWarning+message)
        elif(type==Debug.SUCCESS):
            print(self.__displayPromptSuccess+message)
        else:
            print(self.__displayPromptError+" Bad type format for type in Debug.println method")


def main():

    #Threads
    debug = Debug()
    debug.displayErrors(True)
    debug.println("INFO", Debug.INFO)
    debug.println("SUCCESS", Debug.SUCCESS)
    debug.println("WARNING", Debug.WARNING)
    debug.println("ERROR", Debug.ERROR)

if(__name__ == "__main__"):

    main()