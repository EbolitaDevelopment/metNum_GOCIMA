import tkinter as tk
from mimetypes import init
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk


class AplicacionBiblioteca:
    def __init__(self):
        self.root = ThemedTk(theme="clam")

        self.root.title("BIBLIOTECA DE MÉTODOS NUMÉRICOS")
        self.root.geometry("500x500")
        self.root.resizable(0, 0)
        self.root.mainloop()


