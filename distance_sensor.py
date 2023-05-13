from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(trigger=23, echo=24)

while True:
    print(sensor.distance)
    sleep(1)