from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import utime # importe dans le code la lib qui permet de gerer le temps

pwm_led = PWM(Pin(1,mode=Pin.OUT)) # on prescise au programme que la pin 1 est une sortie de type PWN
pwm_led.freq(1_000) # dont la frequence est de 1000 (default)
utime.sleep(2)   # attendre 1 seconde 
# pwm_led.duty_u16(100) # on lui donne une valeur comprise entre 0  et 65535 qui est converti entre 0 et 3.3v
# utime.sleep(2)   # attendre 1 seconde
# pwm_led.duty_u16(40000) # on lui donne une valeur comprise entre 0  et 65535 qui est converti entre 0 et 3.3v

for i in range(30000) :
    pwm_led.duty_u16(i)
    utime.sleep_ms(10)

for j in range(30000) :
    pwm_led.duty_u16(30000 - j)
    utime.sleep_ms(10)
