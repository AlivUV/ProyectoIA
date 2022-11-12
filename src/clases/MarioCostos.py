# MarioCostos.py

from json import loads
from clases.Mario import Mario

class MarioCostos (Mario):
  """
  Clase que modela un agente que intentará resolver un laberinto
  revisando todas las posibilidades y encontrando el camino más corto.
  """
  _inicio = (0,0)
  _laberinto = []
  _nodos = []
  _listaEspera = []
  _solucion = []
  _terminado = False
  _costoXCasilla = {}
  _accionesPorEstado = []


  def __init__(self, *args: tuple):
    """
    Constructor del Agente.

    Args:
        args (tuple): Lista con 1 argumento:
        + tamaño (int): Tamaño de la matriz cuadrada.
        + laberinto (list): Matriz cuadrada que contiene los datos del laberinto.
    """
    if (len(args) != 1):
      raise Exception("El constructor debe recibir 1 argumento, pero recibió {}".format(len(args)))
    elif (isinstance(args[0], int)):
      super().__init__(args[0])
    elif(isinstance(args[0], list)):
      self.definirLaberinto(args[0])
      self.costos()


  def definirLaberinto(self, laberinto: list):
    self._laberinto = laberinto
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
        if (laberinto[i][j] == 2):
          self._posX, self._posY = (j, i)
          self._inicio = (j, i)


  def costos(self):
    '''
    Uso de la inteligencia artificial por costos
    para solucionar el problema de Mario en el laberinto.
    '''
    nodoInicial = {
      "padre": None,
      "posicion": len(self._nodos),
      "coordenadas": self._inicio,
      "costo": 0,
      "usado": [],
      "estado": {
        "valor": 0
      }
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
    nodoAExpandir = self._evaluarCostos()
    coordenadas = self._listaEspera[nodoAExpandir]["coordenadas"]

    if (self._laberinto[coordenadas[1]][coordenadas[0]] != 6):
      self._crearHijos(self._listaEspera.pop(nodoAExpandir))
    else:
      print("Nodos creados: {}".format(len(self._nodos)))
      print("Costo total: {}".format(self._listaEspera[nodoAExpandir]["costo"]))
      self._terminado = True
      self._crearSolucion(self._listaEspera[nodoAExpandir])
      self._listaEspera.clear()
      print("Pasos de la solución: {}".format(len(self._solucion) - 1))
      print("Solucion: {}".format(self._solucion))


  def _evaluarCostos(self):
    ''' 
    Recorre la lista de espera para encontrar el nodo con el menor costo
    '''
    costo = 1000000
    posicion = 0

    for i in range(len(self._listaEspera)):
      if (self._listaEspera[i]["costo"] < costo):
        costo = self._listaEspera[i]["costo"]
        posicion = i

    return posicion


  def _crearHijos(self, padre):
    '''
    Retorna una lista con los hijos de un nodo determinado.
    '''
    alrededor = self._getAlrededor(padre["coordenadas"][0], padre["coordenadas"][1])

    for coordenadas in alrededor:
      if (coordenadas[0] != 1):
        self._buscarCiclos(padre, self._evaluarEstado(padre, coordenadas))


  def _getAlrededor(self, x: int, y: int):
    '''
    Obtiene los valores de las casillas alrededor de las coordenadas
    XY y lo devuelve en una lista.
    '''
    alrededor = [[1]] * 4

    if (x == 0):
      alrededor[2] = (self._laberinto[y][x + 1], x + 1, y)
    elif (x == len(self._laberinto) - 1):
      alrededor[0] = (self._laberinto[y][x - 1], x - 1, y)
    else:
      alrededor[0] = (self._laberinto[y][x - 1], x - 1, y)
      alrededor[2] = (self._laberinto[y][x + 1], x + 1, y)

    if (y == 0):
      alrededor[3] = (self._laberinto[y + 1][x], x, y + 1)
    elif (y == len(self._laberinto) - 1):
      alrededor[1] = (self._laberinto[y - 1][x], x, y - 1)
    else:
      alrededor[1] = (self._laberinto[y - 1][x], x, y - 1)
      alrededor[3] = (self._laberinto[y + 1][x], x, y + 1)
    return alrededor


  def _buscarCiclos(self, ancestro, nodo):
    '''
    Compara un hijo con sus antecesores para no crear un ciclo.
    '''
    if (ancestro["padre"] == None):
      self._nodos.append(nodo)
      self._listaEspera.append(nodo)
    elif (ancestro["coordenadas"] == nodo["coordenadas"] and ancestro["estado"] == nodo["estado"]):
      return
    else:
      self._buscarCiclos(self._nodos[ancestro["padre"]], nodo)


  def _crearSolucion(self, nodoFinal):
    '''
    Construye la solución paso por paso devolviéndose por los 
    ancestros del nodo solución.
    '''
    self._solucion.insert(0, nodoFinal["coordenadas"])
    if (nodoFinal["padre"] != None):
      self._crearSolucion(self._nodos[nodoFinal["padre"]])


  def _poderUsado(self, padre, coordenadas):
    for casilla in padre["usado"]:
      if (casilla == coordenadas):
        return 0

    return self._laberinto[coordenadas[1]][coordenadas[0]]


  def _evaluarEstado (self, padre, coordenadas: tuple):
    return self._accionesPorEstado[padre["estado"]["valor"]](padre, coordenadas, self._poderUsado(padre, coordenadas[1:]))


  def _estadoGenerico (self, padre, coordenadas: tuple, valorCasilla: int):
    usado = padre["usado"].copy()
    estado = {
      "valor": 0
    }

    if (valorCasilla == 3):
      estado["valor"] = 3
      estado["duracion"] = 6
      usado.extend([coordenadas[1:]])
    elif (valorCasilla == 4):
      estado["valor"] = 3
      estado["cantidad"] = 1
      usado.extend([coordenadas[1:]])

    return {
      "padre": padre["posicion"],
      "posicion": len(self._nodos),
      "coordenadas": coordenadas[1:],
      "costo": padre["costo"] + self._costoXCasilla[str(valorCasilla)],
      "estado": estado,
      "usado": usado
    }


  def _estadoEstrella (self, padre, coordenadas: tuple, valorCasilla: int):
    usado = padre["usado"].copy()
    estado = {
      "valor": 3,
      "duracion": padre["estado"]["duracion"] - 1
    }

    if (valorCasilla == 5):
      usado.extend([coordenadas[1:]])

    if (valorCasilla == 3):
      estado["duracion"] += 6
      usado.extend([coordenadas[1:]])
    elif (estado["duracion"] == 0):
      estado["valor"] = 0

    return {
      "padre": padre["posicion"],
      "posicion": len(self._nodos),
      "coordenadas": coordenadas[1:],
      "costo": padre["costo"] + 0.5,
      "estado": estado,
      "usado": usado
    }


  def _estadoFlor (self, padre, coordenadas: tuple, valorCasilla: int):
    usado = padre["usado"].copy()
    estado = {
      "valor": 4,
      "cantidad": padre["estado"]["cantidad"]
    }
    costo = 1
    cantidad = 0

    if (valorCasilla == 4):
      estado["cantidad"] += 1
      usado.extend([coordenadas[1:]])
    elif (valorCasilla != 5):
      costo = self._costoXCasilla[str(valorCasilla)]
    else:
      estado["cantidad"] -= 1
      estado["valor"] = 4 if (cantidad > 0) else 0
      usado.extend([coordenadas[1:]])

    return {
      "padre": padre["posicion"],
      "posicion": len(self._nodos),
      "coordenadas": coordenadas[1:],
      "costo": padre["costo"] + costo,
      "estado": estado,
      "usado": usado
    }


  def mover(self, *args: tuple):
    if (len(self._solucion) == 1):
      return (0, 0)

    viejasCoordenadas = self._solucion.pop(0)

    self._posX, self._posY = self._solucion[0]

    movimiento = (self._posX - viejasCoordenadas[0], viejasCoordenadas[1] - self._posY)

    return movimiento