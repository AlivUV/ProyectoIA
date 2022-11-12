# pruebas.py

from clases.MarioAmplitud import MarioAmplitud
from clases.MarioCostos import MarioCostos
from clases.MarioAvara import MarioAvara
from clases.MarioA import MarioA
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

print("===Amplitud===")

inicio = datetime.now()

mario = MarioAmplitud(cargarLaberinto())

duracion = datetime.now() - inicio

print("Duración: {}".format(duracion))

print("===Costos===")

inicio = datetime.now()

mario = MarioCostos(cargarLaberinto())

duracion = datetime.now() - inicio

print("Duración: {}".format(duracion))

print("===Avara===")

inicio = datetime.now()

mario = MarioAvara(cargarLaberinto())

duracion = datetime.now() - inicio

print("Duración: {}".format(duracion))

print("===A*===")

inicio = datetime.now()

mario = MarioA(cargarLaberinto())

duracion = datetime.now() - inicio

print("Duración: {}".format(duracion))