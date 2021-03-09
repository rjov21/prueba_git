# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:10:12 2021

@author: DIOS BENDITO
"""
# ciclo for en python

for valor in range(10):
    print(valor)

for valor in range(1, 11):
    print(valor)

for valor in range(2, 100, 2):
    print(valor)

# ciclo while

while True:
    print("hola")
    break

i = 2
while i <= 10:
    print(i)
    i += 2

# HUA que imprima el ganador de una eleccion de dos candidatos
candidato1 = 0
candidato2 = 0
num_votantes = int(input('ingrese el numero de votantes: '))
for valor in range(num_votantes+1):
    while True:
        voto = int(input('ingrese 1 por candidato1 o 2 por candidato2: '))
    break
    if voto == 1:
        candidato1 += 1
    else:
        candidato2 += 1
if candidato1 > candidato2:
    print('el ganador es candidato1')
elif candidato2 > candidato1:
    print('el ganador es candidato2')
else:
    print('se presento un empate')

# HUA que de la n notas de un estudiante calcule el promedio academico final
suma = 0
n_notas = int(input('ingrese el numero de notas: '))
for valor in range(n_notas+1):
    while True:
        nota = float(input('ingrese el valor de la nota: '))
        if nota >= 0 and nota <= 5:
            break
    suma = suma + nota
promedio = suma / n_notas
promedio = round(promedio, 2)
print(f'el promedio de las {n_notas} notas es: {promedio}')

# tipos de colecciones
# listas o vectores
# tipo de dato mutable y ordenado
a = [2, 3, 4]
b = [2, True, 'hola', 3.4]
c = [2, [True, False], ['hola', 'mundo'], [2.3, 3.4, 4.6, 7.8]]
for valor in a:
    print(valor)
for valor in b:
    print(valor)
for valor in c:
    print(valor)

a[0] = 7
print(b[2])
a.append(5)
a.remove(3)
a.pop()
a.pop(1)
a.clear()
4 in a
len(a)
b = a
id(a)
b = a[:]

# tuplas
# tipo de dato inmutable y ordenado
a = (1, 2, 3, 4)

# set
# tipo de dato mutable y no ordenado
a = {1, 2, 3, 4}
a = {7, 8, 5, 4, 9}

# diccionario
a = {'nombre': 'robinson', 'apellido': 'ordoñez'}
a = {1: 'robinson', 2: 'ordoñez'}

# funcione


def nombre_funcion():
    pass


def hola_mundo():
    print('hola mundo')


def saludo(nombre):
    print(f'hola {nombre}')


def saludo1(nombre='mundo'):
    print(f'hola {nombre}')


def operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 + num2
    return suma, resta
