from tkinter import *

class Contador:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("ContCreciente")
        self.ventana.resizable(0,0)
        self.ventana.geometry("250x40")
        self.contador_value = 0

        self.label = Label(ventana, text="Contador   ")
        self.label.grid( row=1, column=1)
        
        self.contador_display = Entry(ventana, state="readonly")
        self.contador_display.insert(0, str(self.contador_value))
        self.contador_display.grid(row=1, column=2)
        
        self.incrementar_button = Button(ventana, text="  +  ", command=self.incrementar)
        self.incrementar_button.grid(row=1, column=3)


    def incrementar(self):
        self.contador_value += 1
        self.contador_display.config(state="normal")
        self.contador_display.delete(0, END)
        self.contador_display.insert(0, str(self.contador_value))
        self.contador_display.config(state="readonly")


ventana=Tk()
contador=Contador(ventana)
ventana.mainloop()
