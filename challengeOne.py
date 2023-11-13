import random

# Función de Counting Sort
def counting_sort(lista):

    if not lista:
        return

    valorMax = max(lista)
    valorMin = min(lista)
    rango = valorMax - valorMin + 1

    count = [0] * rango
    output = [0] * len(lista)

    for i in range(len(lista)):
        count[lista[i] - valorMin] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = len(lista) - 1
    while i >= 0:
        output[count[lista[i] - valorMin] - 1] = lista[i]
        count[lista[i] - valorMin] -= 1
        i -= 1

    for i in range(len(lista)):
        lista[i] = output[i]

    print("Lista ordenada:", lista)


# Generación y procesamiento de la lista
S = 8
n = random.randint(1, 100)
listInt = [random.randint(0, 100) for _ in range(n)]
#listInt = [1, 2, 3, 4, 5, 8]
#listInt = [10, 20, 30, 40]
#listInt = [8]
#listInt = [88] 
#listInt = [85] 
#listInt = [8, 2, 1] 
#listInt = [80, 8, 5, 4, 3, 2, 7, 7, 29, 1]

print("Tamaño lista:", len(listInt))
print("Lista original:", listInt)

listStr = [str(num) for num in listInt]
listStr = [num.replace(str(S), "") for num in listStr]
listInt = [int(num) for num in listStr if (num and int(num) < S)]

# Algoritmo de ordenamiento O(n) - Counting Sort
counting_sort(listInt)