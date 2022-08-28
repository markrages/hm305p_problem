#!/usr/bin/env python3

import u3_manager
import hm305
import msox3000
import time

lj = u3_manager.u3()
ps = hm305.HM305()
scope = msox3000.MSOX3000('USB0::2391::6056::MY53041304::INSTR')
scope.open()

ps.i = 5
ps.v = 10
ps.on()

def relay_on(): lj.FIO0.set()
def relay_off(): lj.FIO0.clear()

def trigger_on(): lj.FIO2.set()
def trigger_done(): lj.FIO2.clear()

def figure1():
    """ Plot load response at 10 V """
    ps.v = 10
    time.sleep(1)
    # ps.v = 8
    trigger_on()
    relay_on()
    time.sleep(1)
    relay_off()
    trigger_done()

def figure2():
    """ Plot voltage change 10V -> 8V, open circuit """
    relay_off()
    ps.v = 10
    time.sleep(1)
    trigger_on()
    ps.v = 8
    time.sleep(1)
    trigger_done()

def figure3():
    """ Plot voltage change 10V -> 8V, loaded circuit """
    relay_on()
    ps.v = 10
    time.sleep(1)
    trigger_on()
    ps.v = 8
    time.sleep(1)
    trigger_done()    
    relay_off()

def figure4():
    """ Plot voltage change 10V -> 8V, circuit loaded during transition """
    ps.v = 10
    time.sleep(1)
    trigger_on()
    ps.v = 8
    relay_on()
    time.sleep(1)
    trigger_done()    
    relay_off()    

def delay():
    time.sleep(4)
    
if __name__=="__main__":
    try:
        figure1()
        scope.hardcopy('figure1.png')

        delay()
    
        figure2()
        scope.hardcopy('figure2.png')
        
        delay()
        
        figure3()
        scope.hardcopy('figure3.png')
        
        delay()
    
        figure4()
        scope.hardcopy('figure4.png')

    finally:
        ps.off()
        
    
