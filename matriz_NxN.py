#!/usr/bin/env python3
"""
 matriz_NxN.py: Programa que crea una matriz NxN (siendo N facilitado por usuario como argumento posicional) y la rellena 
 con números aleatorios de 1 dígito. Calcula y almacena en dos listas la suma de cada fila y columna de la matriz y las imprime.
"""
AUTHOR = "Antonio Javier Garcia Martinez (cokesaeba@gmail.com)"
VERSION = "1.0.1"

import argparse
import random


def create_matriz(N):
    ''' Crea una matriz NxN con números aleatorios de 1 dígito '''
    matriz = []

    # N > 0, no necesitamos comprobar que sea entero porque ya lo hemos forzado
    if N < 1:
        raise ValueError("N debe ser mayor que 0")

    for i in range(N):
        matriz.append([])
        for j in range(N):
            matriz[i].append(random.randint(0,9))

    return matriz


def print_matriz(matriz):
    ''' Imprime la matriz pasada como parámetro de forma legible por humanos '''
    for i in range(len(matriz)):
        print("|", end=" ")
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("|")
    print()

def suma_filas(matriz):
    ''' Suma las filas de la matriz pasada como parámetro y devuelve una lista con los resultados '''
    sum_filas = []

    for i in range(len(matriz)):
        sum_filas.append(sum(matriz[i]))

    return sum_filas

def suma_columnas(matriz):
    ''' Suma las columnas de la matriz pasada como parámetro y devuelve una lista con los resultados '''
    sum_columnas = []

    # Otra forma de hacerlo, más legible (como en el ejemplo del curso de IBM): 
    for c in range(len(matriz)):
        sum_columnas.append(sum([row[c] for row in matriz]))

    return sum_columnas

def main():
    
    # args:
    parser = argparse.ArgumentParser(description="Matriz NxN")
    
    #VERSION
    parser.add_argument( "--version", action="version", \
                         version=f"%(prog)s {VERSION} by {AUTHOR}")
    
    #mandatory/positional args, forzamos a que sea un entero
    parser.add_argument("N", type=int, help="Tamaño de la matriz")
    
    args = parser.parse_args()

    #positional args... 
    N = args.N

    # Create matriz NxN
    matriz = create_matriz(N)


    # Print matriz
    print(f"Matriz {N}x{N}\n")

    print_matriz(matriz)
    # Forma "simple" de imprimir la matriz, menos legible pero ideal para depuración
    # print(matriz) 

    # Inicializamos las listas en las que sumaremos las filas y columnas
    sum_filas = []
    sum_columnas = []

    # Sumamos las filas y columnas
    sum_filas = suma_filas(matriz)
    sum_columnas = suma_columnas(matriz)
     

    # Imprimimos los resultados, me gusta más utilizar f-strings que format():
    print(f"\nSuma de las filas: {sum_filas}")
    print(f"\nSuma de las columnas: {sum_columnas}")

if __name__ == "__main__":
    main()
