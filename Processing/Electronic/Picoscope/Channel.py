#!/usr/bin/env python3
#-- coding: utf-8 --

class Channel():

    countChannel = 0

    def __init__(self, name="A", coupling="DC", enabled=True, BWLimited=0, probeAttenuation=1.0):

        self.__name = name
        self.__coupling = coupling
        self.__enabled = enabled
        self.__BWLimited = BWLimited
        self.__probeAttenuation = probeAttenuation

    def name(self):
        return self.__name
    
    def coupling(self):
        return self.__coupling

    def enabled(self):
        return self.__enabled

    def BWLimited(self):
        return self.__BWLimited

    def probeAttenuation(self):
        return self.__probeAttenuation