from machine import Pin
import time

pinEnabled = Pin(13, Pin.OUT)
pinStep = Pin(14, Pin.OUT)
pinDirection = Pin(15, Pin.OUT)

def steperRun(stepsPerRevolution = 48, stepIntervalMs = 2, numCiclos = 2, numVueltas = 2 ):  
    for i in range(numCiclos):
        pinEnabled.off()
        pinDirection.on()

        for i in range(0,stepsPerRevolution * numVueltas):
            pinStep.on()
            time.sleep_ms(stepIntervalMs)
            pinStep.off()
            time.sleep_ms(stepIntervalMs)

        pinDirection.off()
        time.sleep(0.5)

        for i in range(0,stepsPerRevolution * numVueltas):
            pinStep.on()
            time.sleep_ms(stepIntervalMs)
            pinStep.off()
            time.sleep_ms(stepIntervalMs)
        time.sleep(2)

    pinEnabled.on()
