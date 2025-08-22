class Biblioteca:
    def __init__(self, titulo, autor, estado):
        self.titulo = titulo
        self.autor = autor
        self.estado = estado

    def registrar(self):
        self.titulo = input("¿Qué libro desea registrar?: ")
        self.autor = input("¿Quién es el autor del libro?: ")
        print(f"Has registrado: {self.titulo} de {self.autor}.")

    def prestar(self):
        self.estado = input("¿En qué estado se encuentra su libro? (disponible/prestado): ")

        if self.estado == "disponible":
            self.estado = "prestado"
            print(f"El libro '{self.titulo}' se encuentra disponible.")

        elif self.estado == "prestado":
            print(f"El libro '{self.titulo}' ya está prestado.")


    def devolver(self):
        if self.estado == "prestado":
            status = input("Va a devolver un libro? (si/no): ")
            if status.lower() == "si":
                libro_devuelto = input("¿Qué libro va a devolver?: ")
                if libro_devuelto == self.titulo:
                    self.estado = "disponible"
                    print(f"El libro '{libro_devuelto}' ha sido devuelto y está disponible.")
                else:
                    print(f"El libro '{libro_devuelto}' no coincide con el que está prestado.")  # aquí es en caso de q no se cumpla esa condición 
            elif status.lower() == "no":
                    print("No se realizó ninguna devolución.") 
        else:
            pass


libro = Biblioteca("", "", "disponible")
libro.registrar()
libro.prestar()
libro.devolver()
