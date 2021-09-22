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
    """
    Se adiciona la obra a la lista de obras
    """
    Artw_r=artworks_required(artwork["ObjectID"],
                            artwork["Title"],
                            artwork["ConstituentID"],
                            artwork["Date"],
                            artwork["Medium"],
                            artwork["Dimensions"],
                            artwork["Classification"],
                            artwork["Department"],
                            artwork["DateAcquired"],
                            artwork['CreditLine'],
                            artwork["URL"])

    addArtistsNames(catalog, Artw_r)

    lt.addLast(catalog['artworks'], Artw_r)


# Funciones para creacion de datos

def splitAuthorsIDs(authorsIDs):
    authors=authorsIDs.replace(",","")
    authors = authors.replace("[","")
    authors=authors.replace("]","")

    authorsIDs_list = lt.newList()
    centinela = True

    while centinela:
        if " " in authors:
            pos = authors.find(" ")
            lt.addLast(authorsIDs_list, authors[0:pos])
            authors = authors[pos + 1:]

        if " " not in authors:
            lt.addLast(authorsIDs_list, authors)
            centinela = False

    return authorsIDs_list


def addArtistsNames(catalog, artwork):
    """
    Añade en la información de cada obra los nombres de sus autores
    """
    artists = catalog["artists"]
    authors_IDs = artwork["ArtistID"]
    authors_IDs = splitAuthorsIDs(authors_IDs)
    authors = ""

    #Revisar cada elemento de la cola de IDs de autores         
    while lt.size(authors_IDs)>0: #No realiza más de X ciclos
        authorID = lt.firstElement(authors_IDs)    
        j = binary_search(artists, authorID, AuthorIDLowerThanGivenID, AuthorIDGreaterThanGivenID)
        artist = lt.getElement(artists, j)
        author=artist["Name"]

        if authors == "":                
            authors = author
        else:
            authors += ", " + author

        lt.removeFirst(authors_IDs)

    artwork["ArtistName"] = authors


def artists_required(artistID,name,begindate,end,nationality,gender):
    artist={"ArtistID":artistID,
            'Name':name,
            'BeginDate':begindate,
            'EndDate':end,
            'Nationality':nationality,
            'Gender':gender}
    return artist


def artworks_required(artworkID,title,artistID,date,medium,dimensions,
                    classification,department,dateacquired,creditline, url):
    artwork={"ArtworkID":artworkID,
            "Title": title,
            "ArtistID":artistID,
            "ArtistName": "",
            "Date":date,
            "Medium": medium,
            "Dimensions": dimensions,
            "Classification": classification,
            "Department": department,
            "DateAcquired": dateacquired,
            "CreditLine": creditline,
            "URL": url}
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
    pos = getInitPosReq1(artists, date_initial)
    artists_range = lt.newList()
    size = lt.size(artists)

    artists_count = 0

    while pos<=size:
        artist = lt.getElement(artists, pos)

        if (int(artist["BeginDate"])>=date_initial) and (int(artist["BeginDate"])<=date_final):
            lt.addLast(artists_range, artist)
            artists_count += 1
        
        elif int(artist["BeginDate"]) > date_final:
            break

        pos += 1

    return artists_range, artists_count


"Requerimiento 2"
def binary_searchReq2(lst, value, lowercmpfunction, greatercmpfunction):
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

        if (low==(high-1)) or (low==high): #Se halla el primer elemento del rango así no haya coincidencia exacta
            return low
 
    return -1


def getArtworksInfoReq21(catalog, date_initial, date_final):
    artworks = catalog["artworks"]
    Artworks_final=lt.newList("ARRAY_LIST") #ARRAY_LIST para acceder a cada posición con tiempo constante
    
    pos = binary_searchReq2(artworks, date_initial, DateAcquiredLowerThanGivenDate, DateAcquiredGreaterThanGivenDate) #log(n)
    size = lt.size(artworks)
    artworks_count = 0
    purchase_count = 0
    
    #Se parte de la posición inicial encontrada y se recorre hasta que se encuentra una fecha fuera del rango
    while pos<=size: #Recorre n veces en el peor caso
        artwork = lt.getElement(artworks,pos)

        if (artwork['DateAcquired']>=date_initial) and (artwork['DateAcquired']<=date_final):
            artworks_count += 1

            #Almacenar la información relevante
            data_necessary=lt.newList("ARRAY_LIST") 
            lt.addLast(data_necessary, artwork["ArtworkID"])          #pos 1: ID de la obra
            lt.addLast(data_necessary, artwork["Title"])              #pos 2: Título de la obra
            lt.addLast(data_necessary, artwork["ArtistName"])         #pos 3: Nombres de los autores
            lt.addLast(data_necessary, artwork["Medium"])             #pos 4: Técnica de la obra
            lt.addLast(data_necessary, artwork["Dimensions"])         #pos 5: Dimensiones de la obra
            lt.addLast(data_necessary, artwork["Date"])               #pos 6: Fecha de la obra
            lt.addLast(data_necessary,artwork["DateAcquired"])        #pos 7: Fecha de adquisición de la obra
    
            lt.addLast(Artworks_final,data_necessary)    

            if artwork["CreditLine"]=="Purchase":
                purchase_count+=1

        elif artwork['DateAcquired']>date_final:
            break

        pos+=1

    return Artworks_final,artworks_count,purchase_count


"Requerimiento 4"
def nationalityListReq4(catalog):
    """
    Crea una lista, cuyos elementos son listas que tienen en la posición 1 una nacionalidad y en sus 
    demás posiciones los IDs de los artistas que pertenecen a esa nacionalidad. Devuelve esta lista 
    junto con un directorio. Complejidad O(n)
    """
    artists = catalog["artists"]
    nationalities = lt.newList("ARRAY_LIST") #Lista que guarda los nombres de las nacionalidades (sin IDs)
    nationality_list = lt.newList("ARRAY_LIST") #Lista de listas de nacionalidades-IDs

    pos_artists = 1
    size_artists = lt.size(artists)

    while pos_artists <= size_artists: #size(artists) ciclos
        artist = lt.getElement(artists, pos_artists)
        nationality = artist["Nationality"]
        artistID = artist["ArtistID"]

        if (nationality == "") or (nationality=="Nationality unknown"):
            nationality = "Unknown"

        pos_nationality = lt.isPresent(nationalities, nationality) #Peor caso: #nacionalidades ciclos

        if pos_nationality==0:
            country = lt.newList("ARRAY_LIST") #Lista que guarda la nacionalidad y los IDs de sus artistas

            lt.addLast(country, nationality) #En pos 1 se guarda la nacionalidad
            lt.addLast(country, artistID)    #En pos>1 se guardan los IDs de los artistas correspondientes

            lt.addLast(nationalities, nationality) #Se agrega la nacionalidad al haber sido operada por 1ra vez
            lt.addLast(nationality_list, country) #Se guarda country en la misma posición que en nationalities

        else:
            country = lt.getElement(nationality_list, pos_nationality)
            lt.addLast(country, artistID)
        
        pos_artists += 1

    return nationality_list, nationalities


def getNationalityCountReq4(catalog):
    artworks = catalog["artworks"]
    nationality_list, nationalities = nationalityListReq4(catalog)
    final_list = lt.newList("ARRAY_LIST")

    while lt.size(nationalities)>0:  # size(nationalities) ciclos
        nationality = lt.removeFirst(nationalities)
        country_stack = stack.newStack() #¿Buena idea hacer un stack?
        artworks_info = lt.newList("ARRAY_LIST")

        stack.push(country_stack, nationality)
        stack.push(country_stack, artworks_info)
        stack.push(country_stack, 0)
        stack.push(country_stack, 0)
        
        lt.addLast(final_list, country_stack)

    pos_artworks = 1
    size_artworks = lt.size(artworks)

    while pos_artworks<=size_artworks: #Realiza size(artworks) ciclos
        artwork = lt.getElement(artworks, pos_artworks)

        artwork_info = stack.newStack()
        stack.push(artwork_info, artwork["Dimensions"])
        stack.push(artwork_info, artwork["Medium"])
        stack.push(artwork_info, artwork["Date"])
        stack.push(artwork_info, artwork["ArtistName"])
        stack.push(artwork_info, artwork["Title"])
        stack.push(artwork_info, artwork["ArtworkID"])
        artworkNotInList = True

        authorsIDS = artwork["ArtistID"]
        authors_queue = splitAuthorsIDs(authorsIDS)
        
        while queue.size(authors_queue)>0: #No más de X ciclos
            authorID = queue.dequeue(authors_queue)

            pos_nationality = 1
            found = False
            size_nationalities = lt.size(nationality_list)

            while (pos_nationality<=size_nationalities) and (not found): #No más de #países ciclos
                nationality = lt.getElement(nationality_list, pos_nationality)
                pos_ID = lt.isPresent(nationality, authorID) #No más de #maxArtistasNacionalidad ciclos

                if pos_ID != 0:
                    found = True
                    country_stack = lt.getElement(final_list, pos_nationality)
                    country_count = stack.pop(country_stack)
                    artwork_count = stack.pop(country_stack)
                    artworks_info = stack.pop(country_stack)
                    
                    if artworkNotInList:
                        lt.addLast(artworks_info, artwork_info)
                        artworkNotInList = False
                        artwork_count += 1

                    country_count += 1
                    
                    stack.push(country_stack, artworks_info)
                    stack.push(country_stack, artwork_count)
                    stack.push(country_stack, country_count)

                pos_nationality += 1

        pos_artworks+=1
    
    return final_list


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

#1- Ordenar por departamentos
#2- Búsqueda binaria para buscar obras del departamento (getInitPos)
#3- Sacar lista de obras (peso, costo...) -- lista1
#4- Ordenar lista1 por Date (extraer más antiguos en una lista2)
#5- Ordenar lista1 por costo (extraer más costosas en una lista3)
#A retornar: lista2, lista3, conteo de obras (size(lista1)), peso total, costo total


# Funciones utilizadas para comparar elementos dentro de una lista
"Para Artistas"
def cmpArtistByBeginDate(artist1,artist2):
    return (float (artist1["BeginDate"]) < float(artist2["BeginDate"]))


def BeginDateLowerThanGivenDate(artist, date):            #Requerimiento 1
    return float(artist["BeginDate"]) < date


def BeginDateGreaterThanGivenDate(artist, date):          #Requerimiento 1
    return float(artist["BeginDate"]) > date


def cmpArtistByAuthorID(artist1, artist2):                #Requerimiento 2
    return artist1["ArtistID"] < artist2["ArtistID"]


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


def AuthorIDLowerThanGivenID(artist, id):                 #Requerimiento 2
    return artist["ArtistID"] < id


def AuthorIDGreaterThanGivenID(artist, id):               #Requerimiento 2
    return artist["ArtistID"] > id


def cmpByNumAuthors(nationality1, nationality2):          #Requerimiento 4
    return stack.top(nationality1) > stack.top(nationality2)


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


def sortArtworks(catalog, sort_type, cmpfunction):
    if sort_type == 1:
        iso.sort(catalog['artworks'],cmpfunction)
    elif sort_type == 2:
        sso.sort(catalog['artworks'],cmpfunction)
    elif sort_type == 3:
        mso.sort(catalog['artworks'],cmpfunction)
    elif sort_type == 4:
        qso.sort(catalog['artworks'],cmpfunction)


def sortReq4(final_list):
    mso.sort(final_list, cmpByNumAuthors)