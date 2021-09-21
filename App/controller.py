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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de obras

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)
    sortArtists(catalog)
    sortArtworks(catalog)


def loadArtists(catalog):
    """
    Carga los artistas del archivo.
    """
    artistsfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)


def loadArtworks(catalog):
    """
    Carga las obras del archivo.
    """
    artworksfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

# Funciones de ordenamiento

def sortArtists(catalog):
    model.sortArtists(catalog)

def sortArtworks(catalog):
    model.sortArtworks(catalog)

# Funciones de consulta sobre el catálogo
#Req1
def get_artists_range(a_inicial,a_final,catalog):
   
    artists_range=model.get_artists_range(a_inicial,a_final,catalog)
    return artists_range
#Req2
def artworks_found(date_initial,date_final,catalog):
    works_found=model.artworks_found(date_initial,date_final,catalog)
    return works_found
#Req2
def artists_found(catalog):
    artist_found=model.artists_found(catalog)
    return artist_found
#Req3
def tecnicas_artisticas(nombre,catalog):
    tecnicas_artisticas=model.tecnicas_artisticas(nombre,catalog)
    return tecnicas_artisticas
#Req3
def operaciones_req3(catalog):
    tecnica_mas_u=model.operaciones_req3(catalog)
    return tecnica_mas_u
#req3
def encontrar_obras_con_tec(catalog,tecnica_mas_usada):
    obras_con_tecnica=model.encontrar_obras_con_tec(catalog,tecnica_mas_usada)
    return obras_con_tecnica


