class Equipo(object):

    def __init__(self, n, c, cam, nj):
    #Atributos de estudiante con los valores enviados desde el archivo
        self.nombre = n
        self.ciudad = c
        self.campeonatos = int(cam)
        self.numJugadores = int(nj)
    #Metodos agregar y obtener
    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_ciudad(self, c):
        self.ciudad = c
    
    def obtener_ciudad(self):
        return self.ciudad

    def agregar_campeonatos(self, cam):
        self.campeonatos = int(cam)

    def obtener_campeonatos(self):
        return self.campeonatos
    
    def agregar_numJugadores(self, nj):
        self.numJugadores = int(nj)

    def obtener_numJugadores(self):
        return self.numJugadores

    def __str__(self): #equivalente al toString en java, para visualizar los metodos como tal
        return "%s - %s - %d - %d" % (self.nombre, self.ciudad, self.campeonatos, self.numJugadores)

    def __repr__(self): #representacion de objetos, el sorted hace referencia a este medoto
        return "%s - %s - %d - %d" % (self.nombre, self.ciudad, self.campeonatos, self.numJugadores)


class Operaciones(object):
    
    def __init__(self, listado): #Recibe el listado
        self.listado_equipos = listado

    def ordenar(self, op): #Recibe la opcion ingresada por el usuario en op
        opcion = op #Se crea la variable con el valor de op
        """
            https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
        """
        #Condiciones para ordenar por nombre o campeonatos

        if opcion == 1:
            return sorted(self.listado_equipos, key=lambda equipo: equipo.nombre) #poner el __repr__     
        
        if opcion == 2:
            return sorted(self.listado_equipos, key=lambda equipo: equipo.campeonatos)