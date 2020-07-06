#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:05:58 2020

@author: Beto
"""
import numpy as np
from scipy import stats
from scipy import signal
from scipy import integrate 
import matplotlib.pyplot as plt
import pandas as pd

print("********************* Primer ejercicio********************************")
datos=pd.read_csv('bits10k.csv', header=-1)
bits=pd.DataFrame(datos)

#Numero de bits
N = len(bits)

#Lo que sirve 

#Frecuencia  de operacion
f= 5000 #hz 1ms

#Duracion del periodo de cada simbolo(onda)
T=1/f

#Numero de puntos de muestreo por periodo
p= 100


#Puntos de muestreo para cada periodo
tp= np.linspace(0,T,p)#limite inferior, superior y numero de puntos

#Creacion de forma de onda de portadora
sinus= np.sin(2* np.pi * f * tp)# por frecuencia por vector de tiempo


#Frecuencia de muestreo
fs=p/T #50khz


#Creacion de linea temporal para toda señal Tx
t=np.linspace(0,N*T,N*p) # Numero de bits por el tiempo


#Inicializar el vector de la señal 

senal=np.zeros(N*p)

onda= np.sin(2*np.pi*f*t)

#Creacion de senal modulada     

for k,b in enumerate(bits[0]):
    if b==1:
        senal[k*p:(k+1)*p]= onda[k*p:(k+1)*p]
    else:
        senal[k*p:(k+1)*p]= -onda[k*p:(k+1)*p]

#Visualizacion de los primeros bits modelados
pb=10
plt.figure()
plt.plot(senal[0:pb*p])
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Primeros 10 periodos")
plt.show

print("********************* Segundo ejercicio********************************")

#Calculo de potencia promedio
Pp = integrate.trapz(senal**2, t)/(N*T)
print("Potencia promedio de la señal modulada de parte 1: " + str(Pp))


print("********************* Tercer,Cuarto y Quinto ejercicio********************************")
"""Se colocan los 3 aqui debido a que como son datos aleatorios deben
quedar dentro del mismo for para que queden todos los datos relacionados"""
#Parte 4
# Antes del canal ruidoso
fig=plt.figure(figsize=(7,5), dpi= 80, facecolor='w', edgecolor='k')
fw, PSD = signal.welch(senal, fs, nperseg=1024)
plt.semilogy(fw, PSD)
plt.title("Señal limpia")
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia (tensión cuadrada/hz)')
plt.grid(axis='y', alpha=0.75)
plt.show()

# lista que guarda calores de error
erroresBER = []

for i in range (-2,3+1):
    # Relación señal-a-ruido deseada
    SNR=i
    # Potencia del ruido para SNR y potencia de la señal dadas
    Pn=Pp/(10**(SNR/10))
    #desvesta
    sigma = np.sqrt(Pn)
    #Crear ruido(Pn=sigma^2) la potencia del ruido en una varianza porque 
    #es una disperción 
    ruido= np.random.normal(0,sigma,senal.shape)

    #Simulae "el canal":señal recibida
    Rx = senal + ruido

    #Visualizacion de los primeros bits recibidos
    #Parte 3, señal con ruido
    plt.figure()
    plt.plot(Rx[0:pb*p])
    plt.title("Señal con ruido blanco añadido con SNR: " + str(SNR) + "dB")
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud de la señal')
    plt.show
    
    #Parte 4, después del canal ruidoso
    fw, PSD = signal.welch(Rx, fs, nperseg=1024)
    fig=plt.figure(figsize=(7,5), dpi= 80, facecolor='w', edgecolor='k')
    plt.semilogy(fw, PSD)
    plt.title("Señal ruidosa con SNR: " + str(SNR) + "dB")
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Densidad espectral de potencia (tension cuadrada/Hz)')
    plt.grid(axis='y', alpha=0.75)
    plt.show()


    #Parte 5, Demolacion de un valor de energia
    #Energía de la onda original
    Es= np.sum(sinus**2)
    #Inicialización de bits recibidos
    bitsRx=np.zeros(bits.shape)

    #Decodificacion de la señal por detección de energía

    for k,b in enumerate(bits[0]):
        Ep=np.sum(Rx[k*p:(k+1)*p] * sinus)#producto interno de 2 funciones
        if Ep>Es/1.5:
            bitsRx[k]=1
        else:
            bitsRx[k]=0
        
    err= np.sum(np.abs(bits - bitsRx))
    BER= err/N
    erroresBER.append(BER)
    print("Errores:"+str(err[0])+", en "+str(N)+" bits, Tasa de error: "+str(BER[0]))
    

print("********************* Sexto ejercicio********************************")
fig=plt.figure()
SNR= [-2,-1,0,1,2,3]
plt.scatter(SNR, erroresBER)
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.title("Error Rate")
plt.grid(axis='y', alpha=0.75)
plt.show()







