# Mario.py
from json import loads
import random

class Mario:
  """
  Clase que modela un agente que intentará resolver un laberinto.
  """
  _posX = 0
  _posY = 0
  _memoria = []


  def __init__(self, *args: tuple):
    """
    Constructor del Agente.

    Args:
        args (tuple): Lista con 1 o 3 argumentos
        + tam (int): Tamaño de la matriz cuadrada.
        + x (int): Posición en x del agente.
        + y (int): Posición en y del agente.
    """
    if (len(args) == 1):
      self._constructorAleatorio(args[0])
    elif (len(args) == 3):
      self._constructorDefinido(args[0], args[1], args[2])
    else:
      raise Exception("El constructor debe recibir 1 o 3 argumentos, pero recibió {}".format(len(args)))


  def _constructorAleatorio(self, tam: int):
    """
    Crea a Mario con posición aleatoria.

    Args:
        tam (int): Tamaño del laberinto cuadrado.
    """
    self._posX = random.randrange(tam)
    self._posY = random.randrange(tam)
    self._memoria = [[0] * tam for i in range(tam)]


  def _constructorDefinido(self, tam: int, x: int, y: int):
    """
    Crea a Mario en la posición xy dada.

    Args:
        tam (int): Tamaño del laberinto cuadrado.
        x (int): Posición en x del agente.
        y (int): Posición en y del agente.
    """
    self._posX = x
    self._posY = y
    self._memoria = [[0] * tam for i in range(tam)]


  def getPos(self):
    """
    Obtiene la posición del agente en el laberinto.

    Returns:
        tuple (int, int): Posición actual (X, Y) del agente en el laberinto.
    """
    return self._posX, self._posY


  def setPos(self, newPosX: int, newPosY: int):
    """
    Cambia el valor de la posición del agente en el laberinto.

    Args:
        newPosX (int): Nueva posición en x del agente.
        newPosY (int): Nueva posición en y del agente.
    """
    self._posX = newPosX
    self._posY = newPosY


  def mover(self):
    """
    Retorna el cambio de posición del agente en el laberinto.

    Función no implementada en la clase padre.
    Para más información ver las clases hijas:
    + MarioSimple.
    """
    return


  def guardarLaberinto(self):
    return