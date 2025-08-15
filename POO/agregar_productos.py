
productos_1 = {
    1:("Aceite", 5000),
    2:("Arroz", 3000),
    3:("Azucar", 2000),
    4:("Sal", 1000),
    5:("Harina", 4000),
    6:("Carne", 15000)}

productos_agregados = []


def productos():

    saldo = int(input("Ingrese su saldo disponible: "))

    while True:

        print ("1. Mostrar lista de productos")
        print ("2. Agregar nuevos productos")
        print ("3. Ver productos agregados")
        print ("4. Terminar compra")
         
        

        opcion = input("Selecione los productos que desea comprar: ")

        match opcion:
            case "1":

                #inicio = max(productos_1.keys())+1
                for clave, (nombre, valor) in productos_1.items():
                    print(f"{clave}. {nombre} - Costo: {valor}")
                for clave, (nombre, valor) in enumerate(productos_agregados, 1):
                    print(f"{clave}. {nombre} - Costo: {valor}")
                int(input("Seleccione los productos que desea comprar: "))
                saldo-=valor 

            case "2":

                nombre = input("¿Qué producto desea agregar?:")
                valor = int(input("¿Cuál es el costo del producto que desea agregar?: "))
                productos_agregados.append((nombre, valor))
                for i, (nombre, valor) in enumerate(productos_agregados, 1):
                    print(f"{i}. {nombre} - Costo: {valor}")
            case "3":
                for j, (nombre, valor) in enumerate(productos_agregados, 1):
                    print(f"{j}. {nombre} - Costo: {valor}")
            
            case "4":

                break
            case _:
                print("Opción no válida, por favor intente de nuevo.")
            
    input(f"Su saldo final es {saldo}. Gracias por su compra")

if __name__ == "__main__":
    productos()
            

