# coding=utf-8

# SCRIPT THAT CHECKS known_printers.json FILE CONFIGURATION
# Developed for Python 2.7

# Imports
import os
from os.path import expanduser
import ast

# Classes
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Variables
#winuser =  os.getenv('username')
home = expanduser("~")
path = home+'\\AppData\\Roaming\\Zetup\\known_printers.json'
filamentDiameter = 1.75
nozzleDiameter = 0.40000000000000002
tam = 150
version = '1'

# Does file exist?
if os.path.isfile(path):

    # We read the whole file content into kprinters variable
    with open(path, 'r') as content_file:
        kprinters = content_file.read()

    # Close file
    content_file.close()

    # Cast kprinters from String to Dictionary
    kprinters = ast.literal_eval(kprinters)

    # Check all keys are declared into known_printers.json file and default values are correct

    # Check if defaultPrinterId Key do exists and is not empty
    if 'defaultPrinterId' in kprinters:
        if kprinters['defaultPrinterId'] != '': print bcolors.OKGREEN,'OK',bcolors.ENDC,'Default Printer Id:',kprinters['defaultPrinterId']
        else: print bcolors.FAIL,'NOK',bcolors.ENDC,'Default PrinterId is empty'
    else: print bcolors.FAIL,'NOK',bcolors.ENDC,'Default PrinterId not found'

    if 'printersData' in kprinters:
        print bcolors.OKGREEN,'OK',bcolors.ENDC,'Printers Data'

        printersData = kprinters['printersData']

        if 'filament' in printersData[0]:
            print bcolors.OKGREEN, '\tOK', bcolors.ENDC, 'Filament'
            if 'alpha' in printersData[0]['filament']:
                if printersData[0]['filament']['alpha'] != ' ': print bcolors.OKGREEN, '\t\tOK', bcolors.ENDC, 'Alpha:',printersData[0]['filament']['alpha']
                else: print bcolors.FAIL,'NOK',bcolors.ENDC,'Filament Alpha is empty'
            else: print bcolors.FAIL,'NOK',bcolors.ENDC,'Filament Alpha not found'

            if 'color' in printersData[0]['filament']:
                if printersData[0]['filament']['color'] != ' ': print bcolors.OKGREEN, '\t\tOK', bcolors.ENDC, 'Color:',printersData[0]['filament']['color']
                else: print bcolors.FAIL,'NOK',bcolors.ENDC,'Filament Color is empty'
            else: print bcolors.FAIL,'NOK',bcolors.ENDC,'Filament Color not found'

            if 'type' in printersData[0]['filament']:
                if printersData[0]['filament']['type'] == 'PLA': print bcolors.OKGREEN, '\t\tOK', bcolors.ENDC, 'Type:',printersData[0]['filament']['type']
                else: print bcolors.FAIL,'NOK',bcolors.ENDC,'Filament Type is empty'
            else: print bcolors.FAIL,'NOK',bcolors.ENDC,'Filament Type not found'

        else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Filament not found'

        # Check if printerId Key do exists into printersData and is not empty
        if 'printerId' in printersData[0]:
            if printersData[0]['printerId'] != '':
                print bcolors.OKGREEN, '\tOK', bcolors.ENDC, 'Printer Id:',printersData[0]['printerId']
            else:
                print bcolors.FAIL, 'NOK', bcolors.ENDC, 'Printer Id is empty'
        else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Printer Id not found'

        # Check if printerName Key do exists into printersData and is not empty
        if 'printerName' in printersData[0]:
            if printersData[0]['printerName'] != '':
                print bcolors.OKGREEN, '\tOK', bcolors.ENDC, 'Printer Name:',printersData[0]['printerName']
            else:
                print bcolors.FAIL, 'NOK', bcolors.ENDC, 'Printer Name is empty'
        else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Printer Name not found'

        # Check if printerProperties Key do exists into printersData
        if 'printerProperties' in printersData[0]:
            print bcolors.OKGREEN, '\tOK', bcolors.ENDC, 'Printer Properties'

            # Check if filamentDiameter Key do exists into printerProperties and value equals to 1.75 (default)
            if 'filamentDiameter' in printersData[0]['printerProperties']:
                if printersData[0]['printerProperties']['filamentDiameter'] == filamentDiameter: print bcolors.OKGREEN, '\t\tOK', bcolors.ENDC, 'Filament Diameter',printersData[0]['printerProperties']['filamentDiameter']
                else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Filament Diameter unexpected'
            else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Filament Diameter not found'

            # Check if nozzleDiameter Key do exists into printerProperties and value equals to 1.75 (default)
            if 'nozzleDiameter' in printersData[0]['printerProperties']:
                if printersData[0]['printerProperties']['nozzleDiameter'] == nozzleDiameter: print bcolors.OKGREEN, '\t\tOK', bcolors.ENDC, 'Nozzle Diameter',printersData[0]['printerProperties']['nozzleDiameter']
                else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Nozzle Diameter unexpected'
            else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Nozzle Diameter not found'

            # Check if platformDepth Key do exists into printerProperties and value equals to 1.75 (default)
            if 'platformDepth' in printersData[0]['printerProperties']:
                if printersData[0]['printerProperties']['platformDepth'] == tam: print bcolors.OKGREEN, '\t\tOK', bcolors.ENDC, 'Platform Depth',printersData[0]['printerProperties']['platformDepth']
                else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Platform Depth unexpected'
            else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Platform Depth not found'

            # Check if platformHeight Key do exists into printerProperties and value equals to 1.75 (default)
            if 'platformHeight' in printersData[0]['printerProperties']:
                if printersData[0]['printerProperties']['platformHeight'] == tam: print bcolors.OKGREEN, '\t\tOK', bcolors.ENDC, 'Platform Height',printersData[0]['printerProperties']['platformHeight']
                else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Platform Depth unexpected'
            else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Platform Height not found'

            # Check if platformWidth Key do exists into printerProperties and value equals to 1.75 (default)
            if 'platformWidth' in printersData[0]['printerProperties']:
                if printersData[0]['printerProperties']['platformWidth'] == tam: print bcolors.OKGREEN, '\t\tOK', bcolors.ENDC, 'Platform Width',printersData[0]['printerProperties']['platformWidth']
                else:print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Platform Width unexpected'
            else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Platform Width not found'
        else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Printer Properties not found'

        # Check if printerSerialNumber Key do exists into printersData and is not empty
        if 'printerSerialNumber' in printersData[0]:
            if printersData[0]['printerSerialNumber'] != '':
                print bcolors.OKGREEN, '\tOK', bcolors.ENDC, 'Printer Serial Number:',printersData[0]['printerSerialNumber']
            else:
                print bcolors.FAIL, 'NOK', bcolors.ENDC, 'Printer Serial Number is empty'
        else: print bcolors.FAIL, '\tNOK', bcolors.ENDC, 'Printer Serial Number not found'
    else:
        print bcolors.FAIL,'NOK',bcolors.ENDC,'Printers Data not found'

    # Check if version Key do exists and equals to 1 (current version)
    if 'version' in kprinters:
        if kprinters['version'] == version: print bcolors.OKGREEN,'OK',bcolors.ENDC,'Version:',kprinters['version']
        else: print bcolors.FAIL,'NOK',bcolors.ENDC,'Wrong Version'
    else: print bcolors.FAIL,'NOK',bcolors.ENDC,'Version not found'
else:
    print 'known_printers no existe:'