from machine import Pin, PWM
import utime

led = [PWM(Pin(16,mode=Pin.OUT)), PWM(Pin(17,mode=Pin.OUT)), PWM(Pin(18,mode=Pin.OUT))]
for i in range (3) :
    led[i].freq(1_000)
    led[i].duty_u16(0)

def set_color(c) :
    for i in range (3) :
        led[i].duty_u16(c[i]*64)

def eteindre (led1, led2, led3) :
    for i in range (3) :
        led[i].duty_u16(0)



maison = {
    'Gryffindor':  [0,0,255],
    'Hufflepuff': [0,200,200],
    'Ravenclaw': [255,0,0],
    'Slytherin': [0,255,0],
    '': [255,255,255],
    None:[255,255,255]
    }

import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = ''
password = ''
wlan.connect(ssid, password) # connecte la raspi au réseau
url = ""


while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        print(r.json()) # traite sa reponse en Json
        if r.json()['house'] == "Gryffindor" :
            set_color(maison["Gryffindor"])
            utime.sleep_ms(500)
        if r.json()['house'] == "Hufflepuff" :
            set_color(maison["Hufflepuff"])
            utime.sleep_ms(500)
        if r.json()['house'] == "Ravenclaw" :
            set_color(maison["Ravenclaw"])
            utime.sleep_ms(500)
        if r.json()['house'] == "Slytherin" :
            set_color(maison["Slytherin"])
            utime.sleep_ms(500)
        eteindre(led[0],led[1],led[2])
        r.close() # ferme la demande
        utime.sleep(1)  
    except Exception as e:
        print(e)

