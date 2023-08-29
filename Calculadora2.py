from tkinter import *

class Calculadora2:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.resizable(0,0)
        self.ventana.title("Calculadora 2")
        
        self.valor1 = StringVar()
        self.valor2 = StringVar()
        self.resultado = StringVar()
        self.operacion = StringVar(value="multiplicar")
        
        self.valor1_label = Label(ventana, text="Valor 1:")
        self.valor1_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.valor1_entry = Entry(ventana, textvariable=self.valor1)
        self.valor1_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.valor2_label = Label(ventana, text="Valor 2:")
        self.valor2_label.grid(row=2, column=0, padx=10, pady=5)
        
        self.valor2_entry = Entry(ventana, textvariable=self.valor2)
        self.valor2_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.resultado_label = Label(ventana, text="Resultado:")
        self.resultado_label.grid(row=3, column=0, padx=10, pady=5)
        
        self.resultado_entry = Entry(ventana, textvariable=self.resultado, state="readonly")
        self.resultado_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.operaciones_label = Label(ventana, text="Operaciones:")
        self.operaciones_label.grid(row=0, column=3, padx=10, pady=5)
        
        self.sumar_radio =Radiobutton(ventana, text="Sumar", variable=self.operacion, value="sumar")
        self.sumar_radio.grid(row=1, column=3, padx=10, pady=5, sticky="w")
        
        self.restar_radio =Radiobutton(ventana, text="Restar", variable=self.operacion, value="restar")
        self.restar_radio.grid(row=2, column=3, padx=10, pady=5, sticky="w")
        
        self.multiplicar_radio = Radiobutton(ventana, text="Multiplicar", variable=self.operacion, value="multiplicar")
        self.multiplicar_radio.grid(row=3, column=3, padx=10, pady=5, sticky="w")
        
        self.dividir_radio = Radiobutton(ventana, text="Dividir", variable=self.operacion, value="dividir")
        self.dividir_radio.grid(row=4, column=3, padx=10, pady=5, sticky="w")
        
        self.calcular_button = Button(ventana, text="Calcular", command=self.calcular)
        self.calcular_button.grid(row=4, column=1, padx=10, pady=10)
        
    def calcular(self):
        try:
            val1 = float(self.valor1.get())
            val2 = float(self.valor2.get())
            if self.operacion.get() == "sumar":
                resultado = val1 + val2
            elif self.operacion.get() == "restar":
                resultado = val1 - val2
            elif self.operacion.get() == "multiplicar":
                resultado = val1 * val2
            elif self.operacion.get() == "dividir":
                resultado = val1 / val2
            self.resultado.set(str(resultado))
        except ValueError:
            self.resultado.set("ERROR")


ventana = Tk()
Calculadora2(ventana)
ventana.mainloop()
