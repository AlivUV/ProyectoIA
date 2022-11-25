# MarioA.py

from json import loads
from math import sqrt, pow
from clases.MarioCostos import MarioCostos

class MarioA (MarioCostos):
  """
  Clase que modela un agente que intentará resolver un laberinto
  revisando su distancia a la meta y el costo acumulado
  con el fin de encontrar el camino óptimo.
  """
  _meta = (0, 0)


  def definirLaberinto(self, laberinto: list[list[int]]):
    self._laberinto = laberinto
    self._elementos = loads(open('./src/data/estados/elementos.json').read())
    self._costoXCasilla = loads(open('./src/data/estados/costos.json').read())
    self._accionesPorEstado = [
      self._estadoGenerico,
      self._estadoGenerico,
      self._estadoGenerico,
      self._estadoEstrella,
      self._estadoFlor
    ]

    for i in range (len(laberinto)):
      for j in range (len(laberinto[0])):
        if (laberinto[i][j] == self._elementos["mario"]["valor"]):
          self._posX, self._posY = (j, i)
          self._inicio = (j, i)
        elif (laberinto[i][j] == self._elementos["princesa"]["valor"]):
          self._meta = (j, i)


  def _evaluarNodoAExpandir(self):
    ''' 
    Recorre la lista de espera para encontrar el próximo nodo para expandir.
    '''
    return 0
    heuristica = 1000000
    costo = 1000000
    posicion = 0

    for i in range(len(self._listaEspera)):
      heuristicaNodo = self._evaluarHeuristica(self._listaEspera[i]["coordenadas"])
      costoNodo = self._listaEspera[i]["costo"] + heuristica

      if (heuristicaNodo + costoNodo < heuristica + costo):
        heuristica = heuristicaNodo
        costo = costoNodo
        posicion = i

    return posicion


  def _posicionAnadir(self, nodo, inicio, final):
    '''
    Retorna la posición ideal para añadir el nuevo nodo teniendo en cuenta su costo y heurística.
    '''
    centro = inicio + round((final - inicio) / 2)

    if (final - inicio == 0):
      return inicio

    heuristica = self._evaluarHeuristica(nodo["coordenadas"])
    heuristicaNodo = self._evaluarHeuristica(self._listaEspera[centro]["coordenadas"])

    if (final - inicio == 1 and nodo["costo"] + heuristica < self._listaEspera[centro]["costo"] + heuristicaNodo):
      return inicio
    elif (final - inicio == 1 and nodo["costo"] + heuristica >= self._listaEspera[centro]["costo"] + heuristicaNodo):
      return inicio + 1
    elif (nodo["costo"] + heuristica < self._listaEspera[centro]["costo"] + heuristicaNodo):
      return self._posicionAnadir(nodo, inicio, centro)
    elif (nodo["costo"] + heuristica > self._listaEspera[centro]["costo"] + heuristicaNodo):
      return self._posicionAnadir(nodo, centro, final)
    else:
      return centro + 1


  def _evaluarHeuristica(self, coordenadas: tuple[int]):
    '''
    Recorre la lista de espera para encontrar el nodo más cercano a la meta.
    '''
    dX = coordenadas[0] - self._meta[0]
    dY = coordenadas[1] - self._meta[1]

    return sqrt(pow(dX, 2) + pow(dY, 2)) / (2 * self._pasos)