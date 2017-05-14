#!/usr/bin/env python3
#Created on Wed May 10 18:33:56 2017
#@author: rodrigo Rut 17392282-5
#Desarrollo Practica 1 Programacion UCN

#Mensaje de bienvenida
bienvenida = "Aplicación para Cálculo Promedio PSU".capitalize()
print (bienvenida.center(50,"="))
print ("\n")

#Declaracion de variables
nombreAlumno = input("Ingrese nombre alumno: ")
cursoAlumno = input("Ingrese curso del alumno: ")
nemAlumno = input("Ingrese NEM del alumno: ")
psuLenguaje = input("Ingrese puntaje PSU lenguaje: ")
psuMatematica = input("Ingrese puntaje PSU Matemáticas: ")
psuCiencia = input("Ingrese puntaje PSU Ciencias: ")

#Calculo del puntaje ponderado
puntajePonderado = ((int(psuLenguaje) * 0.2) + (int(psuMatematica) * 0.5) + (int(psuCiencia) * 0.1) + (int(nemAlumno) * 0.2))
newPuntajePonderado = round (puntajePonderado,1)

#Calculo Promedio PSU
promedioPsu = ((int(psuLenguaje) + int(psuMatematica)) / 2)
newPromedioPsu = round (promedioPsu,0)

#Calculo Valoracion Alumno
valoracionAlumno = ((int(psuCiencia) / (int(psuMatematica) + int(psuLenguaje))) ** 2)
newValoracionAlumno = round (valoracionAlumno,1)

#Muestra de datos por pantalla
print ("\n")
print ("Resultados".center(50,"="))
print ("\n")
print ("Alumno(a): " + nombreAlumno.title())
print ("Curso: " + cursoAlumno.title())
print ("NEM: " + nemAlumno)
print ("Valoracion: " + str(newValoracionAlumno))
print ("PSU Matemática: " + str(psuMatematica))
print ("PSU Lenguaje: " + str(psuLenguaje))
print ("PSU Ciencias: " + str(psuCiencia))
print ("Promedio PSU: " + str(newPromedioPsu))
print ("Puntaje Ponderado: " + str(newPuntajePonderado))
