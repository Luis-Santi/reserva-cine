asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print("--- RESERVA DE ASIENTOS DE CINE ---")
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

if 0 <= fila <= 2 and 0 <= columna <= 3:
    asientos[fila][columna] = 1
    print("¡Reserva realizada con éxito!")
else:
    print("Posición fuera de rango.")

print("Estado de la sala:")

for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
    
