﻿"""
Reto 1 - controller.py

Carlos Arturo Holguín Cárdenas
Daniel Hernández Pineda

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
    Llama la funcion de inicializació del catálogo del modelo
    """
    catalog = model.newCatalog(list_type)
    return catalog


# Funciones para la carga de datos

def loadData(catalog, file_size, sort_data, sort_type):
    """
    Carga los datos de los archivos y los ordena
    """
    loadArtists(catalog, file_size)
    loadArtworks(catalog, file_size)

    if sort_data == 1:
        sortArtists(catalog, sort_type, model.cmpArtistByBeginDate)
        sortArtworks(catalog, sort_type, model.cmpArtworkByDateAcquired)


def loadArtists(catalog, file_size):
    """
    Carga los artistas del archivo
    """
    artistsfile = cf.data_dir + 'Artists-utf8-' + file_size + '.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)


def loadArtworks(catalog, file_size):
    """
    Carga las obras del archivo
    """
    sortArtists(catalog, 3, model.cmpArtistByAuthorID)
    artworksfile = cf.data_dir + 'Artworks-utf8-' + file_size + '.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)


# Funciones de ordenamiento

def sortArtists(catalog, sort_type, cmpfunction=model.cmpArtistByBeginDate):
    """
    Ordena los artistas según la función de comparación dada
    """
    model.sortArtists(catalog, sort_type, cmpfunction)


def sortArtworks(catalog, sort_type, cmpfunction):
    """
    Ordena las obras según la función de comparación dada
    """
    model.sortArtworks(catalog, sort_type, cmpfunction)


# Funciones de consulta sobre el catálogo

def REQ1getArtistsRange(catalog, date_initial, date_final):
    return model.getArtistsRangeReq1(catalog, date_initial, date_final)


def REQ2getArtworksRange(catalog, date_initial, date_final):
    return model.getArtworksInfoReq2(catalog, date_initial, date_final)


def REQ3get_techniquees(catalog,Name):
    return model.getTechniquesReq3(catalog,Name)


def REQ4getNationalityCount(catalog):
    final_list = model.getNationalityCountReq4(catalog)
    model.sortReq4(final_list)
    return final_list


def REQ5moveArtworks(catalog, department):
    return model.moveArtworksReq5(catalog, department)