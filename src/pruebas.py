# pruebas.py
from json import loads
from clases.MarioAmplitud import MarioAmplitud

def cargarLaberinto():
  laberinto = open("./src/data/laberinto/laberintoProyecto.txt").read()

  laberinto = laberinto.split("\n")

  for i in range (len(laberinto)):
    laberinto[i] = laberinto[i].split()

  for i in range (len(laberinto)):
    for j in  range (len(laberinto[0])):
      laberinto[i][j] = int(laberinto[i][j])

  return laberinto

mario = MarioAmplitud(cargarLaberinto())
