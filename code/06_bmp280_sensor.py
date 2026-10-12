import machine
import time
from bme280_float import BME280

# Setter opp i2c med en frekvens på 10khz
i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17))

sensor = BME280(i2c=i2c, address=119) # Instans av sensoren - kortet bruker adresse 0x77/119 - det er ikke standard

while True:
    values = sensor.values # Henter alle verdiene BMP280 har ikke luftfuktighet, derfor er denne verdien 0
    #print(values)
    temp = values[0]
    pressure = values[1]
    altitude = sensor.altitude
    s = f'Høyde: {altitude:.2f} Temperatur: {temp} Lufttrykk: {pressure}'
    print(s)
    time.sleep(2)
