import re

def validarCorreo():
    correo = input("Introducir correo electrónico: ")
    patronD1E = r'[\w.-]+@[\w]+\.[a-z]+$'
    patronD2E = r'[\w.-]+@[\w]+\.[a-z]+\.[a-z]+$'
    patronSDE = r'[\w.-]+@[\w]+\.[a-z]+\.[a-z]+$'
    coincidenciaCorreo1 = re.match(patronD1E, correo)
    coincidenciaCorreo2 = re.match(patronD2E, correo)
    coincidenciaCorreo3 = re.match(patronSDE, correo)
    if(coincidenciaCorreo1):
        print('Valido')
    elif(coincidenciaCorreo2):
        print('Valido')
    elif(coincidenciaCorreo3):
        print('Valido')
    else:
        print('No valido')

def validarNumeroTelefonico():
    numero = input("Introducir numero telefonico: ")
    patron10D = r'[\d]{10}$'
    patronL2P = r'[(]{1}[\d]{2}[)]{1}[\d]{8}$'
    patronL3P = r'[(]{1}[\d]{3}[)]{1}[\d]{7}$'
    patronG1 = r'[(]{1}[\d]{2}[)]{1}[-]{1}[\d]{4}[-]{1}[\d]{4}$'
    patronG2 = r'[(]{1}[\d]{3}[)]{1}[-]{1}[\d]{3}[-]{1}[\d]{4}$'
    patronS1 = r'[(]{1}[\d]{2}[)]{1}[ ]{1}[\d]{4}[ ]{1}[\d]{4}$'
    patronS2 = r'[(]{1}[\d]{3}[)]{1}[ ]{1}[\d]{3}[ ]{1}[\d]{4}$'
    coincidenciaNumero1 = re.match(patron10D, numero)
    coincidenciaNumero2 = re.match(patronL2P, numero)
    coincidenciaNumero3 = re.match(patronL3P, numero)
    coincidenciaNumero4 = re.match(patronG1, numero)
    coincidenciaNumero5 = re.match(patronG2, numero)
    coincidenciaNumero6 = re.match(patronS1, numero)
    coincidenciaNumero7 = re.match(patronS2, numero)
    if (coincidenciaNumero1):
        print('Valido')
    elif (coincidenciaNumero2):
        print('Valido')
    elif (coincidenciaNumero3):
        print('Valido')
    elif (coincidenciaNumero4):
        print('Valido')
    elif (coincidenciaNumero5):
        print('Valido')
    elif (coincidenciaNumero6):
        print('Valido')
    elif (coincidenciaNumero7):
        print('Valido')
    else:
        print('No valido')

def validarRFC():
    rfc = input("Introducir RFC: ")
    patronRFC = r'[A-Z]{4}[0-9]{6}[0-9A-Z]{3}$'
    coincidenciaRFC = re.match(patronRFC, rfc)
    if (coincidenciaRFC):
        print('Valido')
    else:
        print('No valido')

def validarCURP():
    curp = input("Introducir CURP: ")
    patronCURPH = r'[A-Z]{4}[0-9]{6}[H]{1}[A-Z]{5}[0-9]{2}$'
    patronCURPM = r'[A-Z]{4}[0-9]{6}[M]{1}[A-Z]{5}[0-9]{2}$'
    coincidenciaCURPH = re.match(patronCURPH, curp)
    coincidenciaCURPM = re.match(patronCURPM, curp)
    if (coincidenciaCURPH):
        print('Valido')
    if (coincidenciaCURPM):
        print('Valido')
    else:
        print('No valido')

while True:
    validarCorreo()
    validarNumeroTelefonico()
    validarRFC()
    validarCURP()
