﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from datetime import datetime, date


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Consultar Requerimiento 1")
    print("2- Consultar Requerimiento 2")
    print("3- Consultar Requerimiento 3")
    print("4- Consultar Requerimiento 4")
    print("5- Consultar Requerimiento 5")
    print("6- Consultar Requerimiento 6")
    print("7- Salir")


def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga las obras en la estructura de datos
    """
    controller.loadData(catalog)

def printFirst(lst, num):
    """
    Imprime los primeros num elementos de la lista.
    """
    for pos in range(1,num+1):
        print(lt.getElement(lst, pos))


def printLast(lst, num):
    """
    Imprime los últimos num elementos de la lista.

    Nota: Para un algoritmo de menor orden de crecimiento en el caso de la lista encadenada,
          habría que crear un método alternativo al getElement() para este tipo de lista 
          puesto que se recorre casi completa por cada elemento que se busca.
    """
    for x in range(num-1, -1,-1):
        pos = lt.size(lst) - x
        print(lt.getElement(lst, pos))


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        print("\nÚltimos 3 artistas:")
        printLast(catalog["artists"], 3)
        print("\nÚltimas 3 obras:")
        printLast(catalog["artworks"], 3)
        print("\n")        

    elif int(inputs[0]) == 1:
       
        print("En segundos procederemos a buscar los artistas nacidos en el rango de años que se requiera")
        a_inicial=input("Por favor ingrese el año inicial: ")
        a_final=input("Por favor ingrese el año final: ")
        artistas_encontrados=controller.get_artists_range(int(a_inicial),int(a_final),catalog)
        count=lt.size(artistas_encontrados)
        print("\n Se encontraron " + str(count) + " artistas nacidos en el rango dado")
        print("\nPrimeros 3 artistas:")
        printFirst(artistas_encontrados,3)
        print("\nUltimos 3 artistas:")
        printLast(artistas_encontrados, 3)



    elif int(inputs[0]) == 2:
        print("Listar cronologicamente las adquisiciones")
        print("Por favor ingresar la fecha en el siguiente formato AAAA-MM-DD")
        date_1=input("Por favor ingrese la fecha inicial: ")
        date_2=input("Por favor ingrese la fecha final: ")
        date_initial=datetime.strptime(date_1, "%Y-%m-%d")
        date_final=datetime.strptime(date_2, "%Y-%m-%d")
        obras_encontradas=controller.artworks_found(date_initial,date_final,catalog)

        find_artistists=controller.artists_found(catalog)
        print(find_artistists)
    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass

    else:
        sys.exit(0)
sys.exit(0)
