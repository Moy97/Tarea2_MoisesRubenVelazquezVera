from mongoengine import *
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot, QEventLoop
from ventanaEstudiante import Ui_MainWindow


class Estudiantes(Document):
    nombre = StringField(required=True)
    correoElectronico = StringField(required=True)
    contraseña = StringField(required=True)

    def escritura(self, alumno):
        alumno.save()

    def lectura(self, nombre):
        for e in Estudiantes.objects():
            if e.nombre == nombre:
                return e
                break
        return False
        print('No se encuentra ese alumno.')

    def actualizacion(self, nombre, correo, contraseña, nombreLineaEdicion, contraseñaLineaEdicion):
        for e in Estudiantes.objects():
            if e.nombre == nombreLineaEdicion:
                if e.contraseña == contraseñaLineaEdicion:
                    print(f'Nuevos atributos capturados.')
                    e.nombre = nombre
                    e.correoElectronico = correo
                    e.contraseña = contraseña
                    return e
                else:
                    print(f'Contraseña incorrecta, no se puede actualizar.')
                    aviso = (f'Contraseña incorrecta, no se puede actualizar.')
                    retorno = False
                    return retorno, aviso
                break
        print('No se encuentra ese alumno.')
        aviso = (f'No se encuentra ese alumno.')
        retorno = False
        return retorno, aviso

    def eliminar(self, nombre, contraseña):
        aviso = None
        alumnoEncontrado = False
        for e in Estudiantes.objects():
            if e.nombre == nombre:
                alumnoEncontrado = True
                if e.contraseña == contraseña:
                    e.delete()
                    break
                else:
                    aviso = (f'Contraseña incorrecta, no se puede eliminar.')
                    print(f'Contraseña incorrecta, no se puede eliminar.')
                    break
        if not alumnoEncontrado:
            aviso = ('No se encuentra ese alumno.')
            print('No se encuentra ese alumno.')
        return Estudiantes.objects(), aviso


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actualizacionBoton.setCheckable(True)
        self.ui.escrituraBoton.clicked.connect(self.escrituraVentana)
        self.ui.lecturaBoton.clicked.connect(self.lecturaVentana)
        self.ui.actualizacionBoton.clicked.connect(self.actualizacionVentana)
        self.ui.eliminarBoton.clicked.connect(self.eliminarVentana)
        self.loop = QEventLoop()

    @Slot()
    def escrituraVentana(self):
        nombre = self.ui.nombreLineaEdicion.text()
        correo = self.ui.correoLineaEdicion.text()
        contraseña = self.ui.contraseniaLineaEdicion.text()
        alumno = Estudiantes(nombre=nombre, correoElectronico=correo, contraseña=contraseña)
        alumno.escritura(alumno)
        formatoEditorTexto = (f'Nombre: {nombre}\n Correo Electrónico: {correo}')
        self.ui.nombreEditorTexto.setText(formatoEditorTexto)

    @Slot()
    def lecturaVentana(self):
        nombre = ''
        correo = ''
        contraseña = ''
        alumno = Estudiantes(nombre=nombre, correoElectronico=correo, contraseña=contraseña)
        nombre = self.ui.nombreLineaEdicion.text()
        try:
            alumno = alumno.lectura(nombre)
            formatoEditorTexto = (f'Nombre: {alumno.nombre}\n Correo Electrónico: {alumno.correoElectronico}')
            self.ui.nombreEditorTexto.setText(formatoEditorTexto)
        except AttributeError:
            formatoEditorTexto = (f'No se encuentra el alumno: {nombre}')
            self.ui.nombreEditorTexto.setText(formatoEditorTexto)

    @Slot()
    def actualizacionVentana(self):
        nombre = ''
        correo = ''
        contraseña = ''
        alumno = Estudiantes(nombre=nombre, correoElectronico=correo, contraseña=contraseña)
        nombreLineaEdicion = self.ui.nombreLineaEdicion.text()
        contraseñaLineaEdicion = self.ui.contraseniaLineaEdicion.text()
        self.loop.exec_()
        if not self.ui.actualizacionBoton.isChecked():
            try:
                nombre = self.ui.nombreLineaEdicion.text()
                correo = self.ui.correoLineaEdicion.text()
                contraseña = self.ui.contraseniaLineaEdicion.text()
                alumno = alumno.actualizacion(nombre, correo, contraseña, nombreLineaEdicion, contraseñaLineaEdicion)
                alumno.save()
                formatoEditorTexto = (f'Alumno actualizado: {alumno.nombre}\n Correo Electrónico: {alumno.correoElectronico}')
                self.ui.nombreEditorTexto.setText(formatoEditorTexto)
                print(f'Alumno actualizado: {alumno.nombre}\n Correo: {alumno.correoElectronico}')
            except AttributeError:
                retorno, aviso = alumno
                formatoEditorTexto = (f'{aviso}\nActualizacion no realizada')
                self.ui.nombreEditorTexto.setText(formatoEditorTexto)
                print('Actualizacion no realizada')
            print('Esperando')
            self.loop.quit()

    @Slot()
    def eliminarVentana(self):
        nombre = ''
        correo = ''
        contraseña = ''
        alumno = Estudiantes(nombre=nombre, correoElectronico=correo, contraseña=contraseña)
        nombre = self.ui.nombreLineaEdicion.text()
        contraseña = self.ui.contraseniaLineaEdicion.text()
        estudiantes = alumno.eliminar(nombre, contraseña)
        alumnos, aviso = estudiantes
        print('Estudiantes restantes en la lista:')
        restantes = ''
        for e in Estudiantes.objects():
            print(f'{e.nombre} \n')
            restantes += (f'\n - {e.nombre}')
        if aviso == None:
            formatoEditorTexto = (f'Estudiantes restantes en la lista: {restantes}')
        else:
            formatoEditorTexto = (f'{aviso}\n Estudiantes restantes en la lista: {restantes}.')
        self.ui.nombreEditorTexto.setText(formatoEditorTexto)


if __name__ == '__main__':
    connect('padts')
    app = QApplication()
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec_()
