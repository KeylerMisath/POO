def sucesion_fibonacci():
    numero_inicial = 0
    numero_siguiente = 1
    for i in range(numero_inicial, 20, 1):
        numero_resultante = numero_inicial + numero_siguiente
        numero_inicial = numero_siguiente
        numero_siguiente = numero_resultante
        print(numero_resultante)

def calcular_seno():
    numero_x = float(input("Ingrese el valor en radianes:"))
    
    sen = 0 
    terminos = 20
    
    for i in range (terminos):
        signo = (-1)**i
        numerador = numero_x ** (2*i+1)
        denominador = 1
        for j in range (1, 2*i+2):
            denominador = denominador * j
        signo_termino = signo * (numerador / denominador)
        sen = sen + signo_termino
    print(f"El valor del seno es: {sen}")

def calcular_coseno():
    numero_x = float(input("Ingrese el valor en radianes:"))
    cos = 0 
    terminos = 20
    
    for i in range (terminos):
        signo = (-1)**i
        numerador = numero_x ** (2*i)
        denominador = 1
        for j in range (1, 2*i+1):
            denominador = denominador * j
        signo_termino = signo * (numerador / denominador)
        cos = cos + signo_termino
    print(f"El valor del coseno es: {cos}")



def menu():

    print("Opción 1: Serie de Fibonacci")
    print("Opción 2: Calcular seno")
    print("Opción 3: Calcular coseno")

    opcion = int(input("Seleccione una opción: "))
    
    while True:
     match opcion:
        case 1: 
         sucesion_fibonacci()
        case 2: 
         calcular_seno()
        case 3: 
         calcular_coseno()
     break 

menu()
