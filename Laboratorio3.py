'''Lopez Camacho Camila Salome
Rospilloso Ramirez Alex Mauricio'''

class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None
        self.set_hijo(hijo)

    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijos.append(hijo)
            if self.hijos is not None:
                for h in self.hijos:
                    h.padre = self

    def get_hijos(self):
        return self.hijos

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    def __str__(self):
        return str(self.get_datos())


def bpa(estado_inicio, estado_solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodos_frontera.append(nodo_inicio)
    tipo_lista = int(input("Introduzca el numero 1 para que se resuelva con una estructura FIFO o numero 2 para que se resuelva con una estructura LIFO "))

    while resuelto == False and len(nodos_frontera) != 0:
        if tipo_lista == 1:
            nodo_actual = nodos_frontera.pop(0)
        if tipo_lista == 2:
            nodo_actual = nodos_frontera.pop()
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            for i in range(len(estado_inicial)-1):
                hijo_datos = nodo_actual.get_datos().copy()
                temp = hijo_datos[i]
                '''Se agrega un if para comprobar si la pieza del rompecabezas ya está en el lugar que pertenece por medio de la variable de
                iteración (i) y asi no tener que crear hijos que muevan piezas que ya estan en su posicion. Si no usamos el if, nuestro
                rompecabezas tendra un maximo de capacidad de resolucion de 7 piezas porque si tendriamos mas piezas el programa tarda mas de
                lo esperado, pero dicha porción de codigo transformaría el archivo en una búsqueda con información
                if temp != i+1:
                    hijo_datos[i] = hijo_datos[i + 1]
                    hijo_datos[i + 1] = temp
                    hijo = Nodo(hijo_datos)'''
                hijo_datos[i] = hijo_datos[i + 1]
                hijo_datos[i + 1] = temp
                hijo = Nodo(hijo_datos)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo)
                    nodos_frontera.append(hijo)

if __name__ == "__main__":
    estado_inicial = [7, 6, 5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5, 6, 7]
    nodo_solucion = bpa(estado_inicial, solucion)

    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)