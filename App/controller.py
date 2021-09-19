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

def initCatalog(list_type):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(list_type)
    return catalog


# Funciones para la carga de datos

def loadData(catalog, file_size, sort_artworks, sort_type):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog, file_size)
    loadArtworks(catalog, file_size)
    sortArtists(catalog, sort_type, model.cmpArtistByBeginDate)

    if sort_artworks == 1:
        sortArtworks(catalog, sort_type)


def loadArtists(catalog, file_size):
    """
    Carga los artistas del archivo.
    """
    artistsfile = cf.data_dir + 'Artists-utf8-' + file_size + '.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)


def loadArtworks(catalog, file_size):
    """
    Carga las obras del archivo.
    """
    artworksfile = cf.data_dir + 'Artworks-utf8-' + file_size + '.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)


# Funciones de ordenamiento

def sortArtists(catalog, sort_type):
    """
    Ordena los artistas por fecha de nacimiento
    """
    model.sortArtists(catalog, sort_type)


def sortArtworks(catalog, sort_type):
    """
    Ordena las obras por fecha de adquisición
    """
    model.sortArtworks(catalog, sort_type)


# Funciones de consulta sobre el catálogo

def getArtistsRange(catalog, date_initial, date_final):
    return model.getArtistsRangeReq1(catalog, date_initial, date_final)


def getArtworksRange(catalog, date_initial, date_final):
    return model.getArtworksInfoReq2(catalog, date_initial, date_final)