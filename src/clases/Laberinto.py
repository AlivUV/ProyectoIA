# Laberinto.py

import random

from clases.MarioAmplitud import MarioAmplitud
from clases.MarioCostos import MarioCostos
from clases.MarioAvara import MarioAvara
from clases.MarioA import MarioA

class Laberinto:
  """
  Clase que modela el laberinto que será recorrido por el agente.
  Contiene al agente y una matriz cuadrada simulando el laberinto.
  """
  _mario = None
  _laberinto = []
  _elementos = {}
  _solucion = {}


  def __init__(self, *args: tuple):
    """
    Constructor del laberinto.

    Args:
        args (tuple): Lista con 3 argumentos.
        + Matriz cuadrada (int / list[list[int]]): también puede recibir un entero indicando el tamaño de la matriz
          en cuyo caso la matriz se creará aleatoriamente.
        + Algoritmo: Algoritmo de búsqueda que se utilizará para resolver el laberinto:
          * Búsqueda no informada:
            1. Búsqueda por amplitud (1).
            2. Búsqueda por costos (2).
            3. Búsqueda por profundidad (3).
          * Búsqueda informada:
            4. Búsqueda avara (4).
            5. Búsqueda por A* (5) .
        + Elementos: Objeto con datos de cada elemento en el algoritmo.
    """
    self._elementos = args[2]

    if (len(args) == 3):
      if (isinstance(args[0], int)):
        self._constructorAleatorio(args[0], args[1])
      elif (isinstance(args[0], list)):
        self._constructorDefinido(args[0], args[1])
    else:
      raise Exception("El constructor debe recibir 2 argumentos, pero recibió {}".format(len(args)))


  def _constructorAleatorio(self, tamano: int, algoritmo: int):
    """
    Construye el laberinto con una matriz cuadrada de manera aleatoria.

    Args:
        args (tuple): Lista con 3 argumentos.
        + Matriz cuadrada (int / list[list[int]]): también puede recibir un entero indicando el tamaño de la matriz
          en cuyo caso la matriz se creará aleatoriamente.
        + Algoritmo: Algoritmo de búsqueda que se utilizará para resolver el laberinto:
          * Búsqueda no informada:
            1. Búsqueda por amplitud (1).
            2. Búsqueda por costos (2).
            3. Búsqueda por profundidad (3).
          * Búsqueda informada:
            4. Búsqueda avara (4).
            5. Búsqueda por A* (5).
    """
    algoritmos = [MarioAmplitud, MarioCostos, MarioA, MarioAvara, MarioA]

    self._mario = algoritmos[algoritmo - 1](tamano, self._elementos)

    self._laberinto = [[{}] * tamano for i in range(tamano)]

    muro = self._elementos["muro"]["valor"]

    for i in range(random.randrange(tamano)*random.randrange(tamano)):
      self._laberinto[random.randrange(tamano)][random.randrange(tamano)] = muro

    marioX, marioY = self._mario.getPos()
    self._princesa = (random.randrange(tamano), random.randrange(tamano))
    self._laberinto[marioX][marioY] = self._elementos["mario"]["valor"]
    self._laberinto[self._princesa[0]][self._princesa[1]] = self._elementos["princesa"]["valor"]

    self._mario.buscarSolucion()


  def _constructorDefinido(self, laberinto: list[list[int]], algoritmo: int):
    """
    Construye el laberinto con la matriz cuadrada recibida.
    Recorre la matriz para encontrar el agente y la meta.

    Args:
        args (tuple): Lista con 3 argumentos.
        + Matriz cuadrada (int / list[list[int]]): también puede recibir un entero indicando el tamaño de la matriz
          en cuyo caso la matriz se creará aleatoriamente.
        + Algoritmo: Algoritmo de búsqueda que se utilizará para resolver el laberinto:
          * Búsqueda no informada:
            1. Búsqueda por amplitud (1).
            2. Búsqueda por costos (2).
            3. Búsqueda por profundidad (3).
          * Búsqueda informada:
            4. Búsqueda avara (4).
            5. Búsqueda por A* (5) .
    """
    self._laberinto = [[0] * len(laberinto[0]) for i in range(len(laberinto))]
    algoritmos = [MarioAmplitud, MarioCostos, MarioA, MarioAvara, MarioA]

    for i in range (len(laberinto)):
      for j in range (len(laberinto[0])):
        self._laberinto[i][j] = laberinto[i][j]

        if (laberinto[i][j] == 0):
          self._laberinto[i][j] = 2 - len(self._elementos)
        elif (laberinto[i][j] == self._elementos["mario"]["valor"]):
          self._mario = algoritmos[algoritmo - 1](laberinto, self._elementos)


  def imprimir(self):
    """
    Muestra en pantalla el laberinto en forma de matriz cuadrada.
    """
    for row in self._laberinto:
      print(row)


  def getLaberinto(self):
    """
    Obtiene la matriz cuadrada que simula el laberinto.

    Returns:
        list: Matriz cuadrada de tamaño n con los datos del laberinto.
    """
    return self._laberinto


  def getPos(self, posX: int, posY: int):
    """
    Obtiene el valor en una casilla (X, Y)

    Args:
        posX (int): Posición en X de la casilla.
        posY (int): Posición en Y de la casilla.

    Returns:
        int: Valor de la casilla (X, Y)
    """
    return self._laberinto[posY][posX]


  def setPos(self, posX: int, posY: int, dato: int):
    """
    Cambia el valor en la casilla (X, Y) por el dato recibido.

    Args:
        posX (int): Posición en X de la casilla.
        posY (int): Posición en Y de la casilla.
        dato (int): Nuevo valor.
    """
    self._laberinto[posY][posX] = dato


  def onTic(self):
    """
    Acciones a realizar en cada tic del reloj.
    """
    posMario = list(self._mario.getPos())

    self.setPos(posMario[0], posMario[1], 2 - len(self._elementos))#self.getPos(posMario[0], posMario[1]) - 5)

    movimiento = self._mario.mover()

    posMario[0] += movimiento[0]
    posMario[1] -= movimiento[1]

    self.setPos(posMario[0], posMario[1], self.getPos(posMario[0], posMario[1]) + len(self._elementos))

    return posMario[0] - movimiento[0], posMario[1] + movimiento[1], posMario[0], posMario[1]


  def getSolucion(self):
    return self._mario.getSolucion()