import random

def burbuja(matriz):
    n = len(matriz)

    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[j] > matriz[j+1]:
                matriz[j], matriz[j+1] = matriz[j+1], matriz[j]

def cuadrados_ordenados(matriz):
    SS = 88
    resultado = []

    for num in matriz:
        cuadrado = num ** 2
        if cuadrado <= SS:
            resultado.append(cuadrado)
    
    if resultado:
        burbuja(resultado)
        return resultado
    else:
        return []


n = random.randint(0, 50)
matriz_original = [random.randint(-15, 15) for _ in range(n)]
#matriz_original = [1, 2, 3, 5, 6, 8, 9]
#matriz_original = [-1,-2]
#matriz_original = [-6, -5, 0, 5, 6]
#matriz_original = [-10,10]


burbuja(matriz_original)
print(matriz_original)

if matriz_original: #Se asegura que solo le llegen matrices no vacias a la funcion
    resultado_final = cuadrados_ordenados(matriz_original)
    print(resultado_final)
else:
    print("Matriz vacia")