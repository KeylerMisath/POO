class Biblioteca:
    def __init__(self, titulo, autor, estado):
        self.titulo = titulo
        self.autor = autor
        self.estado = estado

    def Registro(self):
        self.titulo = str(input("¿Qué libro desea registrar? "))
        self.autor = str(input("¿Qué autor tien el libro? "))
        self.estado = str(input("¿En qué estado se encuentra su libro?: "))
        return print(f"Has registrado: {self.titulo} de {self.autor}.")
    
    def status(self, disponible, prestado):
        self.disponible = "disponible"
        self.prestado = "prestado"
        if self.tiulo == "prestado":
            print(f"El libro {self.titulo} se encuentra prestado")

        elif self.titulo == "Disponible":
            print(f"El libro {self.titulo} se encuentra disponible")    

Libro1 = Biblioteca(False, False, False)
Libro1.Registro() 