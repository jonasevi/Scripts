# coding=utf-8

# IMPORTS
import requests
import json
import sys
import socket
import subprocess

# VARIABLES
project = ''
printer_ip = ''

# Get Printer IP
if (len(sys.argv) > 2):
    # If IP was passed as argument
    printer_ip = sys.argv[1]
    project = sys.argv[2]

    # Check IP readed is valid
    error = True
    while error:
        try:
            # Valid IP Address
            socket.inet_aton(printer_ip)
            error = False
        except socket.error:
            # Not Valid IP Address
            printer_ip = raw_input('Debe insertar una Dirección IP válida: ')

else:
    # If IP was not provided, we ask for it
    print 'Los argumentos son insuficientes o no fueron pasados (Script - Printer_IP - Project)'
    printer_ip = raw_input('Introduzca la IP de la impresora: ')

    # Check IP readed is valid
    error = True
    while error:
        try:
            # Valid IP Address
            socket.inet_aton(printer_ip)
            error = False

            # stoutput is redirected to a subprocess
            #ipstatus = os.system("ping -n 1 " + printer_ip)
            try:
                ipstatus = subprocess.check_output(
                    ['ping', '-n', '1', printer_ip],
                    stderr=subprocess.STDOUT,  # Get all output
                    universal_newlines=True  # Return string not bytes
                )
                project = raw_input('Introduzca el nombre del Proyecto a consultar: ')

                # Start Session
                s = requests.Session()

                # Load Request
                r = s.get("http://" + printer_ip + ":8080/" + project + ".zup?cmd=exists")

                # Get json info from Request
                info = json.loads(r.text)

                # Handle json info getted
                if info['exists']: print 'El Proyecto ' + project + ' existe en ' + printer_ip
                else: print 'Proyecto ' + project + ' no existe en ' + printer_ip
            except subprocess.CalledProcessError:
                print 'La IP introducida está Offline...'
        except socket.error:
            # Not Valid IP Address
            printer_ip = raw_input('Debe insertar una Dirección IP válida: ')