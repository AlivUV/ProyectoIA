import pygame
from pygame.locals import *
import sys
import time


pygame.init()


def fontsize(size):
    font = pygame.font.SysFont("Arial", size)
    return font


font_default = fontsize(20)

labels = []


class Label:

    ''' CLASS FOR TEXT LABELS ON THE WIN SCREEN SURFACE '''

    def __init__(self, screen, text, x, y, size=20, color="white"):
        if size != 20:
            self.font = fontsize(size)
        else:
            self.font = font_default
        self.image = self.font.render(text, 1, color)
        _, _, w, h = self.image.get_rect()
        self.rect = pygame.Rect(x, y, w, h)
        self.screen = screen
        self.text = text
        labels.append(self)

    def change_text(self, newtext, color="white"):
        self.image = self.font.render(newtext, 1, color)

    def change_font(self, font, size, color="white"):
        self.font = pygame.font.SysFont(font, size)
        self.change_text(self.text, color)

    def draw(self):
        self.screen.blit(self.image, (self.rect))


def show_labels():
    for _ in labels:
        _.draw()


def pintar_reporte(screen, nodos, profundidad, tiempo, costo):
    Label(
        screen, str(nodos), 400, 420, 25, color="white")
    Label(
        screen, str(profundidad), 400, 480, 25, color="white")
    Label(
        screen, str(costo), 400, 540, 25, color="white")
    Label(
        screen, str(tiempo), 400, 600, 25, color="white")

    show_labels()


def main():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 700

    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Reporte")

    # cargamos una imagen (se crea objetos "Surface")
    mario_amigos = pygame.image.load(
        "./src/resources/mario_amigos.png").convert_alpha()
    mario_amigos = pygame.transform.scale(
        mario_amigos, (SCREEN_WIDTH * 0.8 / 2, SCREEN_HEIGHT * 0.8 / 2))

    # Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(mario_amigos, (50, 100))

    reporte = Label(
        screen, "Reporte", 460, 180, 80, color="white")

    nodos = Label(
        screen, "Cantidad de nodos creados: ", 50, 420, 25, color="white")

    arbol = Label(
        screen, "Profundidad del árbol: ", 50, 480, 25, color="white")

    Costo = Label(
        screen, "Costo de la solución: ", 50, 540, 25, color="white")

    tiempo = Label(
        screen, "Tiempo de cómputo: ", 50, 600, 25, color="white")

    show_labels()
    # se muestran lo cambios en pantalla
    pygame.display.flip()

    # el bucle principal del juego
    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
