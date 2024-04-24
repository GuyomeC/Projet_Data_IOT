# import utime
# 
# print("ok")
# utime.sleep(1)
# print("delay de 1")

from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps

pinNumber3 = 9# declaration d'une variable pinNumber à 17
led3 = Pin(pinNumber3, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17 
                                   #et on prescise que c'est une pin de sortie de courant (OUT)
pinNumber1 = 1 # declaration d'une variable pinNumber à 17
led1 = Pin(pinNumber1, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17 
                                   #et on prescise que c'est une pin de sortie de courant (OUT)
pinNumber2 = 28 # declaration d'une variable pinNumber à 17
led2 = Pin(pinNumber2, mode=Pin.OUT) # declaration d'une variable de type pin ici la 17 
                                   #et on prescise que c'est une pin de sortie de courant (OUT)

leds = [1,28,9]
pinled = []

for i in leds :
    pinled.append(Pin(i, mode=Pin.OUT))

led1.off()
led2.off()
led3.off()

# while True:          # boucle infini
#     
#     led1.toggle()     # change l'etat de la led
#     utime.sleep_ms(150)   # attendre 1 seconde
#     led1.toggle()     # change l'etat de la led
#     
#     led2.toggle()
#     utime.sleep_ms(150)   # attendre 1 seconde
#     led2.toggle()
#     
#     led3.toggle()
#     utime.sleep_ms(150)   # attendre 1 seconde
#     led3.toggle()
    
    #led.on()        allume la led 
    #led.off()       eteind la led 