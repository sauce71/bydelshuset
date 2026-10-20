import machine
import time
from bme280_float import BME280
from aht import AHT2x

# Setter opp i2c med en frekvens på 10khz
i2c = machine.I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=10000)

sensor = BME280(i2c=i2c, address=0x77) # Instans av sensoren - kortet bruker adresse 0x77/119 - det er ikke standard
sensor_aht = AHT2x(i2c, crc=False)

while True:
    #values = sensor.values # Henter alle verdiene BMP280 har ikke luftfuktighet, derfor er denne verdien 0
    values = sensor.read_compensated_data()
    altitude = sensor.altitude
    #print('Temperatur BMP', values[0], values[1])
    if sensor_aht.is_ready:
        temperature = sensor_aht.temperature
        humidity = sensor_aht.humidity
        
    avg_temp = (values[0]+temperature)/2
    
    # Bruker en f-string
    tid = time.localtime()
    ts = f'{tid[0]}-{tid[1]:02}-{tid[2]:02}T{tid[3]:02}:{tid[4]:02}:{tid[5]:02}'
    
    s = f'{ts} Temperatur: {avg_temp:.2f}C Luftfuktighet: {humidity:.2f}% Trykk: {values[1]}'
    print(s)
    
    # Skriver data til en fil
    sd = f'{ts};{avg_temp};{humidity};{values[1]}\n'
    f = open('data.csv', 'a')
    f.write(sd)
    f.close()

    time.sleep(2)