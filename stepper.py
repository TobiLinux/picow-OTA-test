from machine import Pin
import time

pinEnabled = Pin(13, Pin.OUT,value=0)
pinStep = Pin(14, Pin.OUT)
pinDirection = Pin(15, Pin.OUT)

stepsPerRevolution = 51
stepIntervalMs = 5 
numCiclos = 4
for i in range(numCiclos):

    pinDirection.on()

    for i in range(0,stepsPerRevolution):
        pinStep.on()
        time.sleep_ms(stepIntervalMs)
        pinStep.off()
        time.sleep_ms(stepIntervalMs)

    pinDirection.off()
    time.sleep(2)

    for i in range(0,stepsPerRevolution):
        pinStep.on()
        time.sleep_ms(stepIntervalMs)
        pinStep.off()
        time.sleep_ms(stepIntervalMs)
    time.sleep(2)

pinEnabled.on()
