from tkinter import *

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.resizable(0,0)
        self.ventana.title("Calculadora")
        
        self.num1 = StringVar()
        self.num2 = StringVar()
        self.result = StringVar()
        
        self.num1_label = Label(ventana, text="Primer número:")
        self.num1_label.grid(row=0, column=0, padx=10, pady=5)
        
        self.num1_entry = Entry(ventana, textvariable=self.num1)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.num2_label = Label(ventana, text="Segundo número:")
        self.num2_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.num2_entry = Entry(ventana, textvariable=self.num2)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.result_label = Label(ventana, text="Resultado:")
        self.result_label.grid(row=2, column=0, padx=10, pady=5)
        
        self.result_entry = Entry(ventana, textvariable=self.result, state="readonly")
        self.result_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.add_button = Button(ventana, text=" + ", width=20, height=1, command=self.add)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)
        
        self.subtract_button = Button(ventana, text=" - ", width=20, height=1, command=self.subtract)
        self.subtract_button.grid(row=4, column=1, padx=10, pady=10)
        
        self.multiply_button = Button(ventana, text=" * ", width=20, height=1, command=self.multiply)
        self.multiply_button.grid(row=5, column=0, padx=10, pady=10)
        
        self.divide_button = Button(ventana, text=" / ", width=20, height=1, command=self.divide)
        self.divide_button.grid(row=5, column=1, padx=10, pady=10)
        
        self.modulo_button = Button(ventana, text=" % ", width=20, height=1, command=self.modulo)
        self.modulo_button.grid(row=6, column=0, padx=10, pady=10)
        
        self.clear_button = Button(ventana, text=" CLEAR ", width=20, height=1, command=self.clear)
        self.clear_button.grid(row=6, column=1, padx=10, pady=10)
    
    def add(self):
        try:
            result_value = float(self.num1.get()) + float(self.num2.get())
            self.result.set(str(result_value))
        except ValueError:
            self.result.set("ERROR")
    
    def subtract(self):
        try:
            result_value = float(self.num1.get()) - float(self.num2.get())
            self.result.set(str(result_value))
        except ValueError:
            self.result.set("ERROR")
    
    def multiply(self):
        try:
            result_value = float(self.num1.get()) * float(self.num2.get())
            self.result.set(str(result_value))
        except ValueError:
            self.result.set("ERROR")
    
    def divide(self):
        try:
            result_value = float(self.num1.get()) / float(self.num2.get())
            self.result.set(str(result_value))
        except ValueError:
            self.result.set("ERROR")
        except ZeroDivisionError:
            self.result.set("ERROR")
    
    def modulo(self):
        try:
            result_value = float(self.num1.get()) % float(self.num2.get())
            self.result.set(str(result_value))
        except ValueError:
            self.result.set("ERROR")
    
    def clear(self):
        self.num1.set("")
        self.num2.set("")
        self.result.set("")


ventana= Tk()
Calculadora(ventana)
ventana.mainloop()
