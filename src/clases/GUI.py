# GUI.py

import pygame
import time
from json import loads

from clases.Laberinto import Laberinto

class GUI():
  """
  Clase que genera el modelo gráfico en 2D del laberinto.
  """
  _screenWidth = 0
  _screenHeight = 0
  _abierto = False
  _tam = 0
  _anchoCasilla = 0
  _altoCasilla = 0
  _surface = None
  _muro = None
  _laberinto = None
  _mario = None
  _koopa = None
  _flor = None
  _estrella = None
  _princesa = None
  _lineWidth = 1
  _solucion = {}

  def __init__(self, *args):
    """
    Constructor de la interfaz gráfica.

    Args:
        * args (tuple): Lista con 2 argumentos y 2 opcionales:
          + Matriz cuadrada (int / list[list[int]]): También puede recibir un entero indicando el tamaño de la matriz
            en cuyo caso la matriz se creará aleatoriamente.
          + Algoritmo (int): Algoritmo de búsqueda que se utilizará para resolver el laberinto:
            - Búsqueda no informada:
              1. Búsqueda por amplitud.
              2. Búsqueda por costos.
              3. Búsqueda por profundidad.
            - Búsqueda informada:
              4. Búsqueda avara.
              5. Búsqueda por A*.
          + Elementos (dict): Objeto con datos de cada elemento en el algoritmo.
          + Ancho (width: int = opcional): También puede recibir un entero indicando el tamaño de la matriz
            en cuyo caso la matriz se creará aleatoriamente.
          + Largo (heigth: int = opcional) También puede recibir un entero indicando el tamaño de la matriz
            en cuyo caso la matriz se creará aleatoriamente.

    """
    if (len(args) == 2):
      if (isinstance(args[0], int)):
        self._constructorAleatorio(args[0], args[1])
      elif (isinstance(args[0], list)):
        self._constructorDefinido(args[0], args[1])
      else:
        raise Exception(
          "El tipo de dato {} no es una entrada válida.".format(type(args[0])))
    else:
      if (isinstance(args[0], int)):
        self._constructorAleatorio(
          args[0], args[1],width = args[2], height = args[3])
      elif (isinstance(args[0], list)):
        self._constructorDefinido(
          args[0], args[1], width = args[2], height = args[3])
      else:
        raise Exception(
          "El tipo de dato {} no es una entrada válida.".format(type(args[0])))

  def _constructorAleatorio(self, tamano: int, algoritmo: int, width: int = 900, height: int = 900):
    """
    Construye la ventana con la cuadrícula y los elementos del laberinto
    creados de manera aleatoria.

    Args:
      + tamano (int): Tamaño de la matriz cuadrada.
      + Algoritmo (int): Algoritmo de búsqueda que se utilizará para resolver el laberinto:
        * Búsqueda no informada:
          1. Búsqueda por amplitud (1).
          2. Búsqueda por costos (2).
          3. Búsqueda por profundidad (3).
        * Búsqueda informada:
          4. Búsqueda avara (4).
          5. Búsqueda por A* (5).
      + width (int opcional): Ancho de la ventana. Defaults to 900.
      + height (int opcional): Alto de la ventana. Defaults to 900.
    """
    self._elementos = loads(open('./src/data/estados/elementos.json').read())

    self._screenWidth = width * 0.9
    self._screenHeight = height * 0.9

    self._tam = width * 0.9 / tamano
    self._anchoCasilla = width * 0.9 / tamano
    self._altoCasilla = width * 0.9 / tamano

    self._laberinto = Laberinto(tamano, algoritmo, self._elementos)

    self._crearVentana(width, height)

    self._cargarImagenes()

    self._pintarLaberinto()

  def _constructorDefinido(self, matriz: list[list[int]], algoritmo: int, width: int = 900, height: int = 900):
    """
    Construye la ventana con la cuadrícula y los elementos del laberinto.

    Args:
      + tamano (int): Tamaño de la matriz cuadrada.
      + Algoritmo (int): Algoritmo de búsqueda que se utilizará para resolver el laberinto:
        * Búsqueda no informada:
          1. Búsqueda por amplitud (1).
          2. Búsqueda por costos (2).
          3. Búsqueda por profundidad (3).
        * Búsqueda informada:
          4. Búsqueda avara (4).
          5. Búsqueda por A* (5).
      + width (int opcional): Ancho de la ventana. Defaults to 900.
      + height (int opcional): Alto de la ventana. Defaults to 900.
    """
    self._elementos = loads(open('./src/data/estados/elementos.json').read())

    self._laberinto = Laberinto(matriz, algoritmo, self._elementos)

    self._tam = width * 0.9 / len(matriz)
    self._anchoCasilla = width * 0.9 / len(matriz[0])
    self._altoCasilla = width * 0.9 / len(matriz)

    self._crearVentana(width, height)

    self._cargarImagenes()

    self._pintarLaberinto()


  def _crearVentana(self, width: int, height: int):
    """
    Crea la ventana en donde se pintará el laberinto con sus elementos.

    Args:
      width (int optional): Ancho de la ventana. Defaults to 900.
      height (int optional): Alto de la ventana. Defaults to 900.
    """

    self._screenWidth = width * 0.9
    self._screenHeight = height * 0.9

    self._surface = pygame.display.set_mode((width, height))

    self._surface.fill("light blue")


  def _cargarImagenes(self):
    """
    Carga las imágenes para graficar el laberinto.
    """
    self._elementos["muro"]["imagen"] = pygame.image.load("./src/resources/muro.png")
    self._elementos["muro"]["imagen"] = pygame.transform.scale(
      self._elementos["muro"]["imagen"], (self._anchoCasilla, self._altoCasilla)
    )

    self._elementos["mario"]["imagen"] = pygame.image.load("./src/resources/mario.png")
    self._elementos["mario"]["imagen"] = pygame.transform.scale(
      self._elementos["mario"]["imagen"], (self._anchoCasilla * 0.9, self._altoCasilla * 0.9)
    )

    self._elementos["princesa"]["imagen"] = pygame.image.load("./src/resources/princesa.png")
    self._elementos["princesa"]["imagen"] = pygame.transform.scale(
      self._elementos["princesa"]["imagen"], (self._anchoCasilla * 0.9, self._altoCasilla * 0.9)
    )

    self._elementos["estrella"]["imagen"] = pygame.image.load("./src/resources/estrella.png")
    self._elementos["estrella"]["imagen"] = pygame.transform.scale(
      self._elementos["estrella"]["imagen"], (self._anchoCasilla * 0.9, self._altoCasilla * 0.9)
    )

    self._elementos["koopa"]["imagen"] = pygame.image.load("./src/resources/koopa.png")
    self._elementos["koopa"]["imagen"] = pygame.transform.scale(
      self._elementos["koopa"]["imagen"], (self._anchoCasilla * 0.9, self._altoCasilla * 0.9)
    )

    self._elementos["flor"]["imagen"] = pygame.image.load("./src/resources/flor.png")
    self._elementos["flor"]["imagen"] = pygame.transform.scale(
      self._elementos["flor"]["imagen"], (self._anchoCasilla * 0.9, self._altoCasilla * 0.9)
    )


  def _pintarLaberinto(self):
    """
    Grafica el laberinto con sus elementos.
    """

    for i in range(len(self._laberinto.getLaberinto())):
      for j in range(len(self._laberinto.getLaberinto()[0])):
        self._pintarCasilla(j, i, self._laberinto.getLaberinto()[i][j])

    self._pintarBorde()

    pygame.display.update()


  def _pintarBorde(self):
    """
    Dibuja el rectángulo que delimita el laberinto.
    """
    pygame.draw.rect(self._surface, "black", (self._screenWidth * 0.05, self._screenHeight *
                     0.05, self._screenWidth, self._screenHeight), self._lineWidth * 2)

  def _pintarCasilla(self, x: int, y: int, tipo: int):
    """
    Dibuja cada casilla del laberinto dependiendo de su contenido

    Args:
      x (int): Posición de la casilla en X. 
      y (int): Posición de la casilla en Y.
      tipo (int): Contenido de la casilla.
    """
    if (tipo == self._elementos["muro"]["valor"]):
      "Muro"
      self._pintarElemento(self._elementos["muro"]["imagen"], x, y, 1)

    elif (tipo == self._elementos["mario"]["valor"]):
      "Mario"
      self._pintarElemento(self._elementos["mario"]["imagen"], x, y)

    elif (tipo == self._elementos["estrella"]["valor"]):
      "Estrella"
      self._pintarElemento(self._elementos["estrella"]["imagen"], x, y)

    elif (tipo == self._elementos["flor"]["valor"]):
      "Flor"
      self._pintarElemento(self._elementos["flor"]["imagen"], x, y)

    elif (tipo == self._elementos["koopa"]["valor"]):
      "Koopa"
      self._pintarElemento(self._elementos["koopa"]["imagen"], x, y)

    elif (tipo == self._elementos["princesa"]["valor"]):
      "Peach"
      self._pintarElemento(self._elementos["princesa"]["imagen"], x, y)

    elif (tipo == self._elementos["estrella"]["valor"] + len(self._elementos)):
      "Mario encuentra una estrella"
      self._pintarElemento(self._elementos["mario"]["imagen"], x, y)

    elif (tipo == self._elementos["flor"]["valor"] + len(self._elementos)):
      "Mario encuentra una flor"
      self._pintarElemento(self._elementos["mario"]["imagen"], x, y)

    elif (tipo == self._elementos["koopa"]["valor"] + len(self._elementos)):
      "Mario encuentra un Koopa"
      self._pintarElemento(self._elementos["mario"]["imagen"], x, y)

    elif (tipo == self._elementos["princesa"]["valor"] + len(self._elementos)):
      "Mario encuentra a Peach"
      self._pintarFinal(x, y)

    else:
      self._pintarCasillaVacia(x, y)

  def _pintarCasillaVacia(self, x: int, y: int):
    """
    Dibuja una casilla sin elementos.

    Args:
      x (int): Posición de la casilla en X. 
      y (int): Posición de la casilla en Y.
    """
    pygame.draw.rect(self._surface, "white", (self._screenWidth * 0.05 + self._anchoCasilla *
                     x, self._screenHeight * 0.05 + self._altoCasilla * y, self._anchoCasilla, self._altoCasilla))
    pygame.draw.rect(self._surface, "dark gray", (self._screenWidth * 0.05 + self._anchoCasilla * x,
                     self._screenHeight * 0.05 + self._altoCasilla * y, self._anchoCasilla, self._altoCasilla), self._lineWidth)

  def _pintarElemento(self, elem, x: int, y: int, tam: float = 0.9):
    """
    Dibuja la casilla que contiene la princesa.

    Args:
      x (int): Posición de la casilla en X. 
      y (int): Posición de la casilla en Y.
    """
    self._pintarCasillaVacia(x, y)

    self._surface.blit(elem, (self._screenWidth * 0.05 + self._anchoCasilla * ((1 - tam) / 2) +
                       self._anchoCasilla * x, self._screenHeight * 0.05 + self._altoCasilla * ((1 - tam) / 2) + self._altoCasilla * y))

  def _pintarFinal(self, x: int, y: int):
    """
    Dibuja la casilla donde el agente y la meta se encuentran.

    Args:
        x (int): Posición de la casilla en X. 
        y (int): Posición de la casilla en Y.
    """
    self._pintarCasillaVacia(x, y)

    self._surface.blit(self._elementos["princesa"]["imagen"], (self._screenWidth * 0.05 + self._anchoCasilla * 0.05 +
                       self._anchoCasilla * x, self._screenHeight * 0.05 + self._altoCasilla * 0.05 + self._altoCasilla * y))
    self._surface.blit(self._elementos["mario"]["imagen"], (self._screenWidth * 0.05 + self._anchoCasilla * 0.05 +
                       self._anchoCasilla * x, self._screenHeight * 0.05 + self._altoCasilla * 0.05 + self._altoCasilla * y))

  def _manejarEventos(self):
    """
    Define las acciones a realizar al suceder eventos dentro de la ventana.
    """
    for event in pygame.event.get():
      if (event.type == pygame.QUIT):
        self._abierto = False
        pygame.display.quit()
        pygame.quit()

  def iniciar(self):
    """
    Da inicio al movimiento del agente.
    """
    self._abierto = True

    while self._abierto:
      self._manejarEventos()

      self._mover(self._laberinto.onTic())

      time.sleep(1)


  def getSolucion(self):
    return self._laberinto.getSolucion()


  def _mover(self, casillas: tuple[int]):
    """
    Si hay un movimiento del agente, repinta las dos casillas que cambiaron de contenido.

    Args:
        casillas (tuple(int)): Posiciones en X y Y de las casillas con cambios.
    """
    if (casillas[0] == casillas[2] and casillas[1] == casillas[3]):
        self._abierto = False
    else:
      self._pintarCasilla(casillas[0], casillas[1], self._laberinto.getLaberinto()[
                          casillas[1]][casillas[0]])
      self._pintarCasilla(casillas[2], casillas[3], self._laberinto.getLaberinto()[
                          casillas[3]][casillas[2]])

      self._pintarBorde()

      pygame.display.update()
