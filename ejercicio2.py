import numpy as np

filas = np.random.randint(1, 9)

matriz = np.array([[2,3],[4,5]])

matriz_inversa = np.linalg.inv(matriz)

print(matriz_inversa)

matriz_multiplicada = np.dot(matriz, matriz_inversa)

print(matriz_multiplicada)
