from tkinter import *
import random

class GeneradorNumeros:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.resizable(0,0)
        self.ventana.title("Generador de Números")
        
        self.label1 = Label(ventana, text="Número 1:")
        self.label1.grid(row=0, column=0, padx=10, pady=5)
        
        self.num1_spinbox = Spinbox(ventana, from_=0, to=100)
        self.num1_spinbox.grid(row=0, column=1, padx=10, pady=5)
        
        self.label2 = Label(ventana, text="Número 2:")
        self.label2.grid(row=1, column=0, padx=10, pady=5)
        
        self.num2_spinbox = Spinbox(ventana, from_=0, to=100)
        self.num2_spinbox.grid(row=1, column=1, padx=10, pady=5)
        
        self.label3 = Label(ventana, text="Número Generado:")
        self.label3.grid(row=2, column=0, padx=10, pady=5)
        
        self.generated_num_entry = Entry(ventana, state="readonly")
        self.generated_num_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.generate_button = Button(ventana, text="Generar", command=self.generate_number)
        self.generate_button.grid(row=3, column=1, padx=10, pady=5)
    
    def generate_number(self):
        generated_num=0
        num1 = int(self.num1_spinbox.get())
        num2 = int(self.num2_spinbox.get())
        generated_num = random.randint(min(num1, num2), max(num1, num2))
        self.generated_num_entry.config(state="normal")
        self.generated_num_entry.delete(0, END)
        self.generated_num_entry.insert(0, str(generated_num))
        self.generated_num_entry.config(state="readonly")


ventana = Tk()
GeneradorNumeros(ventana)
ventana.mainloop()
