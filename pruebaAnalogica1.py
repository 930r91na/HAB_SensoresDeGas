import RPi.GPIO as GPIO
import time

# Configuración de los pines
MQ7_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(MQ7_PIN, GPIO.IN)

# Función para leer el sensor MQ-7
def read_MQ7():
    sensorValue = 0
    for i in range(10):
        sensorValue += GPIO.input(MQ7_PIN)
        time.sleep(0.1)
    return sensorValue

# Bucle principal
while True:
    sensorValue = read_MQ7()
    print("Valor del sensor:", sensorValue)
    time.sleep(1)

# Limpieza de los pines
GPIO.cleanup()
