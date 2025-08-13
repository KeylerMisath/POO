
productos_1 = {
    1:("Aceite", 5000),
    2:("Arroz", 3000),
    3:("Azucar", 2000),
    4:("Sal", 1000),
    5:("Harina", 4000),
    6:("Carne", 15000)}
print (type(productos_1))
productos_agregados = []


def productos():

    saldo = int(input("Ingrese su saldo disponible: "))

    while True:

        print ("1. Mostrar lista de productos")
        print ("2. Agregar nuevos productos")
        print ("3. Terminar compra")
         
        

        opcion = input("Selecione los productos que desea comprar: ")

        match opcion:
            case "1":
                print(productos_1)

                #if ora == "no":
                #    break
                break
            case "2":
                costo = 3000
                pago = saldo - costo
                ora = input(f"Has seleccionado Arroz. Su costo es {costo}. Su saldo restante es {pago}, ¿desea algo más?: ")
                if ora == "no":
                    break
            case "6":
                costo = 15000
                pago = saldo - costo
                ora = input(f"Has seleccionado Carne. Su costo es {costo}. Su saldo restante es {pago}, ¿desea algo más?: ")
                if ora == "si":
                    continue 
                if ora == "no":
                    break
                else:
                 print("Opción no válida, por favor intente de nuevo.")
            case "7":
                nombre = input("Nombre del producto que desea agregar: ")
                costo = int(input("Valor del producto que desea comprar: "))
                pago = saldo - costo 
                ora = input(f"Has seleccionado {nombre}. Su costo es {costo}. Su saldo restante es {pago}, ¿desea algo más?: ")
                if ora == "si":
                    continue 
                if ora == "no":
                    break
                else:
                 print("Opción no válida, por favor intente de nuevo.")
                
            case "0":
                break
            case _:
                print("Opción no válida, por favor intente de nuevo.")
            
    saldo -= costo
    ora = input(f"Su saldo final es {saldo}. ¿Desea realizar otra compra? (si/no): ")
    if ora.lower() == "no":
        print("Gracias por su compra.")


        
productos()
            

