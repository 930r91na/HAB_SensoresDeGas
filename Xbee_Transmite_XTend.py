# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:42:55 2022

@author: hallo
"""

#   PROGRAMA PARA EL COORDINADOR

import serial


#CODIGO DE SENSORES














#Aqui introducimos el mensaje

mensaje = "hola"

#Aqui van los datos fijos

direcciones = {'HAB':[0x16,0x5B]}
inicio = 0x7E #Start delimiter
Cadena1 = [0x01,0x01] # Frame type + Frame ID
Cadena2 = 0x00 #Options
n = 'HAB'
mac = direcciones[n]

#Aqui va la longitud

Tamanio = len(mensaje)+ 8 #El # de letras del mensaje + 8 espacios que suma de start delimiter hasta options
Lenght1 = int(Tamanio/255)
Lenght2 = (Tamanio%255)-3

#Aqui vamos a calcular el checksum
m = list(mensaje)

m1 = []

for i in m:
            
    m1.append(ord(i))

mac.append(Cadena2) # 16 - bit address + Options
#Aqui juntamos las cadenas y las sumamos.

f1 = Cadena1+mac+m1 #Frame type + Frme ID + 16 - bit address + Options + msj

chksm = 0 #Iniciamos la variable del cheksum en 0

for h in f1:
    chksm = chksm+h
    
chksm &= 0xFF
chksm = 0xFF - chksm

#print(inicio)
#print(Lenght1)
#print(Lenght2)
#print(f1)
#print(chksm)

Final = [inicio,Lenght1,Lenght2]+f1+[chksm]
print(Final)

xbee = serial.Serial("/dev/ttyUSB0", 9600)

for w in Final:
    r = w.to_bytes(1,'big')
    xbee.write(r)
    print(r)

xbee.close()
