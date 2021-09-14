"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as iso
from DISClib.Algorithms.Sorting import shellsort as sso
from DISClib.Algorithms.Sorting import mergesort as mso
from DISClib.Algorithms.Sorting import quicksort as qso
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(list_type):
    """
    Inicializa el catálogo de obras.
    """
    catalog = {"artists": None,
               "artworks": None}

    if list_type == 1:
        catalog["artists"] = lt.newList("ARRAY_LIST")
        catalog["artworks"] = lt.newList("ARRAY_LIST")
    else:
        catalog["artists"] = lt.newList()
        catalog["artworks"] = lt.newList()

    return catalog


# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    Arti_r=artists_required(artist["ConstituentID"],
                            artist["DisplayName"],
                            artist["BeginDate"],
                            artist["EndDate"],
                            artist["Nationality"],
                            artist["Gender"])
    lt.addLast(catalog['artists'], Arti_r)
    

def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista de obras
    Artw_r=artworks_required(artwork["ObjectID"],
                            artwork["Title"],
                            artwork["ConstituentID"],
                            artwork["Date"],
                            artwork["Medium"],
                            artwork["Dimensions"],
                            artwork["Classification"],
                            artwork["Department"],
                            artwork["DateAcquired"])
    lt.addLast(catalog['artworks'], Artw_r)


# Funciones para creacion de datos
def artists_required(artistID,name,begindate,end,nationality,gender):
    artist={"ArtistID":artistID,
            'Name':name,
            'BeginDate':begindate,
            'EndDate':end,
            'Nationality':nationality,
            'Gender':gender}
    return artist


def artworks_required(artworkID,title,artistID,date,medium,dimensions,classification,department,dateacquired):
    artwork={"ArtworkID":artworkID,
            "Title": title,
            "ArtistID":artistID,
            "Date":date,
            "Medium": medium,
            "Dimensions": dimensions,
            "Classification": classification,
            "Department": department,
            "DateAcquired": dateacquired}
    return artwork


# Funciones de consulta

def binary_search(lst, column, element):
    """
    Se basó en este código en el que se encuentra en la siguiente página web:
    https://www.geeksforgeeks.org/python-program-for-binary-search/
    """

    size = lt.size(lst)
    low = 0
    high = size - 1
 
    while low <= high:
        mid = (high + low) // 2
        elem = lt.getElement(lst, mid)
 
        if int(elem[column]) < element:
            low = mid + 1
 
        elif int(elem[column]) > element:
            high = mid - 1

        else:
            return mid
 
    return -1


def getRangeReq1(artists, a_inicial, a_final):
    """
    Es posible cambiar el uso de BeginDate si se cargan los datos de otra manera.
    También se podría realizar solo una búsqueda, encontrando solamente el año inicial
    y agregando los datos a partir de ahí hasta que se encuentre el último elemento
    del año final.
    """
    #buscar posición de inicio
    pos1 = binary_search(artists, "BeginDate", a_inicial) 
    index1 = pos1-1
    found_pos1 = False

    while (not found_pos1) and index1>0:
        prev_element = lt.getElement(artists, index1)

        if int(prev_element["BeginDate"]) == a_inicial:
            pos1 -= 1
            index1 -= 1
        else:
            found_pos1 = True


    #buscar posición final
    pos2 = binary_search(artists, "BeginDate", a_final)
    index2 = pos2+1
    found_pos2 = False

    while not found_pos2 and index2<=lt.size(artists):
        next_element = lt.getElement(artists, index2)

        if int(next_element["BeginDate"]) == a_final:
            pos2 += 1
            index2 += 1
        else:
            found_pos2 = True

    return pos1,pos2


def getArtistsRangeReq1(catalog, a_inicial, a_final):
    artists = catalog['artists']
    pos1,pos2 = getRangeReq1(artists, a_inicial, a_final)
    artists_range = lt.newList()
    count = pos2 - pos1 + 1

    for pos in range(pos1, pos2 + 1):
        element = lt.getElement(artists, pos)
        lt.addLast(artists_range, element)

    return artists_range, count


# Funciones utilizadas para comparar elementos dentro de una lista
def compare_artists(artist1,artist2):
    return (float (artist1["BeginDate"]) < float(artist2["BeginDate"]))


def cmpArtworkByDateAcquired(artwork1,artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return artwork1["DateAcquired"] < artwork2["DateAcquired"]


# Funciones de ordenamiento
def sortArtists(catalog, sort_type):
    if sort_type == 1:
        iso.sort(catalog['artists'],compare_artists)
    elif sort_type == 2:
        sso.sort(catalog['artists'],compare_artists)
    elif sort_type == 3:
        mso.sort(catalog['artists'],compare_artists)
    elif sort_type == 4:
        qso.sort(catalog['artists'],compare_artists)


def sortArtworks(catalog, sort_type):
    if sort_type == 1:
        iso.sort(catalog['artworks'],cmpArtworkByDateAcquired)
    elif sort_type == 2:
        sso.sort(catalog['artworks'],cmpArtworkByDateAcquired)
    elif sort_type == 3:
        mso.sort(catalog['artworks'],cmpArtworkByDateAcquired)
    elif sort_type == 4:
        qso.sort(catalog['artworks'],cmpArtworkByDateAcquired)