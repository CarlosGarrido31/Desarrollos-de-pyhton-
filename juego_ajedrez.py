class Ajedrez:
    def __init__(self):
        self.tablero = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.jugador_actual = 'blanco'

    def mostrar_tablero(self):
        for fila in self.tablero:
            print(' '.join(fila))
        print()

    def es_valida(self, origen, destino):
        # Aquí solo verificamos si las casillas están dentro del tablero
        return (0 <= origen[0] < 8 and 0 <= origen[1] < 8 and
                0 <= destino[0] < 8 and 0 <= destino[1] < 8)

    def mover(self, origen, destino):
        if not self.es_valida(origen, destino):
            print("Movimiento inválido. Fuera de los límites del tablero.")
            return False

        pieza_origen = self.tablero[origen[0]][origen[1]]
        if pieza_origen == '.':
            print("No hay pieza en la posición de origen.")
            return False

        if self.jugador_actual == 'blanco' and pieza_origen.islower():
            print("Es el turno de las piezas blancas, pero seleccionaste una pieza negra.")
            return False
        if self.jugador_actual == 'negro' and pieza_origen.isupper():
            print("Es el turno de las piezas negras, pero seleccionaste una pieza blanca.")
            return False

        # Movemos la pieza
        self.tablero[destino[0]][destino[1]] = pieza_origen
        self.tablero[origen[0]][origen[1]] = '.'

        # Cambiamos el turno
        self.jugador_actual = 'negro' if self.jugador_actual == 'blanco' else 'blanco'

        return True

    def jugar(self):
        while True:
            self.mostrar_tablero()
            print(f"Es el turno de las piezas {self.jugador_actual}.")

            try:
                origen = input("Ingresa la posición de origen (por ejemplo, 'e2'): ")
                destino = input("Ingresa la posición de destino (por ejemplo, 'e4'): ")

                # Convertir de formato de ajedrez a índices
                columna_origen = ord(origen[0].lower()) - ord('a')
                fila_origen = 8 - int(origen[1])
                columna_destino = ord(destino[0].lower()) - ord('a')
                fila_destino = 8 - int(destino[1])

                if self.mover((fila_origen, columna_origen), (fila_destino, columna_destino)):
                    continue
            except (IndexError, ValueError):
                print("Movimiento inválido. Usa el formato correcto (ej. 'e2').")
            except KeyboardInterrupt:
                print("\nJuego terminado.")
                break


# Crear el juego y comenzarlo
juego = Ajedrez()
juego.jugar()