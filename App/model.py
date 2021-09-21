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


from DISClib.DataStructures.arraylist import size
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import queue
from DISClib.ADT import stack
from datetime import datetime, date
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mso
from DISClib.Algorithms.Sorting import quicksort as qso
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de obras.
    """
    catalog = {"artists": None,
               "artworks": None,
               "artwork_2":None,
               "tecnicas":None}

    catalog["artists"] = lt.newList("ARRAY_LIST")
    catalog["artworks"] = lt.newList("ARRAY_LIST")
    catalog['artwork_2'] = lt.newList("ARRAY_LIST")
    catalog["tecnicas"] = lt.newList("ARRAY_LIST")
    return catalog


# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    Arti_r=artists_required(artist["DisplayName"],artist["BeginDate"],artist["EndDate"],artist["Nationality"],artist["Gender"],artist["ConstituentID"])
    lt.addLast(catalog['artists'], Arti_r)
    

def addArtwork(catalog, artwork):
    """"
     Se adiciona la obra a la lista de obras
     """
    fecha_adquisicion=artwork['DateAcquired']
    if fecha_adquisicion=="":
        fecha_adquisicion="1111-01-01"
    Date_acquired=datetime.strptime(fecha_adquisicion, "%Y-%m-%d")
    Artworks=artworks_required(artwork['Date'],artwork['Title'],artwork['ConstituentID'],Date_acquired,artwork['Medium'],artwork['Dimensions'],artwork['CreditLine'])
    lt.addLast(catalog['artworks'], Artworks)


# Funciones para creacion de datos
def artists_required(name,begindate,end,nationality,gender,constituentID):
    artist={'Name':name,'BeginDate':begindate,'EndDate':end,'Nationality':nationality,'Gender':gender,'ConstituentID':constituentID}
    return artist
def artworks_required(date,title,constituentid,date_acquired,medium,dimensions,creditline):
    artwork={'Date':date,'Title':title,'ConstituentID':constituentid,'DateAcquired':date_acquired,'Medium':medium,'Dimensions':dimensions,'CreditLine':creditline}
    return artwork
# Funciones de consulta
# Busqueda binaria

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

# Binary Search

#def binary_search(data, elem):

    low = 0
    high = len(data) - 1

    while low <= high:
      
        middle = (low + high)//2
       
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return -1

# Requerimiento 1 - Sin busqueda binaria

def get_artists_range(a_inicial,a_final,catalog):
    i=1
    centinela=True
    data_artists=catalog["artists"]
    artists_in_range=lt.newList()
    while i<lt.size(data_artists) and centinela==True:
        artist_m= lt.getElement(data_artists,i)
        
        if (int(artist_m['BeginDate'])>=a_inicial) and (int(artist_m['BeginDate'])<=a_final):
            artist=lt.getElement(data_artists,i)
            lt.addLast(artists_in_range,artist)
        elif (int(artist_m['BeginDate'])>a_final):
            centinela=False
        i+=1
       
    return artists_in_range

# Requerimento 2 

def artworks_found(date_initial,date_final,catalog): #Funcion principal
    i=1
    count=0
    centinela=True
    artworks=catalog["artworks"]
    data_artworks=catalog["artwork_2"]
    while i<lt.size(artworks) and centinela==True:
        artworks_a=lt.getElement(artworks,i)
        if (artworks_a['DateAcquired']>=date_initial) and (artworks_a['DateAcquired']<=date_final):
            lt.addLast(data_artworks,artworks_a)
            if artworks_a["CreditLine"]=="Purchase":
                count+=1
        elif (artworks_a['DateAcquired']>date_final):
            centinela=False
        i+=1
    return (data_artworks,count)

def splitAuthorsIDsReq2(authorsIDs):  #Tratar los datos
    authors = authorsIDs.replace("[","")
    authors=authors.replace("]","")
    authors=authors.replace(",","")
    list_constituentID=authors.split()
    return list_constituentID

def artists_found(catalog):
    iteraciones_p=1
    artworks_clasificados=catalog["artwork_2"]
    artists=catalog["artists"]
    Artworks_final=lt.newList("ARRAY_LIST")
    largo_art_clasificados=lt.size(artworks_clasificados)
    
    while iteraciones_p<=largo_art_clasificados:
        artwork=lt.getElement(artworks_clasificados,iteraciones_p)
        constituentID=artwork["ConstituentID"]
        list_constituentID=splitAuthorsIDsReq2(constituentID)
        size_artwork=len(list_constituentID)
        data_necessary=lt.newList("ARRAY_LIST")
        if size_artwork==1:
            pos1=binary_search(artists,list_constituentID[0],DateidLowerThanGivenDate,DateidGreaterThanGivenDate)
            artista=lt.getElement(artists,pos1)
            if int(list_constituentID[0])==int(artista["ConstituentID"]):
                
                lt.addLast(data_necessary, artwork["Title"])      #pos 1: Título de la obra
                lt.addLast(data_necessary, artista["Name"])       #pos 2: Nombres de los autores
                lt.addLast(data_necessary, artwork["Date"])       #pos 3: Fecha de la obra
                lt.addLast(data_necessary, artwork["Medium"])     #pos 4: Técnica de la obra
                lt.addLast(data_necessary, artwork["Dimensions"]) #pos 5: Dimensiones de la obra    

                lt.addLast(Artworks_final,data_necessary)   
        elif size_artwork>1:
            authors=[]
            
            for artist_at_the_moment in list_constituentID:
                pos=binary_search(artists,artist_at_the_moment,DateidLowerThanGivenDate,DateidGreaterThanGivenDate)
                artista=lt.getElement(artists,pos)
                if int(artist_at_the_moment)==int(artista["ConstituentID"]):
                    authors.append(artista["Name"])
            lt.addLast(data_necessary, artwork["Title"])      #pos 1: Título de la obra
            lt.addLast(data_necessary, authors)       #pos 2: Nombres de los autores
            lt.addLast(data_necessary, artwork["Date"])       #pos 3: Fecha de la obra
            lt.addLast(data_necessary, artwork["Medium"])     #pos 4: Técnica de la obra
            lt.addLast(data_necessary, artwork["Dimensions"]) #pos 5: Dimensiones de la obra    

            lt.addLast(Artworks_final,data_necessary)  

        iteraciones_p+=1
    return Artworks_final

#Requerimiento 3
def eliminar_repetidos(lista_count):
    largo_no_tec=lt.size(lista_count)
    i=1
    while i<largo_no_tec:
        valor_i=lt.getElement(lista_count,i)
        j=1+i

        while j<=largo_no_tec:
            valor_j=lt.getElement(lista_count,j)
            valor_ai=lt.getElement(valor_i,2)
            valor_ji=lt.getElement(valor_j,2)
            if valor_ai==valor_ji:
                lt.deleteElement(lista_count,j)
                largo_no_tec-=1
                j-=1
                
            j+=1
        i+=1
        
    return lista_count

def tecnicas_artisticas(nombre,catalog):
    no_iteraciones_id=1
    no_iteraciones_art=1
    centinela=True
    artists=catalog["artists"]
    artworks=catalog["artworks"]
    data_tecnicas=catalog["tecnicas"]
    large_artists=lt.size(artists)
    large_artworks=lt.size(artworks)
    #Encontremos el constituent ID
    while no_iteraciones_id<=large_artists and centinela==True:
        artist=lt.getElement(artists,no_iteraciones_id)
        if nombre==artist["Name"]:
            Id=artist["ConstituentID"]
            centinela=False
        no_iteraciones_id+=1
    #Comparamos el constituent ID para encontrar las obras
    while no_iteraciones_art<=large_artworks:
        data_at_moment=lt.newList("ARRAY_LIST")
        artwork=lt.getElement(artworks,no_iteraciones_art)
        id_in_artw=artwork["ConstituentID"]
        list_id_in_artw=splitAuthorsIDsReq2(id_in_artw)
        len_list_id=len(list_id_in_artw)
        if len_list_id==1:
            if int(list_id_in_artw[0])==int(Id):
                lt.addLast(data_at_moment, artwork["Title"])      #pos 1: Título de la obra
                lt.addLast(data_at_moment, artwork["Date"])       #pos 3: Fecha de la obra
                lt.addLast(data_at_moment, artwork["Medium"])     #pos 4: Técnica de la obra
                lt.addLast(data_at_moment, artwork["Dimensions"])  #pos 5: Dimensiones de la obra    

                lt.addLast(data_tecnicas,data_at_moment)
        elif len_list_id>1:
            for each_id in list_id_in_artw:
                if int(each_id)==int(Id):
                   lt.addLast(data_at_moment, artwork["Title"])      #pos 1: Título de la obra
                   lt.addLast(data_at_moment, artwork["Date"])       #pos 3: Fecha de la obra
                   lt.addLast(data_at_moment, artwork["Medium"])     #pos 4: Técnica de la obra
                   lt.addLast(data_at_moment, artwork["Dimensions"])  #pos 5: Dimensiones de la obra    

                   lt.addLast(data_tecnicas,data_at_moment)
        no_iteraciones_art+=1
    return data_tecnicas

def operaciones_req3(catalog):
    datos_tecnicas_art=catalog["tecnicas"]    
    iteraciones_data_art=1
    lista_count_tec=lt.newList("ARRAY_LIST")
    large_data_art=lt.size(datos_tecnicas_art)
    while iteraciones_data_art<=large_data_art:
        count=1
        lista_count_tec1=lt.newList("ARRAY_LIST")
        tecnica_m=lt.getElement(datos_tecnicas_art,iteraciones_data_art)
        iteraciones_dm=iteraciones_data_art+1
        while iteraciones_dm<=large_data_art:
            
            tecnica_m1=lt.getElement(datos_tecnicas_art,iteraciones_dm)
            tecnica_c=lt.getElement(tecnica_m1,3)
            tecnica_p=lt.getElement(tecnica_m,3)
            if tecnica_p==tecnica_c:
                count+=1
            iteraciones_dm+=1  
           
        lt.addLast(lista_count_tec1, count)        
        lt.addLast(lista_count_tec1, lt.getElement(tecnica_m,3))       ## Date  ## Dimensions
        
        lt.addLast(lista_count_tec,lista_count_tec1) 
        iteraciones_data_art+=1
    lista_sin_repetidos=eliminar_repetidos(lista_count_tec)
    #ordenar de mayor a menor
    lista_ordenada=sa.sort(lista_sin_repetidos,compare_cantidad)
    tecnica_usa_ve=lt.getElement(lista_ordenada,1)
    tecnica_mas_usada=lt.getElement(tecnica_usa_ve,2)
  
    return (lista_ordenada,tecnica_mas_usada)

#Encontrar las obras de la tecnica que mas usa el artista
def encontrar_obras_con_tec(catalog,tecnica_mas_usada):
    i=1
    data_tecnicas=catalog["tecnicas"]
    large_data_tecnicas=lt.size(data_tecnicas)
    lista_pf=lt.newList("ARRAY_LIST")
    while i<=large_data_tecnicas:
        lista_s=lt.newList("ARRAY_LIST")
        artwork_at=lt.getElement(data_tecnicas,i)
        artwork_at_moment=lt.getElement(artwork_at,3)
        if tecnica_mas_usada==artwork_at_moment:
            lt.addLast(lista_s, lt.getElement(artwork_at,1))      #pos 1: Título de la obra
            lt.addLast(lista_s, lt.getElement(artwork_at,2))       #pos 3: Fecha de la obra
            lt.addLast(lista_s, lt.getElement(artwork_at,3))      #pos 4: Técnica de la obra
            lt.addLast(lista_s, lt.getElement(artwork_at,4))  #pos 5: Dimensiones de la obra  
            lt.addLast(lista_pf,lista_s)
        i+=1
    return lista_pf

    


# Funciones utilizadas para comparar elementos dentro de una lista

#def compare_artists(artist1,artist2):
    if float (artist1["BeginDate"]) != float(artist2["BeginDate"]):
       return (float (artist1["BeginDate"]) < float(artist2["BeginDate"]))
    elif float (artist1['ConstituentID']) != float(artist2['ConstituentID']):
        return float(artist1['ConstituentID']) < float(artist2['ConstituentID'])

def compare_artists(artist1,artist2):
    return float(artist1['ConstituentID']) < float(artist2['ConstituentID'])

# Para el requerimiento 2
def compare_artworks(artwork1,artwork2):
    return  (artwork1["DateAcquired"]) < (artwork2["DateAcquired"])

def DateidLowerThanGivenDate(artists,id):         #Requerimiento 2
    return int(artists["ConstituentID"]) < int(id)

def DateidGreaterThanGivenDate(artists,id):       #Requerimiento 2
    return int(artists["ConstituentID"]) > int(id)

#Para el requerimiento 3
def compare_cantidad(cantidad1,cantidad2):
    return float(lt.getElement(cantidad1,1)) > float(lt.getElement(cantidad2,1))


# Funciones de ordenamiento
# Para el requerimiento 1
def sortArtists(catalog):
    sa.sort(catalog['artists'],compare_artists)

# Para el requerrimiento 2
def sortArtworks(catalog):
    sa.sort(catalog['artworks'],compare_artworks)
    
