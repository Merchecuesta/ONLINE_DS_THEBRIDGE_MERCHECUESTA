import pygame

# Inicializamos pygame
pygame.init()

# Definimos colores
VERDE_AGUA = (64, 224, 208)
NEGRO = (0, 0, 0)

# Tamaño pantalla
ANCHO = 400
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tablero con líneas negras y fondo verde agua")

# Variables tablero
TAM_CASILLA = 40
FILAS = 10
COLUMNAS = 10

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Pintamos fondo verde agua
    pantalla.fill(VERDE_AGUA)

    # Dibujamos las líneas negras
    for i in range(FILAS + 1):
        pygame.draw.line(pantalla, NEGRO, (0, i * TAM_CASILLA), (ANCHO, i * TAM_CASILLA), 2)  # Líneas horizontales
    for j in range(COLUMNAS + 1):
        pygame.draw.line(pantalla, NEGRO, (j * TAM_CASILLA, 0), (j * TAM_CASILLA, ALTO), 2)  # Líneas verticales
# Ejemplo: posiciones de barcos (lista de listas de casillas)

# Cada casilla es (fila, columna)
barcos = [
    [(1,1), (1,2), (1,3)],      # Barco de 3 casillas horizontal
    [(4,5), (5,5), (6,5), (7,5)] # Barco de 4 casillas vertical
]

# Color barco
COLOR_BARCO = (255, 69, 0)  # Naranja rojizo

# Dibujar barcos
for barco in barcos:
    for (fila, col) in barco:
        x = col * TAM_CASILLA
        y = fila * TAM_CASILLA
        pygame.draw.rect(pantalla, COLOR_BARCO, (x + 2, y + 2, TAM_CASILLA - 4, TAM_CASILLA - 4))


    pygame.display.flip()

pygame.quit()