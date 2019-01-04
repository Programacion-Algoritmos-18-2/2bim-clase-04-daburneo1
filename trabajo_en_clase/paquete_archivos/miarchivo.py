import codecs
import sys


class MiArchivo:
    
    def __init__(self):
        self.archivo = codecs.open("data/informacion.csv", "r")

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:
    
    def __init__(self):
        self.archivo = codecs.open("data/informacion_ordenada.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.ciudad,\
                p.campeonatos, p.numJugadores))

    def cerrar_archivo(self):
        self.archivo.close()
