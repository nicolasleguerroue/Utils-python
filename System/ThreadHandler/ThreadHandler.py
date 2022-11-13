#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import threading


class ThreadHandlerMode:

    PERIODIC = 0x01
    SINGLE = 0x02


class ThreadHandler (threading.Thread):

    def __init__(self, threadID, threadName):

        threading.Thread.__init__(self)

        self.__args = []
        self.__callback = None
        self.__mode = ThreadHandlerMode.SINGLE
        self.__timerDuration = 1.0

        self.threadID = threadID
        self.threadName = threadName

        # #Args
        # self.arg1 = data
        # self.arg2 = data_x

    def setArgs(self, listArgs):

        self.__args = listArgs

    def setCallback(self, callback):

        self.__callback = callback

    def setMode(self, mode):

        self.__mode = mode

    def setDuration(self, time):

        self.__timerDuration = time
    """!
    @return
    """
    def run(self):

        #print("Starting " + self.threadName+"\n")

        if(self.__mode == ThreadHandlerMode.PERIODIC):
            while 1:

                if(len(self.__args)>=1):
                    self.__callback(self.__args)
                else:
                    self.__callback()

                time.sleep(self.__timerDuration)

        elif(self.__mode == ThreadHandlerMode.SINGLE):

            if(len(self.__args)>=1):
                self.__callback(self.__args)
            else:
                self.__callback()


def callback_1():
	pass

def callback_2(args):
	print(">>> "+str(args[0]))
	print(">>> "+str(args[1]))
	print(">>> "+str(args[2]))
	pass


def main():

	#Threads
	myThread_1 = ThreadHandler(0,"Thread-1")
	myThread_1.setCallback(callback_1)
	myThread_1.setDuration(1.0)
	myThread_1.setMode(ThreadHandlerMode.PERIODIC)
	myThread_1.start()

	myThread_2 = ThreadHandler(1,"Thread-2")
	myThread_2.setCallback(callback_2)
	myThread_2.setArgs([1,2,3])
	myThread_2.setDuration(5.0)
	myThread_2.setMode(ThreadHandlerMode.PERIODIC)
	myThread_2.start()
	while(1):
		pass

if(__name__ == "__main__"):

    main()