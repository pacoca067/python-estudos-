numero = list (range(10))

for n in range (0,10):
    numero[n] =int(input("digite um numero:"))

for i in range(0,10):
    for j in range(0,i):
        if (numero [i] > numero[j]):
            aux = numero [i]
            numero [i] = numero [j]
            numero[j] = aux

for n in range(0,10): 
    print(numero[n])            