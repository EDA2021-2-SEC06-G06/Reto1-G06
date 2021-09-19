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
from DISClib.ADT import queue
from DISClib.ADT import stack
from DISClib.Algorithms.Sorting import insertionsort as iso
from DISClib.Algorithms.Sorting import shellsort as sso
from DISClib.Algorithms.Sorting import mergesort as mso
from DISClib.Algorithms.Sorting import quicksort as qso
from datetime import datetime
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
               #"artwork_2":None}

    if list_type == 1:
        catalog["artists"] = lt.newList("ARRAY_LIST")
        catalog["artworks"] = lt.newList("ARRAY_LIST")
        #catalog['artwork_2'] = lt.newList("ARRAY_LIST") #Probando
    else:
        catalog["artists"] = lt.newList()
        catalog["artworks"] = lt.newList()
        #catalog['artwork_2'] = lt.newList() #Probando

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
    fecha_adquisicion=artwork['DateAcquired']
    if fecha_adquisicion=="":
        fecha_adquisicion="1111-01-01"
    Date_Acquired=datetime.strptime(fecha_adquisicion, "%Y-%m-%d")
    
    Artw_r=artworks_required(artwork["ObjectID"],
                            artwork["Title"],
                            artwork["ConstituentID"],
                            artwork["Date"],
                            artwork["Medium"],
                            artwork["Dimensions"],
                            artwork["Classification"],
                            artwork["Department"],
                            Date_Acquired,
                            artwork['CreditLine'])

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


def artworks_required(artworkID,title,artistID,date,medium,dimensions,
                    classification,department,dateacquired,creditline):
    artwork={"ArtworkID":artworkID,
            "Title": title,
            "ArtistID":artistID,
            "Date":date,
            "Medium": medium,
            "Dimensions": dimensions,
            "Classification": classification,
            "Department": department,
            "DateAcquired": dateacquired,
            "CreditLine": creditline}
    return artwork


# Funciones de consulta

def binary_search(lst, value, lowercmpfunction, greatercmpfunction):
    """
    Se basó en este código en el que se encuentra en la siguiente página web:
    https://www.geeksforgeeks.org/python-program-for-binary-search/
    """

    size = lt.size(lst)
    low = 0
    high = size - 1
 
    while low <= high:
        mid = (high + low) // 2
        indexed_element = lt.getElement(lst, mid)
 
        if lowercmpfunction(indexed_element, value):
            low = mid + 1
 
        elif greatercmpfunction(indexed_element, value):
            high = mid - 1

        else:
            return mid
 
    return -1


"Requerimiento 1"
def getInitPosReq1(artists, date_initial):
    pos1 = binary_search(artists, date_initial, BeginDateLowerThanGivenDate, BeginDateGreaterThanGivenDate) 
    index1 = pos1-1
    found_pos1 = False

    while (not found_pos1) and index1>0:
        prev_element = lt.getElement(artists, index1)

        if int(prev_element["BeginDate"]) == date_initial:
            pos1 -= 1
            index1 -= 1
        else:
            found_pos1 = True

    return pos1


def getArtistsRangeReq1(catalog, date_initial, date_final):
    artists = catalog['artists']
    pos = getInitPosReq1(artists, date_initial, date_final)
    artists_range = lt.newList()
    size = lt.size(artists)

    artists_count = 0
    centinela = True

    while centinela and pos<size:
        artist = lt.getElement(artists, pos)

        if (artist["BeginDate"]>=date_initial) and (pos<=date_final):
            lt.addLast(artists_range, artist)
            artists_count += 1
        
        elif artist["BeginDate"] > date_final:
            centinela = False

        pos += 1

    return artists_range, artists_count


"Requerimiento 2"
def splitAuthorsIDsReq2(authorsIDs):
    authors = authorsIDs.replace("[","")
    authors=authors.replace("]","")
    authors=authors.replace(",","")
    
    authors_list = queue.newQueue()

    while " " in authors:
        pos = authors.find(" ")
        queue.enqueue(authors_list, authors[0:pos])
        authors = authors[pos + 1:]

    return authors_list


def getInitPosReq2(artworks, date_initial):
    pos1 = binary_search(artworks, date_initial, DateAcquiredLowerThanGivenDate, DateAcquiredGreaterThanGivenDate) 
    index1 = pos1-1
    found_pos1 = False

    #Se compara pos con la posición anterior para hallar la primera posición en la que aparece date_initial
    while (not found_pos1) and index1>0:
        prev_element = lt.getElement(artworks, index1)

        if int(prev_element["DateAcquired"]) == date_initial:
            pos1 -= 1
            index1 -= 1
        else:
            found_pos1 = True

    return pos1


def getArtworksRangeReq2(catalog, date_initial, date_final):
    artworks = catalog["artworks"]
    data_artworks = queue.newQueue()
    
    pos = getInitPosReq2(artworks, date_initial)
    size = lt.size(artworks)
    artworks_count = 0
    purchase_count = 0
    centinela = True

    #Se parte de pos y se añaden a una cola todos los elementos en el rango
    while pos<size and centinela:
        artworks_a = lt.getElement(artworks,pos)

        if (artworks_a['DateAcquired']>=date_initial) and (artworks_a['DateAcquired']<=date_final):
            queue.enqueue(data_artworks,artworks_a)
            artworks_count += 1

            if artworks_a["CreditLine"]=="Purchase":
                purchase_count+=1

        elif artworks_a['DateAcquired']>date_final:
            centinela=False

        pos+=1

    return data_artworks,artworks_count,purchase_count


def getArtworksInfoReq2(catalog, date_initial, date_final):
    artists=catalog["artists"]
    data_artworks,artworks_count,purchase_count = getArtworksRangeReq2(catalog, date_initial, date_final)
    Artworks_final=lt.newList("ARRAY_LIST") #ARRAY_LIST para acceder a cada posición con tiempo constante

    #TAREA PENDIENTE: Determinar máximo de artistas en una obra (X)
    #max = 0 

    #Se recorre la lista de obras encontradas para hallar los autores de cada una
    while queue.size(data_artworks)>0:
        artwork = queue.peek(data_artworks)
        authors_IDs = artwork["ArtistID"]
        authors_IDs = splitAuthorsIDsReq2(authors_IDs)
        authors = ""
        data_necessary=lt.newList()

        j=1
        artists_size = lt.size(artists)  

        #TAREA PENDIENTE: Determinar el máximo de artistas en una obra (X)
        #if queue.size(authors_IDs)>max:
        #    max = queue.size(authors_IDs)

        #Revisar cada elemento de la cola de IDs de autores         
        while queue.size(authors_IDs)>0: #No realiza más de X ciclos
            authorID = queue.peek(authors_IDs)    
            j = 1
            centinela = True

            #Recorrer el catálogo de autores para buscar el nombre correspondiente a cada ID
            while j<=artists_size and centinela:
                artist=lt.getElement(artists,j)
                constituentID=artist["ArtistID"]

                if int(authorID)==int(constituentID):
                    author=artist["Name"]
                        
                    if authors == "":
                        authors = author
                    else:
                        authors += ", " + author

                    centinela=False
                    queue.dequeue(authors_IDs)

                j+=1  
        
        #Almacenar la información relevante
        lt.addLast(data_necessary, artwork["Title"])      #pos 1: Título de la obra
        lt.addLast(data_necessary, authors)               #pos 2: Nombres de los autores
        lt.addLast(data_necessary, artwork["Date"])       #pos 3: Fecha de la obra
        lt.addLast(data_necessary, artwork["Medium"])     #pos 4: Técnica de la obra
        lt.addLast(data_necessary, artwork["Dimensions"]) #pos 5: Dimensiones de la obra
    
        lt.addLast(Artworks_final,data_necessary)       

        queue.dequeue(data_artworks)

    return Artworks_final,artworks_count,purchase_count


"Requerimiento 5"
def calculateDimensionsReq5(depth, height, lenght, width, diameter):
    """
    Calcula las dimensiones físicas (área o volumen) de cada obra dependiendo de la información que
    se brinde. Se utilizan unidades de metro
    """
    data = lt.newList("ARRAY_LIST")
    lt.addLast(data, depth)
    lt.addLast(data, height)
    lt.addLast(data, lenght)
    lt.addLast(data, width)
    lt.addLast(data, diameter)
    
    dimensions_count = 0
    no_dimensions = True
    ans = -1

    pos = 1
    size = lt.size(data)

    #Se evalúa cada dimensión para saber cuántas tienen información útil
    while pos<=size:
        dimension = lt.getElement(data, pos)
        if (dimension != "") and (dimension != "0"):
            lt.changeInfo(data, pos, float(dimension))
            dimensions_count += 1
            no_dimensions = False
        else:
            lt.changeInfo(data, pos, 1)
        pos += 1

    #Se calcula el factor de conversión a unidades de metro
    factor = 10**(-2*dimensions_count)

    if no_dimensions==False:
        if diameter != "":
            diameter = lt.getElement(data, 5)
            height = lt.getElement(data, 2)
            ans = 3.1416 * ((diameter/2)**2) * height * factor/100
        
        else:
            depth = lt.getElement(data, 1)
            height = lt.getElement(data, 2)
            lenght = lt.getElement(data, 3)
            width = lt.getElement(data, 4)
            ans =  depth * height * lenght * width * factor

    return ans


def calculateSingularCostReq5(depth, height, lenght, width, diameter, weight):
    """
    Calcula el costo de transportar cierta obra dadas sus dimensiones físicas y su peso.
    Las obras con volumen tienen un costo de transporte muy inferior, puesto que 1cm^2 = 10^-4 m^2,
    mientras que 1cm^3 = 10^-6 m^3
    """
    dimensions = calculateDimensionsReq5(depth, height, lenght, width, diameter)

    if dimensions == -1:
        dcost = 48
    else:
        dcost = dimensions*72
    
    max = dcost

    if (weight!="") and (weight!="0"):
        wcost = float(weight)*72

        if wcost > max:
            max = wcost

    return round(max,5)


#TAREA PENDIENTE: ¿Cómo se implementaría si la lista de artistas estuviera organizada según Constituent ID?
#Esto reduciría la complejidad temporal del algoritmo (sin tener en cuenta el ordenamiento)
#def getAuthorsReq2IfArtistsSortedByID(catalog, artworks):


# Funciones utilizadas para comparar elementos dentro de una lista
"Para Artistas"
def cmpArtistByBeginDate(artist1,artist2):
    return (float (artist1["BeginDate"]) < float(artist2["BeginDate"]))


def BeginDateLowerThanGivenDate(artist, date):            #Requerimiento 1
    return float(artist["BeginDate"]) < date


def BeginDateGreaterThanGivenDate(artist, date):          #Requerimiento 1
    return float(artist["BeginDate"]) > date


"Para Obras"
def cmpArtworkByDateAcquired(artwork1,artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return artwork1["DateAcquired"] < artwork2["DateAcquired"]


def DateAcquiredLowerThanGivenDate(artwork,date):         #Requerimiento 2
    return artwork["DateAcquired"] < date


def DateAcquiredGreaterThanGivenDate(artwork,date):       #Requerimiento 2
    return artwork["DateAcquired"] > date


def cmpArtworkByDate(artwork1,artwork2):                  #Requerimiento 5
    int(artwork1["Date"]) < int(artwork2["Date"])


# Funciones de ordenamiento
def sortArtists(catalog, sort_type, cmpfunction):
    if sort_type == 1:
        iso.sort(catalog['artists'],cmpfunction)
    elif sort_type == 2:
        sso.sort(catalog['artists'],cmpfunction)
    elif sort_type == 3:
        mso.sort(catalog['artists'],cmpfunction)
    elif sort_type == 4:
        qso.sort(catalog['artists'],cmpfunction)


def sortArtworks(catalog, sort_type):
    if sort_type == 1:
        iso.sort(catalog['artworks'],cmpArtworkByDateAcquired)
    elif sort_type == 2:
        sso.sort(catalog['artworks'],cmpArtworkByDateAcquired)
    elif sort_type == 3:
        mso.sort(catalog['artworks'],cmpArtworkByDateAcquired)
    elif sort_type == 4:
        qso.sort(catalog['artworks'],cmpArtworkByDateAcquired)