#!/usr/bin/env python3
"""
 matriz_NxN.py: Programa que crea una matriz NxN (siendo N facilitado por usuario como argumento posicional) y la rellena 
 con números aleatorios de 1 dígito. Calcula y almacena en dos listas la suma de cada fila y columna de la matriz y las imprime.
"""
AUTHOR = "Antonio Javier Garcia Martinez (cokesaeba@gmail.com)"
VERSION = "0.0.1"

import logging
import argparse
import random

def createLogger(file):
    ''' Crea un logger con el nombre del fichero pasado como parámetro '''

    LOG_FORMAT = "%(asctime)s %(levelname)s - %(message)s"
    logging.basicConfig(
        filename=file, level=logging.DEBUG, format=LOG_FORMAT
    )
    logger = logging.getLogger()

    return logger


def print_matriz(matriz):
    ''' Imprime la matriz pasada como parámetro de forma legible por humanos '''
    for i in range(len(matriz)):
        print("|", end=" ")
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("|")
    print()

def main():
    
    # Creamos un logger
    logger = createLogger("matriz.log")
    logger.info("Inicio del programa")

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

    # N > 0, no necesitamos comprobar que sea entero porque ya lo hemos forzado
    if N < 1:
        logger.error("N debe ser mayor que 0")
        raise ValueError("N debe ser mayor que 0")
    
    # Create matriz NxN
    matriz = []

    for i in range(N):
        matriz.append([])
        for j in range(N):
            matriz[i].append(random.randint(0,9))

    # Print matriz
    print(f"Matriz {N}x{N}\n")

    print_matriz(matriz)

    # Inicializamos las listas en las que sumaremos las filas y columnas
    sum_filas = []
    sum_columnas = []

    #TODO: Sumamos las filas y las columnas y las almacenamos en las listas
    # Sumamos las filas

    # Sumamos las columnas

    # Imprimimos los resultados

    logger.info("Fin programa!")

if __name__ == "__main__":
    main()
