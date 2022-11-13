#!/usr/bin/env python3
#-- coding: utf-8 --

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import time
from time import time_ns
from ctypes import byref, c_byte, c_int16, c_int32, sizeof

from .AWG import AWG
from .Channel import Channel



import matplotlib.pyplot as plt
import numpy as np

from picosdk.ps2000 import ps2000
from picosdk.functions import assert_pico2000_ok, adc2mV
from picosdk.PicoDeviceEnums import picoEnum




class PicoscopeHandler():

    def __init__(self):

        print("Init Picoscope Handler")

        #self.__picoscope = ps2000.open_unit()
        #print(type(self.__picoscope))
        print("Found the following picoscope : ")

        self.__picoscope = ps2000.open_unit()
        self.info()


    def info(self):

        print('Device info: {}'.format(self.__picoscope.info))


    def addChannel(self, channel):

        assert type(channel) is Channel

        res = ps2000.ps2000_set_channel(
                self.__picoscope.handle,
                ps2000.PICO_CHANNEL['A'],
                channel.enabled(),
                ps2000.PICO_COUPLING['DC'],
                ps2000.PS2000_VOLTAGE_RANGE['PS2000_500MV'],
        )
        assert_pico2000_ok(res)
        return res

        # channelRange = self.__picoscope.setChannel(channel.name() , channel.coupling(), VRange=5.0, VOffset=0.0, enabled=channel.enabled(), BWLimited=channel.BWLimited(), probeAttenuation=1.0)
        # return 0

    def setResolution(self, timeBetweenTwoValues, acquiringTime):
        """Max samples is 4096, if samples > 4096, new samples is 4096"""

        time = 0
        computedSamples = acquiringTime/timeBetweenTwoValues
        if(computedSamples <= 3968.0):
            time = timeBetweenTwoValues
            print("time<")
        else: 
            print("time>")
            time = acquiringTime / 3968.0
        print(time)
        print("Time between value = "+str(time))

        res = self.__picoscope.setSamplingFrequency(2000, 4096)
        sampleRate = res[0]
        print("Sampling @ %f MHz, %d samples" % (res[0] / 1E3, res[1]))
        #(self.__samplingInterval, self.__samplesCount, self.__maxSamples)  = self.__picoscope.setSamplingInterval(time, acquiringTime)

        #print("Resolution = %f s" % self.__samplingInterval)
        #print("Taking %d samples " % self.__samplesCount)

        return 100

    def setAWG(self, Awg):

        assert type(Awg) is AWG

        self.__picoscope.setSigGenBuiltInSimple(offsetVoltage=Awg.offset(), pkToPk=Awg.amplitude(), waveType=Awg.waveType(), frequency=Awg.frequency())

    def setAcquiringTIme(self, time):

        self.__acquiringTime = time

    def get_timebase(self, wanted_time_interval):

        current_timebase = 1

        old_time_interval = None
        time_interval = c_int32(0)
        time_units = c_int16()
        max_samples = c_int32()

        while ps2000.ps2000_get_timebase(
            self.__picoscope.handle,
            current_timebase,
            2000,
            byref(time_interval),
            byref(time_units),
            1,
            byref(max_samples)) == 0 \
            or time_interval.value < wanted_time_interval:

            current_timebase += 1
            old_time_interval = time_interval.value

            if current_timebase.bit_length() > sizeof(c_int16) * 8:
                raise Exception('No appropriate timebase was identifiable')

        return current_timebase - 1, old_time_interval


    def startReading(self, duration_ms):

        timebase_a, interval = self.get_timebase(duration_ms)

        collection_time = c_int32()

        res = ps2000.ps2000_run_block(
        self.__picoscope.handle,
        2000,
        timebase_a,
        OVERSAMPLING,
        byref(collection_time)
        )
        assert_pico2000_ok(res)

        while ps2000.ps2000_ready(self.__picoscope.handle) == 0:
            time.sleep(0.1)

        times = (c_int32 * SAMPLES)()

        buffer_a = (c_int16 * SAMPLES)()
        buffer_b = (c_int16 * SAMPLES)()

        overflow = c_byte(0)

        res = ps2000.ps2000_get_times_and_values(
        self.__picoscope.handle,
        byref(times),
        byref(buffer_a),
        byref(buffer_b),
        None,
        None,
        byref(overflow),
        2,
        SAMPLES,
        )
        assert_pico2000_ok(res)

        channel_a_overflow = (overflow.value & 0b0000_0001) != 0
        # res = ps2000.ps2000_run_block(
        #     device.handle,
        #     SAMPLES,
        #     timebase_a,
        #     OVERSAMPLING,
        #     byref(collection_time)
        # )
        ps2000.ps2000_stop(self.__picoscope.handle)

        channel_a_mv = adc2mV(buffer_a, ps2000.PS2000_VOLTAGE_RANGE['PS2000_500MV'], c_int16(32767))
        #channel_b_mv = adc2mV(buffer_b, ps2000.PS2000_VOLTAGE_RANGE['PS2000_50MV'], c_int16(32767))

        fig, ax = plt.subplots()
        ax.set_xlabel('time/ms')
        ax.set_ylabel('voltage/mV')
        ax.plot(list(map(lambda x: x * 1e-6, times[:])), channel_a_mv[:])
        #ax.plot(list(map(lambda x: x * 1e-6, times[:])), channel_b_mv[:])

        if channel_a_overflow:
            ax.text(0.01, 0.01, 'Overflow present', color='red', transform=ax.transAxes)

        plt.show()
        return 0

if __name__ == "__main__":



    SAMPLES = 3000
    OVERSAMPLING = 1

    pico = PicoscopeHandler()

    channel = Channel("A", "DC")
    awg = AWG(waveType="Square", amplitude=1, offsetVoltage=0, frequency=1000)

    pico.addChannel(channel)
    pico.startReading(2000)
    
    #samples = pico.setResolution(0.001, 0.05)
    #pico.setAWG(awg)
