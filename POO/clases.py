class Carro:
    def __init__(self, color, marca, modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo 

    def Acelerar(self):
        return print(f"El carro {self.marca} {self.modelo} {self.color} aceleró")
    
    def Frenar(self):
        return print(f"El carro {self.marca} {self.modelo} {self.color} frenó después de 2 minutos")
    
    def Iluminacion(self):
        return print(f"El carro {self.marca} {self.modelo} {self.color} después de frenar encendió sus luces")
    
    def Girar(self):
        return print(f"El carro {self.marca} {self.modelo} {self.color} giró a la derecha con las luces encendidas \n")


carro_obj = Carro("Rojo", "Mazda", "CX30")
carro_obj1 = Carro("Negro", "Fiat", "Pulse")
carro_obj2 = Carro("Gris", "Lamborgini", "Urus")
carro_obj3 = Carro("Azul", "Ford", "Fiesta")
carro_obj.Acelerar() 
carro_obj.Frenar()
carro_obj.Iluminacion()
carro_obj.Girar()
carro_obj1.Acelerar() 
carro_obj1.Frenar()
carro_obj1.Iluminacion()
carro_obj1.Girar()
carro_obj2.Acelerar() 
carro_obj2.Frenar()
carro_obj2.Iluminacion()
carro_obj2.Girar()
carro_obj3.Acelerar() 
carro_obj3.Frenar()
carro_obj3.Iluminacion()
carro_obj3.Girar()


#una biblioteca necesita un programa sencillo para gestonar libros, cada libro tiene: titulo, autor y estado: si está disponible o prestado el sistema debe permitir registrar el libro con su titulo y autor, prestar un libro cambiando su estao a prestado y devolver un libro cambiando s estado a disponible y consultar el estado del libro