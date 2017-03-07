# coding=utf-8

# Script that check .zup Project contains  all supposed files
# Default files are:
#   data.json
#   model_0.stl
#   project.gcode
#   thumbnail_0.png

# IMPORTS
import zipfile
import sys
import os

# VARIABLES
files = ('data.json', 'model_0.stl', 'project.gcode', 'thumbnail_0.png')

# MAIN CODE

# File requesting
if (len(sys.argv) > 1):
    # If File was passed as argument
    name = sys.argv[1]
else:
    # If Args were not provided, we ask for them
    name = raw_input('Introduzca nombre completo del fichero: ')

# Check File does exist
if os.path.isfile(name):
    # Get Project as Zip File
    zip = zipfile.ZipFile(name)

    # Check all files wanted do exists
    for i in range(len(files)):
        if files[i] in zip.namelist(): print files[i],'is ok'
        else:
            print files[i], 'is missing'
            #error = True
else: print ("El archivo introducido no existe:")