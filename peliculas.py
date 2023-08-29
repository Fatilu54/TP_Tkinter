from tkinter import *

class Peliculas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Películas")
        self.ventana.resizable(0,0)
        self.ventana.geometry("400x290")
        self.peliculas = []
        
        self.label1 = Label(ventana, text=" Escribe el título de una película: ")
        self.label1.grid(row=0, column=0)
         
        self.pelicula_entry = Entry(ventana)
        self.pelicula_entry.grid(row=1, column=0)
 
        self.add_button = Button(ventana, text="  Añadir  ", command=self.add_pelicula)
        self.add_button.grid(row=2, column=0)
        
        self.label2 = Label(ventana, text="Películas: ")
        self.label2.grid(row=0, column=1)
        
        self.listbox = Listbox(ventana)
        self.listbox.grid(row=1, column=1, padx=10, pady=10)

       
    def add_pelicula(self):
        pelicula = self.pelicula_entry.get()
        if pelicula:
            self.peliculas.append(pelicula)
            self.pelicula_entry.delete(0, END)
            self.update_listbox()
    
    def update_listbox(self):
        self.listbox.delete(0, END)
        for pelicula in self.peliculas:
            self.listbox.insert(END, pelicula)

    

ventana = Tk()
Peliculas(ventana)
ventana.mainloop()
