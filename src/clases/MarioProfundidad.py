# MarioProfundidad.py

from clases.Mario import Mario
from json import loads

class MarioProfundidad(Mario):
    
  """
  Clase que se encarga de modelar un agente que intentará resolver un laberinto
  recorriendo sus ramas (de irzquierda a derecha), expandiendo siempre el nodo
  más profundo del árbol. Dado el caso de que este no tenga más hijos y no sea 
  la meta, se expanden los nodos de niveles menos profundos. Hasta dar con la meta.
  Se evitan los ciclos.
  """

  _laberinto = []
  _elementos = {}
  _nodos = []
  _pila = []
  _solucion = []
  _final = False

  def __init__(self, *args: tuple):

    """
    Constructor del Agente.

    Args:
      args (tuple): Lista con 1 argumento:
      + laberinto (list): Matriz cuadrada que contiene los datos del laberinto.
      + tamaño (int): Tamaño de la matriz cuadrada.
    """
    self._solucion.clear()
    self._nodos.clear()
    self._pila.clear()
    self._elementos = args[1]

    self.definirLaberinto(args[0])
    self.profundidad()


  def definirLaberinto(self, laberinto: list[list[int]]):
    self._laberinto = laberinto
    self._elementos = loads(open('./src/data/estados/elementos.json').read())

    for i in range (len(laberinto)):
      for j in range (len(laberinto[0])):
        if (laberinto[i][j] == self._elementos["mario"]["valor"]):
          self._posX, self._posY = (j, i)

  def profundidad(self):
      
    primerNodo = {
      "padre": None,
      "posicion": len(self._nodos),
      "coordenadas": (self._posX, self._posY)
    }
    
    self._pila.append(primerNodo)
    self._nodos.append(primerNodo)

    while (not self._final):
      coordenadaMario = self._pila[len(self._pila) - 1]["coordenadas"]
      if(len(self._pila) == 0):
        print("Falló")
        self._final = True
      if (self._laberinto[coordenadaMario[1]][coordenadaMario[0]] != self._elementos["princesa"]["valor"]):
        self.expandirHijos(self._pila.pop())
      else:
        print("Lo logró señor, lo logró") 
        self._final = True
        print("Nodos creados: ", (len(self._nodos)))
        self.solucionHallada(self._pila[-1])
        self._pila.clear()
        self._nodos.clear()
        print("Pasos de la solución: ", len(self._solucion) - 1)
        print("Solucion: ", self._solucion)
        
      
  def expandirHijos(self, nodoRecibido):
    posiblesHijos = self.obtenerPosiblesHijos(nodoRecibido["coordenadas"][0], nodoRecibido["coordenadas"][1])
    for coordenadas in posiblesHijos:
      if (coordenadas[0] != self._elementos["muro"]["valor"]):
        siguienteNodo = {
          "padre": nodoRecibido["posicion"],
          "posicion": len(self._nodos),
          "coordenadas": (coordenadas[1], coordenadas[2])
        }
        self.evitarCiclos(nodoRecibido, siguienteNodo)
        #self.eliminarRamaPerdida(self, siguienteNodo)

  def evitarCiclos(self, nodoPadre, nodoHijo):
    if (nodoPadre["padre"] == None):
      self._nodos.append(nodoHijo)
      self._pila.append(nodoHijo)
    elif (nodoPadre["coordenadas"] == nodoHijo["coordenadas"]):
      return
    else:
      self.evitarCiclos(self._nodos[nodoPadre["padre"]], nodoHijo)

  #def eliminarRamaPerdida(self, nodoAnalizar):


  def obtenerPosiblesHijos(self, coordenadaX : int, coordenadaY : int):
    
    # Orden de prioridad => (0: Derecha, 1: Bajar, 2: Izquierda, 3: Subir)

    posiblesHijos = [ [1], [1], [1], [1] ]

    if(coordenadaX == 0):
      posiblesHijos[0] = (self._laberinto[coordenadaY][coordenadaX + 1], coordenadaX + 1, coordenadaY) #Borde izquierdo, mueve hacia la derecha
    elif(coordenadaX == len(self._laberinto) - 1 ):
      posiblesHijos[2] = (self._laberinto[coordenadaY][coordenadaX - 1], coordenadaX - 1, coordenadaY) #Borde derecho, mueve hacia la izquierda
    else: 
      posiblesHijos[0] = (self._laberinto[coordenadaY][coordenadaX - 1], coordenadaX - 1, coordenadaY) #Se encuentra en las columnas
      posiblesHijos[2] = (self._laberinto[coordenadaY][coordenadaX + 1], coordenadaX + 1, coordenadaY) #del medio
    
    if(coordenadaY == 0):
      posiblesHijos[1] = (self._laberinto[coordenadaY + 1][coordenadaX], coordenadaX, coordenadaY + 1) #Borde superior, mueve hacia abajo
    elif(coordenadaY == len(self._laberinto) - 1 ):
      posiblesHijos[3] = (self._laberinto[coordenadaY - 1][coordenadaX], coordenadaX, coordenadaY - 1) #Borde inferior, mueve hacia arriba
    else:
      posiblesHijos[1] = (self._laberinto[coordenadaY + 1][coordenadaX], coordenadaX, coordenadaY + 1) #Se encuentra en las filas
      posiblesHijos[3] = (self._laberinto[coordenadaY - 1][coordenadaX], coordenadaX, coordenadaY - 1) #del medio
    return posiblesHijos
  
  def solucionHallada(self, ultimoNodo):

    self._solucion.insert(0, ultimoNodo["coordenadas"])
    if (ultimoNodo["padre"] != None):
      self.solucionHallada(self._nodos[ultimoNodo["padre"]])

  def mover(self, *args: tuple):
    if (len(self._solucion) == 1):
      return (0, 0)

    viejasCoordenadas = self._solucion.pop()

    self._posX, self._posY = self._solucion[self._solucion.index(viejasCoordenadas)]

    movimiento = (self._posX - viejasCoordenadas[0], viejasCoordenadas[1] - self._posY)

    return movimiento





