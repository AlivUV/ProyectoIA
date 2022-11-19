# pruebas.py

from clases.MarioAmplitud import MarioAmplitud
from clases.MarioCostos import MarioCostos
from clases.MarioProfundidad import MarioProfundidad
from clases.MarioAvara import MarioAvara
from clases.MarioA import MarioA

from datetime import datetime
from json import loads

def cargarLaberinto():
  laberinto = open("./src/data/laberinto/Prueba2.txt").read()

  laberinto = laberinto.split("\n")

  for i in range (len(laberinto)):
    laberinto[i] = laberinto[i].split()

  for i in range (len(laberinto)):
    for j in  range (len(laberinto[0])):
      laberinto[i][j] = int(laberinto[i][j])

  return laberinto

laberinto = cargarLaberinto()
elementos = loads(open("./src/data/estados/elementos.json").read())

print("===Amplitud===")

inicio = datetime.now()

mario = MarioAmplitud(laberinto, elementos)

duracion = datetime.now() - inicio

print("Duración: {}".format(duracion))


print("===Costos===")

inicio = datetime.now()

mario = MarioCostos(laberinto, elementos)

duracion = datetime.now() - inicio

print("Duración: {}".format(duracion))


print("===Profundidad===")

inicio = datetime.now()

mario = MarioProfundidad(laberinto, elementos)

duracion = datetime.now() - inicio

print("Duración: {}".format(duracion))


print("===Avara===")

inicio = datetime.now()

mario = MarioAvara(laberinto, elementos)

duracion = datetime.now() - inicio

print("Duración: {}".format(duracion))

print("===A*===")

inicio = datetime.now()

mario = MarioA(laberinto, elementos)

duracion = datetime.now() - inicio

print("Duración: {}".format(duracion))