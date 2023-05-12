from machine import Pin
import time

pinEnabled = Pin(5, Pin.OUT,value=0)
pinStep = Pin(14, Pin.OUT)
pinDirection = Pin(15, Pin.OUT)

stepsPerRevolution = 200
stepIntervalMs = 100 
numCiclos = 4
for i in range(numCiclos):

    pinDirection.on()

    for i in range(0,stepsPerRevolution):
        pinStep.on()
        time.sleep_ms(stepIntervalMs)
        pinStep.off()
        time.sleep_ms(stepIntervalMs)

    pinDirection.off()

    for i in range(0,stepsPerRevolution):
        pinStep.on()
        time.sleep_ms(stepIntervalMs)
        pinStep.off()
        time.sleep_ms(stepIntervalMs)    
