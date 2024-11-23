
from tkinter import *

class Calculadora(Frame):  # Frame es la clase de tkinter que estamos heredando.
    def __init__(self, master=None):
        super().__init__(master, width=320, height=170)
        self.master = master
        self.pack()
        self.creaboton()

    def suma(self):
        a1 = self.anum1.get()
        a2 = self.anum2.get()
        r = float(a1) + float(a2)
        self.anum3.delete(0, 'end')
        self.anum3.insert(0, r)

    def resta(self):
        a1 = self.anum1.get()
        a2 = self.anum2.get()
        r = float(a1) - float(a2)
        self.anum3.delete(0, 'end')
        self.anum3.insert(0, r)

    def producto(self):
        a1 = self.anum1.get()
        a2 = self.anum2.get()
        r = float(a1) * float(a2)
        self.anum3.delete(0, 'end')
        self.anum3.insert(0, r)

    def cociente(self):
        a1 = self.anum1.get()
        a2 = self.anum2.get()
        r = float(a1) / float(a2)
        self.anum3.delete(0, 'end')
        self.anum3.insert(0, r)

    def creaboton(self):
        self.bnum1 = Label(self, text='DATO 1')
        self.bnum1.config(fg='green', font=('Arial', 20))
        self.anum1 = Entry(self)
        self.bnum2 = Label(self, text='DATO 2')
        self.anum2 = Entry(self)
        self.op = Button(self, text='Suma', command=self.suma)
        self.op1 = Button(self, text='Resta', command=self.resta)
        self.op2 = Button(self, text='Multiplicación', command=self.producto)
        self.op3 = Button(self, text='División', command=self.cociente)
        self.bnum3 = Label(self, text='Resultado')
        self.anum3 = Entry(self)

        # Posicionamiento de los widgets
        self.bnum1.place(x=10, y=10, width=100, height=30)
        self.anum1.place(x=120, y=10, width=100, height=30)
        self.bnum2.place(x=10, y=50, width=100, height=30)
        self.anum2.place(x=120, y=50, width=100, height=30)
        self.op.place(x=230, y=10, width=100, height=20)
        self.op1.place(x=230, y=40, width=100, height=20)
        self.op2.place(x=230, y=70, width=100, height=20)
        self.op3.place(x=230, y=100, width=100, height=20)
        self.bnum3.place(x=10, y=120, width=100, height=30)
        self.anum3.place(x=120, y=120, width=100, height=30)

# Crear la ventana principal
vent = Tk()
vent.wm_title('Calculadora')
vent.geometry('400x200')
app = Calculadora(vent)  # Instanciar la clase
app.mainloop()  # Ejecutar el bucle principal de la aplicación







