from machine import Pin, PWM
import time

led = [PWM(Pin(16,mode=Pin.OUT)), PWM(Pin(17,mode=Pin.OUT)), PWM(Pin(18,mode=Pin.OUT))]

def eteindre (led1, led2, led3) :
    led1.duty_u16(0)
    led2.duty_u16(0)
    led3.duty_u16(0)


eteindre(led[0],led[1],led[2])