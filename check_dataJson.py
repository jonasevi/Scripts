# coding=utf-8

# Script that extracts data.json from a .zup Project
# data.json default configuration is checked
# User has to indicate infill & quality configured when Project was uploaded to printer
# and script will check it matchs with data.json info

# IMPORTS
import zipfile
import ast
import sys
import os

# VARIABLES
version = 1
thumbnails = 'thumbnail_0.png'
fileName = 'model_0.stl'

# MAIN CODE

# File requesting
if (len(sys.argv) > 3):
    # If File was passed as argument
    name = sys.argv[1]
    infill = sys.argv[2]
    quality = sys.argv[3]
else:
    # If Args were not provided, we ask for them
    name = raw_input('Introduzca nombre completo del fichero: ')
    infill = raw_input('Introduzca porcentaje de relleno comfigurado: ')
    quality = raw_input('Introduzca calidad configurada: ')

print '\n'

# Check File does exist
if os.path.isfile(name):
    # Extract data.json file from .zup Project given
    zip = zipfile.ZipFile(name)
    if 'data.json' in zip.namelist():
        data = zip.read('data.json')

        # Cast data from String to Dictionary
        data = ast.literal_eval(data)

        # Check if keys infill, printQuality & version do exist in data
        if 'infill' and 'printQuality' and 'version' and 'dateCreation' and 'thumbnails' and 'models' in data:
            if 'fileName' and 'positionX' and 'positionY' and 'rotationValueX' and 'rotationValueY' and 'rotationValueZ' and 'scaleValue' in data['models'][0]:
                if data['thumbnails'][0] == thumbnails and data['models'][0]['fileName'] == fileName:
                    print 'El fichero tiene la configuracion correcta'
                else: print 'WARNING: El fichero NO tiene la configuracion correcta!'
            else: print 'WARNING: El fichero NO tiene la configuracion correcta'

            if data['infill'] == infill: print 'La configuracion de Relleno coincide con la especificada'
            else: print 'La configuracion de Relleno coincide con la especificada'

            if data['printQuality'] == quality: print 'La configuracion de Calidad coincide con la especificada'
            else: print 'La configuracion de Calidad coincide con la especificada'

            if data['version'] == version: print 'La Version del fichero es correcta'
            else: print 'La Version del fichero es incorrecta'

        else: print 'ERROR: Los campos a checkear no existen en el Proyecto'
    else: print 'ERROR: el archivo data.json no existe dentro del Proyecto'
else: print ("El archivo introducido no existe:")