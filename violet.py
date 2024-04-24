from machine import Pin, PWM
import utime

led = [PWM(Pin(16,mode=Pin.OUT)), PWM(Pin(17,mode=Pin.OUT)), PWM(Pin(18,mode=Pin.OUT))]
led[0].freq(1_000)
led[1].freq(1_000)
led[2].freq(1_000)

#led[0].duty_u16(10000) rouge
#led[1].duty_u16(10000) vert
#led[2].duty_u16(10000) bleu

def violet(led1, led2, led3) :
    led1.freq(1_000)
    led3.freq(1_000)
    led1.duty_u16(10000)
    led3.duty_u16(10000)

#violet(led[0],led[1],led[2])

def arc_en_ciel(led1, led2, led3,freq) :
    led1.freq(1_000)
    led2.freq(1_000)
    led3.freq(1_000)
    led1.duty_u16(freq)
    for i in range (freq) :
        led2.duty_u16(i)
        utime.sleep_ms(1)
    for j in range (freq) :
        led1.duty_u16(freq - j)
        utime.sleep_ms(1)
    for k in range (freq) :
        led3.duty_u16(k)
        utime.sleep_ms(1)
    for l in range (freq) :
        led2.duty_u16(freq - l)
        utime.sleep_ms(1)
    for m in range (freq) :
        led1.duty_u16(m)
        utime.sleep_ms(1)
    
        
def eteindre (led1, led2, led3) :
    led1.duty_u16(0)
    led2.duty_u16(0)
    led3.duty_u16(0)


def set_color(r,v,b) :
    c =[r,v,b]
    for i in range (3) :
        led[i].duty_u16(c[i]*256)
        

eteindre(led[0],led[1],led[2])
arc_en_ciel(led[0],led[1],led[2],2500)
#set_color(10000,0,10000)
eteindre(led[0],led[1],led[2])
    