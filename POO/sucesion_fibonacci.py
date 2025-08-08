numero_inicial = 0
numero_siguiente = 1

for i in range(numero_inicial, 20, 1):
    numero_resultante = numero_inicial + numero_siguiente
    numero_inicial = numero_siguiente
    numero_siguiente = numero_resultante
    print(numero_resultante)