import tkinter as tk

class FourSquares(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x400")  # Tamaño de la ventana
        self.grid(sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        # Crear los cuadros
        self.create_square1()
        self.create_square2()
        self.create_square3()
        self.create_square4()

        # Configurar el peso de las filas y columnas
        # La fila 0 será más grande que la fila 1
        self.grid_rowconfigure(0, weight=2)  # Fila 0 más grande
        self.grid_rowconfigure(1, weight=1)  # Fila 1 más pequeña
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Configurar el tamaño mínimo de las filas y columnas
        self.grid_rowconfigure(0, minsize=250)  # Ajusta este valor según sea necesario
        self.grid_rowconfigure(1, minsize=150)  # Ajusta este valor según sea necesario
        self.grid_columnconfigure(0, minsize=200)  # Ajusta este valor según sea necesario
        self.grid_columnconfigure(1, minsize=200)  # Ajusta este valor según sea necesario

    def create_square1(self):
        self.square1 = tk.Frame(self, bg='red')
        self.square1.grid(row=0, column=0, sticky="nsew")

    def create_square2(self):
        self.square2 = tk.Frame(self, bg='green')
        self.square2.grid(row=0, column=1, sticky="nsew")

    def create_square3(self):
        self.square3 = tk.Frame(self, bg='blue')
        self.square3.grid(row=1, column=0, sticky="nsew")

    def create_square4(self):
        self.square4 = tk.Frame(self, bg='yellow')
        self.square4.grid(row=1, column=1, sticky="nsew")

root = tk.Tk()
app = FourSquares(master=root)
app.mainloop()
