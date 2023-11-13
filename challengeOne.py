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
print("Tamaño lista:", len(listInt))
print("Lista original:", listInt)

listStr = [str(num) for num in listInt]
listStr = [num.replace(str(S), "") for num in listStr]
listInt = [int(num) for num in listStr if (num and int(num) < S)]
#print("Lista procesada:", listInt)

# Algoritmo de ordenamiento O(n) - Counting Sort
counting_sort(listInt)