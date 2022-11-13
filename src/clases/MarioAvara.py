# MarioAvara.py

from math import sqrt, pow

from clases.MarioAmplitud import MarioAmplitud

class MarioAvara (MarioAmplitud):
  """
  Clase que modela un agente que intentará resolver un laberinto
  revisando su distancia a la meta y encontrando el camino más corto.
  """
  _meta = (0, 0)


  def definirLaberinto(self, laberinto: list):
    self._laberinto = laberinto

    for i in range (len(laberinto)):
      for j in range (len(laberinto[0])):
        if (laberinto[i][j] == 2):
          self._posX, self._posY = (j, i)
          self._inicio = (j, i)
        elif (laberinto[i][j] == 6):
          self._meta = (j, i)


  def _evaluarNodoAExpandir(self):
    ''' 
    Recorre la lista de espera para encontrar el próximo nodo para expandir.
    '''
    heuristica = 1000000
    posicion = 0

    for i in range(len(self._listaEspera)):
      heuristicaNodo = self._evaluarHeuristica(self._listaEspera[i]["coordenadas"])
      if (heuristicaNodo < heuristica):
        heuristica = heuristicaNodo
        posicion = i

    return posicion


  def _evaluarHeuristica(self, coordenadas: tuple):
    '''
    Recorre la lista de espera para encontrar el nodo más cercano a la meta.
    '''
    dX = coordenadas[0] - self._meta[0]
    dY = coordenadas[1] - self._meta[1]

    return dX + dY