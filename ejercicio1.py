#creacion de matriz
matriz=[[2,4,6,8,10],
        [12,14,16,18,20],
        [22,24,26,28,30],
        [32,24,26,28,40],
        [42,44,46,48,50]]

suma_mas_alta= 0

for columas in range(5):
    sumas_columnas = 0
    for filas in range(5):
        sumas_columnas += matriz[filas][columas]
        if sumas_columnas > suma_mas_alta:
            suma_mas_alta = sumas_columnas

print("la suma mas alta es:",suma_mas_alta)