try:
    import cPickle as pickle
except ImportError:
    import pickle

import shelve

class Estudiante:
    _nombre = ''
    _correoElectronico = ''
    _contraseña = ''

    def __init__(self, nombre, correoElectronico, contraseña):
        self._nombre = nombre
        self._correoElectronico = correoElectronico
        self._contraseña = contraseña

    def ingresarAtributos(self):
        self._nombre = input("Introducir nombre: ")
        self._correoElectronico = input("Introducir correo: ")
        self._contraseña = input("Introducir contraseña: ")

    def obtenerAtributos(self):
        return (self._nombre, self._correoElectronico, self._contraseña)

    def obtenerNombre(self):
        return (self._nombre)

    def __str__(self):
        return f'Nombre: {self._nombre}\n' \
               f'Correo Electronico: {self._correoElectronico}\n'

def guardarEstudiantesPickle(diccionarioGuardar):
    file = open('students.db', 'wb')
    pickle.Pickler(file, 4).dump(diccionarioGuardar)
    file.close()

def guardarEstudantesShelve(alumno):
    nombre = alumno.obtenerNombre()
    with shelve.open('students') as shelf:
        shelf[nombre] = alumno
        shelf.close()

def leerEstudiantesPickle(nombre):
    file = open('students.db', 'rb')
    diccionarioLeer = pickle.load(file)
    alumnoLeido = diccionarioLeer[nombre]
    file.close()
    print(alumnoLeido)
    return alumnoLeido

def leerEstudiantesShelve(nombre):
    with shelve.open('students') as shelf:
        alumnoLeido = shelf[nombre]
        shelf.close()
    print(alumnoLeido)
    return alumnoLeido

def actualizarEstudiantesPickle(alumno, nombre):
    file = open('students.db', 'rb')
    diccionarioActualizar = pickle.load(file)
    file.close()
    diccionarioActualizar[alumno.obtenerNombre()] = alumno
    del diccionarioActualizar[nombre]
    file = open('students.db', 'wb')
    pickle.Pickler(file, 4).dump(diccionarioActualizar)
    file.close()
    file = open('students.db', 'rb')
    diccionarioActualizado = pickle.load(file)
    file.close()
    for i in diccionarioActualizado:
        print(diccionarioActualizado[i])

def actualizarEstudiantesShelve(alumno, nombre):
    with shelve.open('students') as shelf:
        del shelf[nombre]
        nombre = alumno.obtenerNombre()
        shelf[nombre] = alumno
        for k in shelf:
            print(shelf[k])
        shelf.close()
