import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from ui.mainInterfaz import AplicacionBiblioteca

ventana = ThemedTk()
ventana.set_theme("clam")
ventana.geometry("500x500")
marco = ttk.Frame(ventana)
boton = ttk.Button(ventana,text='Ezquizofenia')

marco.pack(fill="both", expand=True)
boton.pack(side="right", fill="both", expand=True)

ventana.mainloop()
#AplicacionBiblioteca()


