from paquete_archivos.miarchivo import MiArchivo, MiArchivoEscribir
from paquete_modelo.mimodelo import Equipo, Operaciones

m = MiArchivo()
m2 = MiArchivoEscribir()

#Leer la informacion del archivo separandolos por el |
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

lista_e = [] #se crea una lista vacia
#Se envian los datos a Equipo para convertirlos en datos tipo Equipo
for d in lista:
	e = Equipo(d[0], d[1], d[2], d[3])
	lista_e.append(e)
#Mensaje que se presenta al usuario para que seleccione de que forma desea ordenar los datos
opcion = int(input("Ingrese [1] para ordenar por nombre o [2] para ordenar por campeonatos"))
#Se crea el objeto 
operacion = Operaciones(lista_e)
#Se envian los datos tipo Equipo para que sean ordenados
lista2 = operacion.ordenar(opcion)


lista2 = lista2[0:]
for d in lista2:
    print(d)#Presentar los datos
    m2.agregar_informacion(d) #Crea y agrega la informacion al nuevo archivo

#Cierran los dos archivos
m.cerrar_archivo()
m2.cerrar_archivo()