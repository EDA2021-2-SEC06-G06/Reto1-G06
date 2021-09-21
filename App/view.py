"""
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
from DISClib.ADT import queue
from DISClib.ADT import stack
from datetime import datetime
from time import process_time
import textwrap
from tabulate import tabulate
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n\n-----------------------------------------")
    print("Bienvenido al menú de opciones")
    print("-----------------------------------------")
    print("Opciones preliminares")
    print("1- Cargar datos")
    print("2- Ordenar obras por fecha de adquisición")
    print("-----------------------------------------")
    print("Requerimientos")
    print("10- Consultar Requerimiento 1")
    print("20- Consultar Requerimiento 2")
    print("30- Consultar Requerimiento 3")
    print("40- Consultar Requerimiento 4")
    print("50- Consultar Requerimiento 5")
    print("60- Consultar Requerimiento 6")
    print("-----------------------------------------")
    print("0- Salir\n")


def printSortMenu():
    print("1- Insertion Sort")
    print("2- Shell Sort")
    print("3- Merge Sort")
    print("4- Quick Sort")


def initCatalog(list_type):
    """
    Inicializa el catálogo
    """
    return controller.initCatalog(list_type)


def loadData(catalog, file_size, sort_artworks, sort_type):
    """
    Carga las obras en la estructura de datos
    """
    controller.loadData(catalog, file_size, sort_artworks, sort_type)


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


def adjustlenght(text, step):
    lenght = len(text)

    for n in range(step, 20*step + 1, step):
        if lenght > n:
            text = text[:n] + "\n" + text[n:]
    
    return text


def printReq1Table(lst):
    headers = ["ConstituentID", "Name", "BeginDate", "EndDate", "Nationality", "Gender"]
    table = []

    for pos in range(1,4):
        artist = lt.getElement(lst, pos)
        c1 = artist["ArtistID"]
        c2 = artist["Name"]
        c3 = artist["BeginDate"]
        c4 = artist["EndDate"]
        if c4 == "0":
            c4 = "--"
        c5 = artist["Nationality"]
        if c5 == "":
            c5 = "--"
        c6 = artist["Gender"]
        if c6 == "":
            c6 = "--"

        table.append([c1,c2,c3,c4,c5,c6])
     

    for x in range(2, -1,-1):
        pos = lt.size(lst) - x
        artist = lt.getElement(lst, pos)
        c1 = artist["ArtistID"]
        c2 = artist["Name"]
        c3 = artist["BeginDate"]
        c4 = artist["EndDate"]
        if c4 == "0":
            c4 = "--"
        c5 = artist["Nationality"]
        if c5 == "":
            c5 = "--"
        c6 = artist["Gender"]
        if c6 == "":
            c6 = "--"

        table.append([c1,c2,c3,c4,c5,c6])

    print(tabulate(table, headers, tablefmt="grid"))


def printReq2Table(lst):
    headers = ['ObjectID','Title','ArtistsNames',"Medium","Dimensions","Date","DateAcquired"]
    table = []

    for pos in range(1,4):
        lista = lt.getElement(lst, pos)
        c1 = lt.getElement(lista, 1)
        c2 = adjustlenght(lt.getElement(lista, 2), 15)
        c3 = adjustlenght(lt.getElement(lista, 3), 30)
        c4 = adjustlenght(lt.getElement(lista, 4), 20)
        c5 = adjustlenght(lt.getElement(lista, 5), 20)
        c6 = lt.getElement(lista, 6)
        c7 = lt.getElement(lista, 7)[0:10]

        table.append([c1,c2,c3,c4,c5,c6,c7])
     

    for x in range(2, -1,-1):
        pos = lt.size(lst) - x
        lista = lt.getElement(lst, pos)
        c1 = lt.getElement(lista, 1)
        c2 = adjustlenght(lt.getElement(lista, 2), 15)
        c3 = adjustlenght(lt.getElement(lista, 3), 30)
        c4 = adjustlenght(lt.getElement(lista, 4), 20)
        c5 = adjustlenght(lt.getElement(lista, 5), 20)
        c6 = lt.getElement(lista, 6)
        c7 = lt.getElement(lista, 7)[0:10]

        table.append([c1,c2,c3,c4,c5,c6,c7])

    print(tabulate(table, headers, tablefmt="grid"))


def printReq4Table1(req4_list):
    headers = ["Nationality", "ArtWorks"]
    table = []

    for pos in range(1,11):
        country_stack = lt.getElement(req4_list, pos)
        num = stack.pop(country_stack)
        country = stack.pop(country_stack)
        table.append([country, num])

    print(tabulate(table, headers, tablefmt="grid"))


catalog = None
file_size = "small"
list_type = "ARRAY_LIST"
sort_type = 3
sort_data = 1

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')


    if int(inputs) == 1:
        #Seleccionar archivo a utilizar como muestra
        #print("Para cada archivo, existen muestras con los siguientes tamaños:")
        #print("small, 5pct, 10pct, 20pct, 30pct, 50pct, 80pct, large\n")
        #file_size = input("Ingrese el tamaño de la muestra que desea utilizar: ")

        #Seleccionar tipo de lista
        #print("\n ¿Qué tipo de lista desea utilizar para crear el catálogo?")
        #print("1- Arreglo (ARRAY_LIST)")
        #print("2- Lista encadenada (SINGLE_LINKED)")
        #list_type = int(input())

        #Preguntar si ordenar obras al cargar datos
        #print("\nPara facilitar el Requerimiento 2, es posible ordenar las obras por fecha de adquisición")
        #print("apenas se cargan los archivos. Sin embargo, también es posible ordenarlas manualmente por")
        #print("medio de la opción 2 del menú.")
        #print("¿Desea que la información de las obras sea ordenada automáticamente al cargar los archivos?")
        #print("1- Sí")
        #print("2- No")
        #sort_artworks = int(input("Digite aquí su respuesta: "))

        #Cargar archivos
        print("Cargando información de los archivos ....")
        catalog = initCatalog(list_type)
        loadData(catalog, file_size, sort_data, sort_type)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        print("\nÚltimos 3 artistas:")
        printLast(catalog["artists"], 3)
        print("\nÚltimas 3 obras:")
        printLast(catalog["artworks"], 3)
        print("\n")


    elif int(inputs) == 2:
        printSortMenu()
        sort_type = int(input("Digite la opción que desea utilizar: "))
        if sort_type == 1:
            sort_ag = "Insertion Sort"
        elif sort_type == 2:
            sort_ag = "Shell Sort"
        elif sort_type == 3:
            sort_ag = "Merge Sort"
        elif sort_type == 4:
            sort_ag = "Quick Sort"

        start_time = process_time()
        controller.sortArtworks(catalog, sort_type)
        stop_time = process_time()
        running_time = (stop_time - start_time)*1000

        print("\nAlgoritmo de ordenamiento: " + sort_ag)
        print("Tamaño de la muestra: " + file_size)
        print("Tiempo de ejecución: " + str(running_time) + " milisegundos")


    elif int(inputs) == 10:
        a_inicial = int(input("Ingrese el año inicial: "))
        a_final = int(input("Ingrese el año final: "))

        start_time = process_time()
        req1, count = controller.REQ1getArtistsRange(catalog, a_inicial, a_final)
        stop_time = process_time()
        running_time = (stop_time - start_time)

        print("\n\n=============== Requerimiento Número 1 ===============")
        print("Tiempo de ejecución: " + str(running_time) + " segundos")
        
        print("\nSe encontraron " + str(count) + " artistas nacidos en el rango dado")
        print("\nLos primeros y últimos 3 fueron:")
        printReq1Table(req1)


    elif int(inputs) == 20:
        date_initial_str = input("Ingrese la fecha de adquisición inicial en formato AAAA-MM-DD: ")
        date_final_str = input("Ingrese la fecha de adquisición final en formato AAAA-MM-DD: ")
        date_initial = datetime.strptime(date_initial_str, "%Y-%m-%d")
        date_final = datetime.strptime(date_final_str, "%Y-%m-%d")

        start_time = process_time()
        req2,artworks_count,purchase_count = controller.REQ2getArtworksRange(catalog, date_initial, date_final)
        stop_time = process_time()
        running_time = (stop_time - start_time)

        print("\n\n=============== Requerimiento Número 2 ===============")
        print("Tiempo de ejecución: " + str(running_time) + " segundos")
        
        print("\nSe encontraron " + str(artworks_count) + " obras adquiridas entre la fecha " + date_initial_str + " y la fecha " + date_final_str + ".")
        print(str(purchase_count) + " fueron adquiridas por compra" + "\n")
        print("Las primeras y últimas 3 compras en el rango fueron:")
        printReq2Table(req2)


    elif int(inputs) == 30:
        pass


    elif int(inputs) == 40:
        start_time = process_time()
        req4_list = controller.REQ4getNationalityCount(catalog)
        stop_time = process_time()
        running_time = (stop_time - start_time)

        print("\n\n=============== Requerimiento Número 4 ===============")
        print("Tiempo de ejecución: " + str(running_time) + " segundos\n")
        print("El TOP 10 de nacionalidades con más obras es:")
        printReq4Table1(req4_list)


    elif int(inputs) == 50:
        pass


    elif int(inputs) == 60:
        pass


    else:
        sys.exit(0)
sys.exit(0)
