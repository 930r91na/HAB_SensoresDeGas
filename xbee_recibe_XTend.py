# -- coding: utf-8 --
"""
Created on Fri Apr 29 18:42:55 2022

@author: hallo
"""

#   PROGRAMA PARA EL END - DEVICE (Recibe)



import serial 

# el ord recibe un carácter y regresa un entero unicode (ascii)
# Desde el "ord" #9 inicia el mensaje, hasta tamanio

xbee=serial.Serial("/dev/ttyUSB0", 9600)

while True:
    
    inicio = ord(xbee.read()) 
    length1 = ord(xbee.read())
    length2 = ord(xbee.read())
   
    #hasta aqui recuperamos los primeros 3 bytes
   
    tamanio = length2 + 4 #longitud de toda la trama; 13, mensje = hola, este numero puede cambiar
    
    basura = []    

    for i in range(5): # este numero puede cambiar, va desde frame type hasta options
        
        p = ord(xbee.read())
        basura.append(p)
       
    #Hasta aqui recuperamos los siguientes 5 bytes de la trama, en total llevamos 8 bytes recuperados    
    restante = (tamanio - 8) -1 #tamanio del mensaje; el tamaño total menos los bytes que ya vienen predefinidos por la trama, tambien cambia el primer numeros
    # en restante se resta el tamaño total de la trama, menos los primeros bytes fijos (frame type hasta options) y se le vuelve a restar psara obtener el tamaño total del mensaje
    
    # aqui empezamos a recuperar el mensaje, que son desde el byte 8 hasta "restante" (tamanio del mensaje)
    
    trama_msj = []
    
    for j in range(restante):

        r = ord(xbee.read())
        trama_msj.append(r)
        
    # Se agregó a "trama_msj" cada caracter del mensaje enviado en formato "unicode"
    
    # Ahora convertiremos el mensaje a carater
    
    caracter = ""
    
    for l in trama_msj:
        
        caracter = caracter + chr(l)
        
    
    mensaje = str(caracter)
    
    
    
    print(mensaje)
    
    #es importante incluir la ultima parte de la trama para que la trama se reinicie correctamente
    chsk = ord(xbee.read()) #ultima parte de la trama

xbee.close()