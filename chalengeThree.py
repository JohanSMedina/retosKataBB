import random
listCoins=[50,100,200,500,1000]

def cambioMinimo(coins):
    coins.sort()
    print("Monedas: ",coins)
    minChange = 1

    for coin in coins:
        if coin <= minChange:
            minChange += coin

    return minChange

n = random.randint(0, 20)
coins = [random.randint(1,20) for _ in range(n)]
#coins = [5, 7, 1, 1, 2, 3, 22]
#coins = [1,1,1,1,1]
#coins = [1, 5, 1, 1, 1, 10, 15, 20, 100]

cambio = cambioMinimo(coins)
print("Cambio minimo: ",cambio)