# GUI.py
from clases.Laberinto import Laberinto
import pygame
import time


class GUI():
  """
  Clase que genera el modelo gráfico en 2D del laberinto.
  """
  _screenWidth = 0
  _screenHeight = 0
  _abierto = False
  _tam = 0
  _surface = None
  _muro = None
  _laberinto = None
  _mario = None
  _koopa = None
  _flor = None
  _estrella = None
  _princesa = None
  _lineWidth = 1

  def __init__(self, *args):
    """
    Constructor de la interfaz gráfica.

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
        raise Exception(
          "El tipo de dato {} no es una entrada válida.".format(type(args[0])))
    else:
      if (isinstance(args[0], int)):
        self._constructorAleatorio(
          args[0], width=args[1], height=args[2])
      elif (isinstance(args[0], list)):
        self._constructorDefinido(
          args[0], width=args[1], height=args[2])
      else:
        raise Exception(
          "El tipo de dato {} no es una entrada válida.".format(type(args[0])))

  def _constructorAleatorio(self, tamano: int, width: int = 900, height: int = 900):
    """
    Construye la ventana con la cuadrícula y los elementos del laberinto
    creados de manera aleatoria.

    Args:
      tamano (int): Tamaño de la matriz cuadrada.
      width (int optional): Ancho de la ventana. Defaults to 900.
      height (int optional): Alto de la ventana. Defaults to 900.
    """
    self._screenWidth = width * 0.9
    self._screenHeight = height * 0.9

    self._tam = width * 0.9 / tamano

    self._laberinto = Laberinto(tamano)

    self._pintarLaberinto()

  def _constructorDefinido(self, matriz: list[list[int]], width: int = 900, height: int = 900):
    """
    Construye la ventana con la cuadrícula y los elementos del laberinto.

    Args:
      matriz (list): Matriz cuadrada con los datos del nuevo laberinto.
      width (int optional): Ancho de la ventana. Defaults to 900.
      height (int optional): Alto de la ventana. Defaults to 900.
    """
    self._laberinto = Laberinto(matriz)

    self._tam = width * 0.9 / len(matriz)

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
    self._muro = pygame.image.load("./src/resources/muro.png")
    self._muro = pygame.transform.scale(
      self._muro, (self._tam * 0.9, self._tam * 0.9)
    )

    self._mario = pygame.image.load("./src/resources/mario.png")
    self._mario = pygame.transform.scale(
      self._mario, (self._tam * 0.9, self._tam * 0.9)
    )

    self._princesa = pygame.image.load("./src/resources/princesa.png")
    self._princesa = pygame.transform.scale(
      self._princesa, (self._tam * 0.9, self._tam * 0.9)
    )

    self._estrella = pygame.image.load("./src/resources/estrella.png")
    self._estrella = pygame.transform.scale(
      self._estrella, (self._tam * 0.9, self._tam * 0.9)
    )

    self._koopa = pygame.image.load("./src/resources/koopa.jpg")
    self._koopa = pygame.transform.scale(
      self._koopa, (self._tam * 0.9, self._tam * 0.9)
    )

    self._flor = pygame.image.load("./src/resources/flor.png")
    self._flor = pygame.transform.scale(
      self._flor, (self._tam * 0.9, self._tam * 0.9)
    )


  def _pintarLaberinto(self):
    """
    Grafica el laberinto con sus elementos.
    """

    for i in range(len(self._laberinto.getLaberinto())):
      for j in range(len(self._laberinto.getLaberinto())):
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
    if (tipo == 1):
      "Muro"
      self._pintarElemento(self._muro, x, y)
    elif (tipo == 2):
      "Mario"
      self._pintarElemento(self._mario, x, y)
    elif (tipo == 3):
      "Estrella"
      self._pintarElemento(self._estrella, x, y)
    elif (tipo == 4):
      "Flor"
      self._pintarElemento(self._flor, x, y)
    elif (tipo == 5):
      "Koopa"
      self._pintarElemento(self._koopa, x, y)
    elif (tipo == 6):
      "Peach"
      self._pintarElemento(self._princesa, x, y)
    elif (tipo == 8):
      "Mario encuentra una estrella"
      self._pintarElemento(self._mario, x, y)
    elif (tipo == 9):
      "Mario encuentra una flor"
      self._pintarElemento(self._mario, x, y)
    elif (tipo == 10):
      "Mario encuentra un Koopa"
      self._pintarElemento(self._mario, x, y)
    elif (tipo == 11):
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
    pygame.draw.rect(self._surface, "white", (self._screenWidth * 0.05 + self._tam *
                     x, self._screenHeight * 0.05 + self._tam * y, self._tam, self._tam))
    pygame.draw.rect(self._surface, "dark gray", (self._screenWidth * 0.05 + self._tam * x,
                     self._screenHeight * 0.05 + self._tam * y, self._tam, self._tam), self._lineWidth)

  def _pintarElemento(self, elem, x: int, y: int):
    """
    Dibuja la casilla que contiene la princesa.

    Args:
      x (int): Posición de la casilla en X. 
      y (int): Posición de la casilla en Y.
    """
    self._pintarCasillaVacia(x, y)

    self._surface.blit(elem, (self._screenWidth * 0.05 + self._tam * 0.05 +
                       self._tam * x, self._screenHeight * 0.05 + self._tam * 0.05 + self._tam * y))

  def _pintarFinal(self, x: int, y: int):
    """
    Dibuja la casilla donde el agente y la meta se encuentran.

    Args:
        x (int): Posición de la casilla en X. 
        y (int): Posición de la casilla en Y.
    """
    self._pintarCasillaVacia(x, y)

    self._surface.blit(self._mario, (self._screenWidth * 0.05 + self._tam * 0.05 +
                       self._tam * x, self._screenHeight * 0.05 + self._tam * 0.05 + self._tam * y))
    self._surface.blit(self._princesa, (self._screenWidth * 0.05 + self._tam * 0.05 +
                       self._tam * x, self._screenHeight * 0.05 + self._tam * 0.05 + self._tam * y))

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
