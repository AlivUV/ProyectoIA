# MarioAmplitud.py

from json import loads
from datetime import datetime

from clases.Mario import Mario

class MarioAmplitud (Mario):
  """
  Clase que modela un agente que intentará resolver un laberinto
  revisando todas las posibilidades y encontrando el camino más corto.
  """
  _laberinto = []
  _elementos = {}
  _nodos = []
  _listaEspera = []
  _solucion = {}
  _terminado = False
  _tiempoInicio = 0


  def __init__(self, *args: tuple):
    """
    Constructor del Agente.

    Args:
        args (tuple): Lista con 1 argumento:
        + tamaño (int): Tamaño de la matriz cuadrada.
        + laberinto (list): Matriz cuadrada que contiene los datos del laberinto.
    """
    self._solucion = {
      "total nodos": 0,
      "profundidad": 0,
      "tiempo": 0,
      "camino": []
    }

    self._nodos.clear()
    self._listaEspera.clear()
    self._elementos = args[1]

    if (len(args) != 2):
      raise Exception("El constructor debe recibir 1 argumento, pero recibió {}".format(len(args)))
    elif (isinstance(args[0], int)):
      super().__init__(args[0])
    elif(isinstance(args[0], list)):
      self.definirLaberinto(args[0])
      self.buscarSolucion()


  def definirLaberinto(self, laberinto: list[list[int]]):
    self._laberinto = laberinto
    self._elementos = loads(open('./src/data/estados/elementos.json').read())

    for i in range (len(laberinto)):
      for j in range (len(laberinto[0])):
        if (laberinto[i][j] == self._elementos["mario"]["valor"]):
          self._posX, self._posY = (j, i)


  def buscarSolucion(self):
    '''
    Uso de la inteligencia artificial por amplitud
    para solucionar el problema de Mario en el laberinto.
    '''
    self._tiempoInicio = datetime.now()

    nodoInicial = {
      "padre": None,
      "posicion": len(self._nodos),
      "coordenadas": (self._posX, self._posY)
    }

    self._nodos.append(nodoInicial)
    self._listaEspera.append(nodoInicial)

    while (not self._terminado):
      self._expandir()


  def _expandir(self):
    '''
    Verifica si el nodo es una meta; crea los hijos y los 
    añade a la lista de nodos por expandir.
    '''
    nodoAExpandir = self._evaluarNodoAExpandir()
    coordenadas = self._listaEspera[nodoAExpandir]["coordenadas"]

    if (self._laberinto[coordenadas[1]][coordenadas[0]] != self._elementos["princesa"]["valor"]):
      self._crearHijos(self._listaEspera.pop(nodoAExpandir))
    else:
      self._terminado = True
      print("Nodos creados: {}".format(len(self._nodos)))
      self._crearSolucion(self._listaEspera[nodoAExpandir])
      self._listaEspera.clear()
      self._nodos.clear()
      print("Pasos de la solución: {}".format(len(self._solucion["camino"]) - 1))
      print("Solucion: {}".format(self._solucion["camino"]))


  def _evaluarNodoAExpandir(self):
    ''' 
    Recorre la lista de espera para encontrar el próximo nodo para expandir.
    '''
    return 0


  def _crearHijos(self, nodo: dict):
    '''
    Retorna una lista con los hijos de un nodo determinado.
    '''
    alrededor = self._getAlrededor(nodo["coordenadas"][0], nodo["coordenadas"][1])

    for coordenadas in alrededor:
      if (coordenadas[0] != self._elementos["muro"]["valor"]):
        nuevoNodo = {
          "padre": nodo["posicion"],
          "posicion": len(self._nodos),
          "coordenadas": (coordenadas[1], coordenadas[2])
        }
        self._buscarCiclos(nodo, nuevoNodo)


  def _buscarCiclos(self, ancestro: dict, nodo: dict):
    '''
    Compara un hijo con sus antecesores para no crear un ciclo.
    '''
    if (ancestro["padre"] == None):
      self._nodos.append(nodo)
      self._listaEspera.append(nodo)
    elif (ancestro["coordenadas"] == nodo["coordenadas"]):
      return
    else:
      self._buscarCiclos(self._nodos[ancestro["padre"]], nodo)


  def _crearSolucion(self, nodoFinal: dict):
    '''
    Construye la solución paso por paso devolviéndose por los 
    ancestros del nodo solución.
    '''
    self._solucion["total nodos"] = len(self._nodos)
    self._solucion["tiempo"] = datetime.now() - self._tiempoInicio

    self._solucion["camino"].insert(0, nodoFinal["coordenadas"])
    if (nodoFinal["padre"] != None):
      self._crearSolucion(self._nodos[nodoFinal["padre"]])
    else:
      self._solucion["profundidad"] = len(self._solucion["camino"])


  def getSolucion(self):
    return self._solucion


  def mover(self):
    if (len(self._solucion["camino"]) == 1):
      return (0, 0)

    viejasCoordenadas = self._solucion["camino"].pop(0)

    self._posX, self._posY = self._solucion["camino"][0]

    movimiento = (self._posX - viejasCoordenadas[0], viejasCoordenadas[1] - self._posY)

    return movimiento