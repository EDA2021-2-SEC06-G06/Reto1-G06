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
from datetime import datetime, date
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
               "artworks": None,
               "artwork_2":None}

    catalog["artists"] = lt.newList("ARRAY_LIST")
    catalog["artworks"] = lt.newList("ARRAY_LIST")
    catalog['artwork_2'] = lt.newList("ARRAY_LIST")
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

def artworks_found(date_initial,date_final,catalog):
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
    return data_artworks,count
def artists_found(catalog):
    i=1
    artworks_clasificados=catalog["artwork_2"]
    artists=catalog["artists"]
    Artworks_final=lt.newList()
    largo=lt.size(artworks_clasificados)
    
    while i<largo:
        artwork=lt.getElement(artworks_clasificados,i)
        constituentID=artwork["ConstituentID"]
        new_constituentID=constituentID.replace("[","")
        new_constituentID1=new_constituentID.replace("]","")
        new_constituentID2=new_constituentID1.replace(",","")
        list_constituentID=new_constituentID2.split()
        size_artwork=len(list_constituentID)
        centinela=True
        j=1
        data_necessary={}
        if size_artwork==1:
            while j<lt.size(artists) and centinela==True:
                artist=lt.getElement(artists,j)
                constituentID_2=artist["ConstituentID"]
                
                if int(list_constituentID[0])==int(constituentID_2):
                    print(1)
                    data_necessary={"Titulo":artwork["Title"],
                                    "Artista":artist["Name"],
                                    "Fecha":artwork["Date"],
                                    "Medio":artwork["Medium"],
                                    "Dimensiones":artwork["Dimensions"]   
                                         }
                    lt.addLast(Artworks_final,data_necessary)
                    centinela=False
              
                j+=1 
        elif size_artwork>1:
            authors=[]
            
            for no_artist in list_constituentID:
                centinela=True
                while j<lt.size(artists) and centinela==True:
                    artist=lt.getElement(artists,j)
                    constituentID_2=artist["ConstituentID"]
                    if int(no_artist)==int(constituentID_2):
                        author=artist["Name"]
                        authors.append(author)
                        centinela=False
                j+=1  
            data_necessary={"Titulo":artwork["Title"],
                            "Artista":authors,
                            "Fecha":artwork["Date"],
                            "Medio":artwork["Medium"],
                            "Dimensiones":artwork["Dimensions"]
            } 
            lt.addLast(Artworks_final,data_necessary)   

        i+=1
    return Artworks_final
    


# Funciones utilizadas para comparar elementos dentro de una lista
def compare_artists(artist1,artist2):
    return (float (artist1["BeginDate"]) < float(artist2["BeginDate"]))

def compare_artworks(artwork1,artwork2):
    return  (artwork1["DateAcquired"]) < (artwork2["DateAcquired"])

# Funciones de ordenamiento
def sortArtists(catalog):
    sa.sort(catalog['artists'],compare_artists)

def sortArtworks(catalog):
    sa.sort(catalog['artworks'],compare_artworks)
    
