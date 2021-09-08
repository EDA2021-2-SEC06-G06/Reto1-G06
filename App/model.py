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
from DISClib.Algorithms.Sorting import shellsort as sa
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
               "artworks": None}

    catalog["artists"] = lt.newList("ARRAY_LIST")
    catalog["artworks"] = lt.newList("ARRAY_LIST")
    return catalog


# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    Arti_r=artists_required(artist["DisplayName"],artist["BeginDate"],artist["EndDate"],artist["Nationality"],artist["Gender"])
    lt.addLast(catalog['artists'], Arti_r)
    

def addArtwork(catalog, artwork):
    """"
     Se adiciona la obra a la lista de obras
     """
    lt.addLast(catalog['artworks'], artwork)


# Funciones para creacion de datos
def artists_required(name,begindate,end,nationality,gender):
    artist={'name':name,'begin_date':begindate,'end':end,'nationality':nationality,'gender':gender}
    return artist

# Funciones de consulta

def get_artists_range(a_inicial,a_final,catalog):
    data_artists=catalog["artists"]
    artists_in_range=lt.newList()
    for i in data_artists:
        if (data_artists[i]["BeginDate"]>a_inicial) and (data_artists[i]["BeginDate"]<a_final):
            artist=lt.getElement(data_artists,i)
            lt.addLast(artists_in_range,artist)
            
    return artists_in_range



# Funciones utilizadas para comparar elementos dentro de una lista
def compare_artists(artist1,artist2):
    return (float (artist1["BeginDate"]) < float(artist2["BeginDate"]))


# Funciones de ordenamiento
def sortArtists(catalog):
    sa.sort(catalog['artists'],compare_artists)
    
