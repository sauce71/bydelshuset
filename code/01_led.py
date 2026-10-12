import machine # Importere biblioteket med hardware funksjonalitet
import time # Importerer biblioteket med tidsfunksjonalitet


led = machine.Pin('LED', machine.Pin.OUT) # Setter pinne LED som en output pi

def blink(interval):
    led.on() # Slår led på / Setter pinnen HIGH
    time.sleep(interval) # Sover i 1.5 sekunder
    led.off() # Slår led av / Setter pinnen LOW
    time.sleep(interval) # Sover i 1.5 sekunder
    

while True: # Gjentar for alltid
    blink(0.5)