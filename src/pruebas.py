# pruebas.py

from clases.MarioCostos import MarioCostos
from datetime import datetime

def cargarLaberinto():
  laberinto = open("./src/data/laberinto/laberintoProyecto.txt").read()

  laberinto = laberinto.split("\n")

  for i in range (len(laberinto)):
    laberinto[i] = laberinto[i].split()

  for i in range (len(laberinto)):
    for j in  range (len(laberinto[0])):
      laberinto[i][j] = int(laberinto[i][j])

  return laberinto

inicio = datetime.now()

mario = MarioCostos(cargarLaberinto())

duracion = datetime.now() - inicio

print("Duración: {}".format(duracion))