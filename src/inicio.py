import pygame
from pygame.locals import *
import sys
import time
from tkinter.filedialog import askopenfile
from clases.GUI import GUI

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


class AperturaArchivo():

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

    def seleccionar_archivo():
        archivo = askopenfile(mode='r', filetypes=[
                              ('Archivos de texto', '*.txt')])

        if archivo is not None:
            contenido1 = archivo.read()

            return contenido1


def retornar(contenido, algoritmo):
    ventana = GUI(cargarLaberinto(contenido), algoritmo, 600, 600)

    time.sleep(1)

    ventana.iniciar()


def cargarLaberinto(contenido):
    laberinto = contenido

    laberinto = laberinto.strip().split("\n")

    for i in range(len(laberinto)):
        laberinto[i] = laberinto[i].strip().split()

    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            laberinto[i][j] = int(laberinto[i][j])

    return laberinto


def main():
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 639
    contenido = None
    algoritmo = 0

    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mario Smart")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = pygame.image.load("./src/resources/fondo.jpg").convert()

    # Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(fondo, (0, 0))

    seleccionar_mundo = Label(
        screen, "Seleccionar mundo", 520, 330, 36, color="white")
    amplitud = Label(screen, "Amplitud", 350, 400, 25)
    costo = Label(screen, "Costo uniforme", 470, 400, 25)
    profundidad = Label(screen, "Profundidad", 650, 400, 25)
    avara = Label(screen, "Avara", 800, 400, 25)
    A = Label(screen, "A*", 900, 400, 25)
    iniciar = Label(screen, "Iniciar", 575, 450, 45)

    show_labels()
    # se muestran lo cambios en pantalla
    pygame.display.flip()

    # el bucle principal del juego
    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (520 <= pygame.mouse.get_pos()[0] <= 780 and 330 <= pygame.mouse.get_pos()[1] <= 375):
                    contenido = AperturaArchivo.seleccionar_archivo()
                    if (contenido is not None):
                        seleccionar_mundo.change_font(
                            "Arial", 36, color="red")
                        show_labels()
                        pygame.display.flip()
                # Botón de amplitud
                if (350 <= pygame.mouse.get_pos()[0] <= 440 and 400 <= pygame.mouse.get_pos()[1] <= 440):
                    algoritmo = 1
                    amplitud.change_font(
                        "Arial", 25, color="white")
                    costo.change_font(
                        "Arial", 25, color="white")
                    profundidad.change_font(
                        "Arial", 25, color="white")
                    avara.change_font(
                        "Arial", 25, color="white")
                    A.change_font(
                        "Arial", 25, color="white")
                    amplitud.change_font(
                        "Arial", 25, color="red")
                    show_labels()
                    pygame.display.flip()
                # Botón de costo uniforme
                if (470 <= pygame.mouse.get_pos()[0] <= 620 and 400 <= pygame.mouse.get_pos()[1] <= 440):
                    algoritmo = 2
                    amplitud.change_font(
                        "Arial", 25, color="white")
                    costo.change_font(
                        "Arial", 25, color="white")
                    profundidad.change_font(
                        "Arial", 25, color="white")
                    avara.change_font(
                        "Arial", 25, color="white")
                    A.change_font(
                        "Arial", 25, color="white")
                    costo.change_font(
                        "Arial", 25, color="red")
                    show_labels()
                    pygame.display.flip()
                # Botón de profundidad
                if (650 <= pygame.mouse.get_pos()[0] <= 770 and 400 <= pygame.mouse.get_pos()[1] <= 440):
                    algoritmo = 3
                    amplitud.change_font(
                        "Arial", 25, color="white")
                    costo.change_font(
                        "Arial", 25, color="white")
                    profundidad.change_font(
                        "Arial", 25, color="white")
                    avara.change_font(
                        "Arial", 25, color="white")
                    A.change_font(
                        "Arial", 25, color="white")
                    profundidad.change_font(
                        "Arial", 25, color="red")
                    show_labels()
                    pygame.display.flip()
                # Botón de avara
                if (800 <= pygame.mouse.get_pos()[0] <= 860 and 400 <= pygame.mouse.get_pos()[1] <= 440):
                    algoritmo = 4
                    amplitud.change_font(
                        "Arial", 25, color="white")
                    costo.change_font(
                        "Arial", 25, color="white")
                    profundidad.change_font(
                        "Arial", 25, color="white")
                    avara.change_font(
                        "Arial", 25, color="white")
                    A.change_font(
                        "Arial", 25, color="white")
                    avara.change_font(
                        "Arial", 25, color="red")
                    show_labels()
                    pygame.display.flip()
                # Botón de A*
                if (900 <= pygame.mouse.get_pos()[0] <= 940 and 400 <= pygame.mouse.get_pos()[1] <= 440):
                    algoritmo = 5
                    amplitud.change_font(
                        "Arial", 25, color="white")
                    costo.change_font(
                        "Arial", 25, color="white")
                    profundidad.change_font(
                        "Arial", 25, color="white")
                    avara.change_font(
                        "Arial", 25, color="white")
                    A.change_font(
                        "Arial", 25, color="white")
                    A.change_font(
                        "Arial", 25, color="red")
                    show_labels()
                    pygame.display.flip()
                # Botón de inicio
                if (575 <= pygame.mouse.get_pos()[0] <= 690 and 450 <= pygame.mouse.get_pos()[1] <= 500):
                    if (contenido is not None and algoritmo != 0):
                        retornar(contenido, algoritmo)

            elif event.type == pygame.MOUSEMOTION:
                if (520 <= pygame.mouse.get_pos()[0] <= 780 and 330 <= pygame.mouse.get_pos()[1] <= 375):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif (350 <= pygame.mouse.get_pos()[0] <= 440 and 400 <= pygame.mouse.get_pos()[1] <= 440):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif (470 <= pygame.mouse.get_pos()[0] <= 620 and 400 <= pygame.mouse.get_pos()[1] <= 440):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif (650 <= pygame.mouse.get_pos()[0] <= 770 and 400 <= pygame.mouse.get_pos()[1] <= 440):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif (800 <= pygame.mouse.get_pos()[0] <= 860 and 400 <= pygame.mouse.get_pos()[1] <= 440):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif (900 <= pygame.mouse.get_pos()[0] <= 940 and 400 <= pygame.mouse.get_pos()[1] <= 440):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif (575 <= pygame.mouse.get_pos()[0] <= 690 and 450 <= pygame.mouse.get_pos()[1] <= 500):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


if __name__ == "__main__":
    main()
