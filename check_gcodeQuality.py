# coding=utf-8

# SCRIPT THAT DETERMINATES GCODE QUALITY
# Developed for Python 2.7

# Imports
import sys
import os.path


# File requesting
if (len(sys.argv) > 1):
    # If File was passed as argument
    name = sys.argv[1]
else:
    # If File was not provided, we ask for it
    name = raw_input('Introduzca nombre completo del fichero: ')

    # Does file exist?
    if os.path.isfile(name):
        # If exist, we open it
        f = open(name, 'r')

        draft = True
        normal = True
        cant = set()

        # Get number of lines in document
        it = (line for i, line in enumerate(f))

        # Run the whole document looking for Z movements
        for line in it:
            # We cast line to String
            aux = str(line)
            if aux.__contains__(' Z'):
                # We get Z Value from each Line and
                ini = aux.find('Z')
                aux = aux[ini + 1:]
                end = aux.find(' ')
                aux = aux[:end]
                cant.add(float(aux))

        # We calculate All values addition and divide it for iterations to calculate how much is being added in each Z movement
        # Go through Set and calculate if all values are divisible by 0.300 (Draft), 0.200 (Normal) or 0.100 (High)
        for i in cant:
            if int(round(i*10)) % 3 != 0:
                draft = False
            if int(round(i*10)) % 2 != 0:
                normal = False

        # We determinate Quality and show it on screen
        if draft:
            print name, 'Quality: Draft'
        elif normal:
            print name, 'Quality: Normal'
        else:
            print name, 'Quality: High'

        # We close File opened
        f.close()
    else:
        print 'El archivo introducido no existe:'