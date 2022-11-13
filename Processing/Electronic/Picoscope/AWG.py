#!/usr/bin/env python3
#-- coding: utf-8 --

class AWG():

    def __init__(self, waveType="Sine", amplitude=1.0, offsetVoltage=0.0, frequency = 1e3):

        self.__waveType = waveType
        self.__amplitude = amplitude
        self.__offsetVoltage = offsetVoltage
        self.__frequency = frequency


    def waveType(self):
        return self.__waveType

    def amplitude(self):
        return self.__amplitude

    def offset(self):
        return self.__offsetVoltage

    def frequency(self):
        return self.__frequency