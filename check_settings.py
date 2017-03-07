# coding=utf-8

# SCRIPT THAT CHECK settings.json FILE CONFIGURATION
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
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Variables
home = expanduser("~")
path = home+'\\AppData\\Roaming\\Zetup\\settings.json'
version = 1
language = ('es', 'en')

# Does file exist?
if os.path.isfile(path):

    # We read the whole file content into doc variable
    with open(path, 'r') as content_file:
        settings = content_file.read()

    # Close file
    content_file.close()

    # Cast settings from String to Dictionary
    settings = ast.literal_eval(settings)

    # Check if language Key do exists and value is correct
    if 'language' in settings:
        if settings['language'] in language: print bcolors.PINK, 'OK', bcolors.ENDC, 'Current Language:', settings['language']
        else: print bcolors.FAIL, 'NOK', bcolors.ENDC, 'Language config is empty'
    else: print bcolors.FAIL, 'NOK', bcolors.ENDC, 'Language field not found'

    # Check if version Key do exists and value matches with current version defined
    if 'version' in settings:
        if settings['version'] == version: print bcolors.PINK, 'OK', bcolors.ENDC, 'Current Version:', settings['version']
        else: print bcolors.FAIL, 'NOK', bcolors.ENDC, 'Version config is empty'
    else: print bcolors.FAIL, 'NOK', bcolors.ENDC, 'Version field not found'
else: print 'settings.json no existe en la ruta por defecto'