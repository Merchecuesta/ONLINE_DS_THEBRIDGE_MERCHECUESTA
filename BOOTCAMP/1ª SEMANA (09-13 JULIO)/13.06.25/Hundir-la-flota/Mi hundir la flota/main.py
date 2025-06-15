from utils import *

def jugar():
    mostrar_reglas()
    
    tablero_jugador = crea_tablero()
    tablero_maquina = crea_tablero()
    tablero_jugador = colocar_barcos(tablero_jugador)
    tablero_maquina = colocar_barcos(tablero_maquina)
    disparos_maquina = set()

    print("\n🚢 ¡Empieza el juego! ¡Buena suerte!")
    turno = 0

    while True:
        print("\n📌 Tu tablero:")
        mostrar_tablero(tablero_jugador)
        print("\n🎯 Tablero enemigo:")
        mostrar_tablero(tablero_maquina, oculto=True)

        print(f"\n📊 Barcos restantes - Tú: {contar_barcos_restantes(tablero_jugador)} | Enemigo: {contar_barcos_restantes(tablero_maquina)}")
        print(f"🎯 Disparos máquina realizados: {len(disparos_maquina)}")

        if turno == 0:
            print("\n🧍 Tu turno.")
            coord = obtener_coordenada_usuario()
            recibir_disparo(tablero_maquina, coord)
            if todos_hundidos(tablero_maquina):
                print("\n🎉 ¡Felicidades! ¡Has hundido toda la flota enemiga y ganado el juego!")
                break
        else:
            print("\n🤖 Turno de la máquina...")
            coord = disparo_maquina(tablero_jugador, disparos_maquina)
            disparos_maquina.add(coord)
            print(f"La máquina dispara en {coord}...")
            recibir_disparo(tablero_jugador, coord)
            if todos_hundidos(tablero_jugador):
                print("\n💀 La máquina ha hundido toda tu flota. ¡Has perdido!")
                break

        turno = 1 - turno

if __name__ == "__main__":
    jugar()
