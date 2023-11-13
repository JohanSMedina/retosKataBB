import random

# Función de Counting Sort
def counting_sort(arr):

    if not arr:
        return  # Do nothing if the list is empty

    valorMax = max(arr)
    valorMin = min(arr)
    rango = valorMax - valorMin + 1

    count = [0] * rango
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - valorMin] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i] - valorMin] - 1] = arr[i]
        count[arr[i] - valorMin] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

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
print("Lista ordenada:", listInt)
