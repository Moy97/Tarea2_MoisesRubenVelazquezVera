from StudentIO import studentIO

nombre = ''
correo = ''
contraseña = ''
diccionarioGuardar = {}

print("Introducir 5 estudiantes para agragar")
for i in range(5):
    print(f"Estudiante {i+1}")
    alumno = studentIO.Estudiante(nombre, correo, contraseña)
    alumno.ingresarAtributos()
    studentIO.guardarEstudantesShelve(alumno)
    diccionarioGuardar[alumno.obtenerNombre()] = alumno
    # print(diccionarioGuardar)
studentIO.guardarEstudiantesPickle(diccionarioGuardar)

nombre = input("\nIntroducir el nombre del estudiante a buscar: ")
alumnoLeido = studentIO.leerEstudiantesPickle(nombre)
print(alumnoLeido.obtenerAtributos())
studentIO.leerEstudiantesShelve(nombre)
alumnoLeido = studentIO.leerEstudiantesShelve(nombre)
print(alumnoLeido.obtenerAtributos())

print("\nIntroducir el estudiante a añadir para actualizar")
alumno = studentIO.Estudiante(nombre, correo, contraseña)
alumno.ingresarAtributos()
nombre = input("\nIntroducir el nombre del estudiante a eliminar para actualizar: ")
print("Lista Pickle")
studentIO.actualizarEstudiantesPickle(alumno, nombre)
print("Lista Shelve")
studentIO.actualizarEstudiantesShelve(alumno, nombre)





