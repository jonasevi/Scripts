# coding=utf-8

# SCRIPT THAT CHECKS recent_files.json FILE CONFIGURATION
# Developed for Python 2.7

# Imports
import os.path
from os.path import expanduser
import ast

# Classes
class bcolors:
    PINK = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Variables
home = expanduser("~")
path = home+'\\AppData\\Roaming\\Zetup\\recent_files.json'
keys = ('recentModels', 'recentProjects')
subkeys = ('fileName', 'filePath')

# Does file exist?
if os.path.isfile(path):

    # We read the whole file content into doc variable
    with open(path, 'r') as content_file:
        recent_files = content_file.read()

    # Close file
    content_file.close()

    # Cast settings from String to Dictionary
    recent_files = ast.literal_eval(recent_files)

    # Check each Key included in keys list do exists
    for key in keys:
        if key in recent_files:
            print bcolors.PINK, 'OK', bcolors.ENDC, '', key, 'Key was detected'

            if len(recent_files[key]) != 0:
                for i in range(len(recent_files[key])):
                    print bcolors.PINK, '\tOK', bcolors.ENDC, '', key, 'found'
                    for subkey in subkeys:
                        print '\t\t',subkey,': ', recent_files[key][i][subkey]
            else:
                print '\tBut no one was indexed'
        else: print bcolors.FAIL, 'NOK', bcolors.ENDC,'', key,'not found'
else: print 'recent_files.json no existe en la ruta por defecto'