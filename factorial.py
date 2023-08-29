from tkinter import *
import math

class Factorial:
    def __init__(self, vetana):
        self.ventana= ventana
        self.ventana.title("Factorial")
        self.ventana.resizable(0,0)
        self.ventana.geometry("450x40")
        self.num_value=0
        

        self.num_label = Label(ventana, text="n:  ")
        self.num_label.grid(row=0, column=1)
        
        self.num_display = Entry(ventana, state="readonly")
        self.num_display.grid(row=0, column=2)
        
        self.factorial = Label(ventana, text="Factorial (n):  ")
        self.factorial.grid(row=0, column=3)
        
        self.factorial = Entry(ventana, state="readonly")
        self.factorial.grid(row=0, column=4)
        
        self.next_button = Button(ventana, text="  Siguiente  ", command=self.calcular_factorial)
        self.next_button.grid(row=0, column=5)
        
    def calcular_factorial(self):
        self.num_value += 1
        self.num_display.config(state="normal")
        self.num_display.delete(0, END)
        self.num_display.insert(0, str(self.num_value))
        self.num_display.config(state="readonly")
        
        factorial_value = math.factorial(self.num_value)
        self.factorial.config(state="normal")
        self.factorial.delete(0, END)
        self.factorial.insert(0, str(factorial_value))
        self.factorial.config(state="readonly")
        
    
    
        
        

ventana = Tk()
Factorial(ventana)
ventana.mainloop()
