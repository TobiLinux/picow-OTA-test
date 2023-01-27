import sys
from rotary_irq_rp2 import RotaryIRQ
import time
from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

r = RotaryIRQ(pin_num_clk=18,
              pin_num_dt=17,
              min_val=0,
              max_val=50,
              reverse=True,
              range_mode=RotaryIRQ.RANGE_WRAP)

led = Pin(25, Pin.OUT, value=0)
b1 = Pin(7, Pin.IN, Pin.PULL_UP)
b2 = Pin(14, Pin.IN, Pin.PULL_UP)
b3 = Pin(16, Pin.IN, Pin.PULL_UP)

def led_parpadeo():
    led.on()
    time.sleep_ms(5)
    led.off()

val_old = r.value()
lcd.putstr("I2C Address:"+str(I2C_ADDR)+"\n")
print(str(I2C_ADDR)+"\n")


counter = 10
ms_now = time.ticks_ms()
intervalo_counter = 1000

lcd.clear()
lcd.putstr('Sp:   | Cont:  ')
edicion = False

while True:
    val_new = r.value()
    if (time.ticks_ms() - ms_now >= intervalo_counter) and (not edicion):
        lcd.move_to(14,0 )
        lcd.putstr('  ')
        lcd.move_to(14,0 )
        print(str(counter))
        lcd.putstr(str(counter))
        counter = counter-1
        if counter < 0:
            counter = 10
        ms_now = time.ticks_ms()
        
    if val_old != val_new:
        val_old = val_new
        print('valor encoder =', val_new)
        lcd.move_to(3, 0)
        lcd.putstr('  ')
        lcd.move_to(3, 0)
        lcd.hide_cursor()
        lcd.putstr(str(val_new))
    if b1.value()==0:
        print('boton1 apretado')
        lcd.move_to(0, 0)   
        lcd.putstr('')
        lcd.putstr('boton 1 apretado')
        led_parpadeo()
    if b2.value()==0:
        print('boton2 apretado')
        lcd.move_to(0, 0)   
        lcd.putstr('')
        lcd.putstr('boton 2 apretado')
        led_parpadeo()
    if b3.value()==0:
        print('boton3 apretado')
        if not edicion:
            print('Modo edición de SetPoint')
            edicion = True
            lcd.move_to(3, 0)
            lcd.putstr('  ')
            lcd.move_to(3, 0)
            lcd.show_cursor()
            
        else:
            print('Modo countDown')
            lcd.move_to(14, 0)
            lcd.putstr('  ')
            lcd.move_to(14, 0)
            lcd.show_cursor()
            counter = val_new
            lcd.putstr(str(counter))
            edicion = False
        led_parpadeo()        
    time.sleep_ms(50)