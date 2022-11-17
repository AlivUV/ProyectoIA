# Laberinto.py
import random
from clases.MarioSimple import MarioSimple
from clases.MarioAmplitud import MarioAmplitud

class Laberinto:
  """
  Clase que modela el laberinto que será recorrido por el agente.
  Contiene al agente y una matriz cuadrada simulando el laberinto.
  """
  _mario = None
  _princesa = ()
  _laberinto = []


  def __init__(self, *args: tuple):
    """
    Constructor del laberinto.

    Args:
        args (tuple): Lista con 1 argumento.
        + Matriz cuadrada, también puede recibir un entero indicando el tamaño de la matriz
          en cuyo caso la matriz se creará aleatoriamente.
    """
    if (len(args) == 1):
      if (isinstance(args[0], int)):
        self._constructorAleatorio(args[0])
      elif (isinstance(args[0], list)):
        self._constructorDefinido(args[0])
    else:
      raise Exception("El constructor debe recibir 1 argumento, pero recibió {}".format(len(args)))


  def _constructorAleatorio(self, tamano: int):
    """
    Construye el laberinto con una matriz cuadrada de manera aleatoria.

    Args:
        tamano (int): Tamaño de la matriz cuadrada.
    """
    self._mario = MarioSimple(tamano)

    self._laberinto = [[{}] * tamano for i in range(tamano)]

    for i in range(random.randrange(tamano)*random.randrange(tamano)):
      self._laberinto[random.randrange(tamano)][random.randrange(tamano)] = 1

    marioX, marioY = self._mario.getPos()
    self._princesa = (random.randrange(tamano), random.randrange(tamano))
    self._laberinto[marioX][marioY] = 2
    self._laberinto[self._princesa[0]][self._princesa[1]] = 6


  def _constructorDefinido(self, laberinto: list[list[int]]):
    """
    Construye el laberinto con la matriz cuadrada recibida.
    Recorre la matriz para encontrar el agente y la meta.

    Args:
        laberinto (list[list[int]]): Matriz cuadrada con los datos del nuevo laberinto.
    """
    self._laberinto = [[{}] * len(laberinto) for i in range(len(laberinto))]

    for i in range (len(laberinto)):
      for j in range (len(laberinto[0])):
        self._laberinto[i][j] = laberinto[i][j]

        if (laberinto[i][j] == 2):
          self._mario = MarioAmplitud(laberinto)
        elif (laberinto[i][j] == 6):
          self._princesa = (j, i)


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


  def getAlrededor(self, posX: int, posY: int):
    """
    Obtiene los datos en la casilla contigua a cada una de las cuatro direcciones de la posición (X, Y).

    Args:
        posX (int): Posición en X de la casilla.
        posY (int): Posición en Y de la casilla.

    Returns:
        list[int]: información de las 4 casillas contiguas.
    """
    alrededor = [0] * 4

    if (posX == 0):
      alrededor[0] = 1
      alrededor[2] = self._laberinto[posY][posX + 1]
    elif (posX == len(self._laberinto) - 1):
      alrededor[0] = self._laberinto[posY][posX - 1]
      alrededor[2] = 1
    else:
      alrededor[0] = self._laberinto[posY][posX - 1]
      alrededor[2] = self._laberinto[posY][posX + 1]

    if (posY == 0):
      alrededor[1] = 1
      alrededor[3] = self._laberinto[posY + 1][posX]
    elif (posY == len(self._laberinto) - 1):
      alrededor[1] = self._laberinto[posY - 1][posX]
      alrededor[3] = 1
    else:
      alrededor[1] = self._laberinto[posY - 1][posX]
      alrededor[3] = self._laberinto[posY + 1][posX]

    return alrededor


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
    alrededor = self.getAlrededor(posMario[0], posMario[1])

    self.setPos(posMario[0], posMario[1], self.getPos(posMario[0], posMario[1]) - 2)

    movimiento = self._mario.mover(alrededor[0], alrededor[1], alrededor[2], alrededor[3], self._princesa)

    posMario[0] += movimiento[0]
    posMario[1] -= movimiento[1]

    self.setPos(posMario[0], posMario[1], self.getPos(posMario[0], posMario[1]) + 2)

    return posMario[0] - movimiento[0], posMario[1] + movimiento[1], posMario[0], posMario[1]