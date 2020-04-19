import pygame
import numpy as np
import time

pygame.init()

# Tamaño de la ventana del juego.
size = width, height = 500, 500

# Cantidad de celdas por filas/columnas.
nxC = 50    # Cantidad de celdas por filas (Eje X).
nyC = 50   # Cantidad de celdas por columnas (Eje Y).

# Proporcion de tamaño en relación con la cantida de celdas por filas/columnas.
dimCW = (width - 1) / nxC   # Distancia vertical de la pantalla sobre cantidad de celdas por filas.
dimCH = (height - 1) / nyC  # Distancia horizontal de la pantalla sobre cantidad de celdas por columnas.

# Color de fondo de la ventana del juego.
bg = 25, 25, 25

screen = pygame.display.set_mode(size)

# Crea una matriz llena de zeros con la cantidad de filas y columnas previamente definidas.
gameState = np.zeros((nxC, nyC))

# Pone vivas algunas celdas (Coloca el valor en encendido / 1) para mostrar "A Middleweight spaceship".
gameState[21, 21] = 1
gameState[22, 21] = 1
gameState[18, 22] = 1
gameState[19, 22] = 1
gameState[20, 22] = 1
gameState[22, 22] = 1
gameState[23, 22] = 1
gameState[18, 23] = 1
gameState[19, 23] = 1
gameState[20, 23] = 1
gameState[21, 23] = 1
gameState[22, 23] = 1
gameState[19, 24] = 1
gameState[20, 24] = 1
gameState[21, 24] = 1

# Inicia el prompt del juego dentro de un bucle infinito. Para salir de la ventana hay que matar el proceso.
while True:

    # Crea una matriz copia de la matriz previa para hacer los cambios en esta.
    new_gameState = np.copy(gameState)

    # Borra la pantalla colocando el color de fondo previamente definido.
    screen.fill(bg)

    # Ciclo que se encarga de recorrer la matriz para calcular el número de celdas vecinas vivas y así poder
    # establecer las reglas del juego. Además de que el ciclo se encarga de que el tablero sea Toroidal.
    for y in range(0, nyC):
        for x in range(0, nxC):

            # Se crea una variable con el número de vecinos vivos de una celda, sin contar la celda en la que 
            # se encuentra parado el ciclo (x, y).
            n_neigh = gameState[(x-1) % nxC, (y-1) % nyC] + \
                      gameState[(x) % nxC, (y-1) % nyC] + \
                      gameState[(x+1) % nxC, (y-1) % nyC] + \
                      gameState[(x-1) % nxC, (y) % nyC] + \
                      gameState[(x+1) % nxC, (y) % nyC] + \
                      gameState[(x-1) % nxC, (y+1) % nyC] + \
                      gameState[(x) % nxC, (y+1) % nyC] + \
                      gameState[(x+1) % nxC, (y+1) % nyC]

            ### Reglas/lógica del juego ###

            # Una celula muerta con exactamente 3 celulas vecinas vivas "nace".
            if gameState[x,y] == 0 and n_neigh == 3:
                new_gameState[x,y] = 1
            # Una celula viva con 2 o 3 celulas vecinas vivas sigue viva, en caso contrario muere.
            elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                new_gameState[x,y] = 0

            # Se define un poligono regular, cuadrado, de la siguiente manera:
            poly = [((x) * dimCW, (y) * dimCH),
                    ((x+1) * dimCW, (y) * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, (y+1) * dimCH)]

            # Por cada interacción previa con el ciclo (Notese que todavía se encuentra en el ciclo)
            # se dibuja el cuadrado que contendrá el valor de la celula.
            # Un cuadrado hueco para una celula muerta (0).
            # Un cuadrado solido para una celula viva (1).
            pygame.draw.polygon(screen, (128,128,128), poly, int(abs(1 - new_gameState[x,y])))

    # Al salir del bucle se guarda todos los datos de la interación en su matriz original.
    gameState = new_gameState
    
    # Delay
    time.sleep(0.05)

    # Muestra en pantalla los objetos dibujados (previamente el .draw.).
    pygame.display.flip()