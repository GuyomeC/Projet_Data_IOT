from machine import Pin, ADC # importe dans le code la lib qui permet de gerer les Pin de sortie et de reception de signaux analogique
import time # importe dans le code la lib qui permet de gerer le temps

from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal

pwm_led = PWM(Pin(1,mode=Pin.OUT)) # on prescise au programme que la pin 1 est une sortie de type PWN
pwm_led.freq(1_000) # dont la frequence est de 1000 (default)



adc = ADC(Pin(26, mode=Pin.IN)) # on prescise au programme que la pin 26 est une entré de type ADC

while True:# boucle infini
    val = adc.read_u16() # elle lit la valeur converti entre 0 et 65535 
    #val = val * (10 / 65535) # produit en crois pour retrouver le voltage
    pwm_led.duty_u16(val)
    print(int(val)) # ecrire la valeur de val en arrondisant à l'entier
    time.sleep_ms(100) # attendre 100ms => 0.1 seconde