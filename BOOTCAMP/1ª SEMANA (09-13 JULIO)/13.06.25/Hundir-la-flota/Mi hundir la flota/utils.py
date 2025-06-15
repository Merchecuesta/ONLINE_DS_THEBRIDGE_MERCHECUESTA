import numpy as np
import random

def mostrar_reglas():
    print("""
🚢 Bienvenido a Batalla Naval

Reglas rápidas:
- Introduce filas y columnas del 0 al 9 para disparar.
- Barcos marcados con 'O' en tu tablero.
- 'X' = tocado, '-' = agua.
- ¡El primero que hunda toda la flota gana!

¡Buena suerte!
""")

def crea_tablero(lado=10):
    return np.full((lado, lado), " ")

def coloca_barco_plus(tablero, barco):
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    for pieza in barco:
        fila, columna = pieza
        if fila < 0 or fila >= num_max_filas or columna < 0 or columna >= num_max_columnas:
            return False
        if tablero[pieza] in ["O", "X"]:
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp

def colocar_barcos(tablero):
    esloras = [2, 2, 2, 3, 3, 4]
    for eslora in esloras:
        colocado = False
        intentos = 0
        print(f"🔧 Intentando colocar barco de eslora {eslora}...")
        while not colocado and intentos < 200:
            intentos += 1
            barco = []
            fila = random.randint(0, 9)
            col = random.randint(0, 9)
            orientacion = random.choice(["N", "S", "E", "O"])
            barco.append((fila, col))
            for _ in range(eslora - 1):
                if orientacion == "N": fila -= 1
                elif orientacion == "S": fila += 1
                elif orientacion == "E": col += 1
                elif orientacion == "O": col -= 1
                barco.append((fila, col))
            tablero_temp = coloca_barco_plus(tablero, barco)
            if isinstance(tablero_temp, np.ndarray):
                tablero = tablero_temp
                colocado = True
                print(f"✅ Barco de eslora {eslora} colocado ")
        if not colocado:
            print(f"⚠️ No se pudo colocar el barco de eslora {eslora} después de muchos intentos.")
    return tablero

def mostrar_tablero(tablero, oculto=False):
    print("  " + " ".join(str(i) for i in range(tablero.shape[1])))
    for i, fila in enumerate(tablero):
        fila_mostrar = []
        for c in fila:
            if oculto and c == "O":
                fila_mostrar.append(" ")
            else:
                fila_mostrar.append(c)
        print(str(i) + " " + " ".join(fila_mostrar))

def contar_barcos_restantes(tablero):
    return np.sum(tablero == "O")

def obtener_coordenada_usuario():
    while True:
        try:
            fila = int(input("Introduce la fila (0-9): "))
            col = int(input("Introduce la columna (0-9): "))
            if 0 <= fila < 10 and 0 <= col < 10:
                return (fila, col)
            else:
                print("Coordenadas fuera de rango.")
        except:
            print("Entrada inválida, usa números enteros.")

def disparo_maquina(tablero, disparos_previos):
    while True:
        fila = random.randint(0, 9)
        col = random.randint(0, 9)
        if (fila, col) not in disparos_previos:
            return (fila, col)

def recibir_disparo(tablero, coordenada):
    if tablero[coordenada] == "O":
        tablero[coordenada] = "X"
        print(f"💥 ¡Tocado en {coordenada}!")
    elif tablero[coordenada] == "X" or tablero[coordenada] == "-":
        print(f"⛔ Ya disparaste a {coordenada}, prueba otro lugar.")
    else:
        tablero[coordenada] = "-"
        print(f"🌊 Agua en {coordenada}.")

def todos_hundidos(tablero):
    return not np.any(tablero == "O")
