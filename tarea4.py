from mongoengine import *

class Estudiantes(Document):
    nombre = StringField(required=True)
    correoElectronico = StringField(required=True)
    contraseña = StringField(required=True)

    def escritura(self):
        self.nombre = input("Introducir nombre: ")
        self.correoElectronico = input("Introducir correo: ")
        self.contraseña = input("Introducir contraseña: ")

    def lectura(self, nombre):
        for e in Estudiantes.objects():
            if e.nombre == nombre:
                return e
                break
        print('No se encuentra ese alumno.')

    def actualizacion(self, nombre):
        for e in Estudiantes.objects():
            if e.nombre == nombre:
                contraseña = input("Introducir contraseña: ")
                if e.contraseña == contraseña:
                    e.nombre = input("Actualizar nombre: ")
                    e.correoElectronico = input("Actualizar correo: ")
                    e.contraseña = input("Actualizar contraseña: ")
                    return e
                else:
                    print(f'Contraseña incorrecta, no se puede actualizar.')
                    return False
                break
        print('No se encuentra ese alumno.')

    def eliminar(self, nombre):
        alumnoEncontrado = False
        for e in Estudiantes.objects():
            if e.nombre == nombre:
                alumnoEncontrado = True
                contraseña = input("Introducir contraseña: ")
                if e.contraseña == contraseña:
                    e.delete()
                    break
                else:
                    print(f'Contraseña incorrecta, no se puede eliminar.')
                    break
        if not alumnoEncontrado:
            print('No se encuentra ese alumno.')
        return Estudiantes.objects()

if __name__ == '__main__':

    connect('padts')

    nombre = ''
    correo = ''
    contraseña = ''
    alumno = Estudiantes(nombre=nombre, correoElectronico=correo, contraseña=contraseña)

    print("Introducir 5 estudiantes para agragar")
    for i in range(5):
        print(f"Estudiante {i + 1}")
        alumno = Estudiantes(nombre=nombre, correoElectronico=correo, contraseña=contraseña)
        alumno.escritura()
        alumno.save()

    nombre = input("\nIntroducir el nombre del estudiante a buscar: ")
    alumno = alumno.lectura(nombre)
    print(f'Alumno: {alumno.nombre}\n Correo: {alumno.correoElectronico}')

    nombre = input("\nIntroducir el nombre del estudiante a actualizar: ")
    try:
        alumno = alumno.actualizacion(nombre)
        alumno.save()
        print(f'Alumno actualizado: {alumno.nombre}\n Correo: {alumno.correoElectronico}')
    except AttributeError:
        print('Actualizacion no realizada')

    nombre = input("\nIntroducir el nombre del estudiante a eliminar: ")
    estudiantes = alumno.eliminar(nombre)
    print('Estudiantes restantes en la lista:')
    for e in Estudiantes.objects():
        print(f'{e.nombre} \n')
