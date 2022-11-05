# MarioSimple.py

from json import loads
from clases.Mario import Mario

#  Clase que modela a Mario para crear un agente de reflejo simple.
class MarioSimple(Mario):
  """
  Clase que modela un agente simple que intentará resolver un laberinto.
  """
  _movimientos = {}


  def __init__(self, *args: tuple):
    """
    Constructor del Agente.

    Args:
        args (tuple): Lista con 1 o 3 argumentos
        + tam (int): Tamaño de la matriz cuadrada.
        + x (int): Posición en x del agente.
        + y (int): Posición en y del agente.
    """
    super().__init__(*args)
    self._movimientos = loads(open("./src/data/MarioSimple.json").read())


  def mover(self, izquierda: int, arriba: int, derecha: int, abajo: int, queso: int):
    """_summary_

    Args:
        izquierda (int): Información de la casilla a la izquierda de la posición del agente.
        arriba (int): Información de la casilla arriba de la posición del agente.
        derecha (int): Información de la casilla a la derecha de la posición del agente.
        abajo (int): Información de la casilla abajo de la posición del agente.
        queso (int): Posición de la meta.

    Returns:
        tuple: Movimiento realizado por el agente para llegar a la nueva posición
    """
    if (queso == (self._posX, self._posY)):
      print("Comer queso")
      movimiento = (0, 0)
    elif (izquierda == 3):
      print("izquierda")
      movimiento = (-1, 0)
    elif (arriba == 3):
      print("arriba")
      movimiento = (0, 1)
    elif (derecha == 3):
      print("derecha")
      movimiento = (1, 0)
    elif (abajo == 3):
      print("abajo")
      movimiento = (0, -1)
    else:
      movimiento = self._movimientos[str(izquierda) + str(arriba) + str(derecha) + str(abajo)]
      print("I: {}, Ar: {}, D: {}, Ab: {}".format(izquierda, arriba, derecha, abajo))
      print("Del objeto: {}".format(movimiento))
      print("Posición actual: {}".format((self._posX, self._posY)))

    self._posX += movimiento[0]
    self._posY -= movimiento[1]

    print("Nueva posición: {}".format((self._posX, self._posY)))

    return movimiento