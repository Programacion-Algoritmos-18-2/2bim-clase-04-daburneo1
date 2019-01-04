from paquete_archivos.miarchivo import MiArchivo, MiArchivoEscribir
from paquete_modelo.mimodelo import Equipo, Operaciones
m = MiArchivo()
m2 = MiArchivoEscribir()

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]


opcion = int(input("Ingrese [1] para ordenar por nombre o [2] para ordenar por campeonatos"))

operacion = Operaciones(lista)
lista2 = operacion.ordenar(opcion)

lista2 = lista2[0:]
for d in lista2:
    e = Equipo(d[0], d[1], d[2], d[3])
    print(e)
    m2.agregar_informacion(e)

m.cerrar_archivo()
m2.cerrar_archivo()