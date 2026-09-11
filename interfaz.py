import tkinter as tk
from struct import pack

ventana = tk.Tk()
ventana.title("Biblioteca de métodos numéricos")
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
alto_ventana = 700
ancho_ventana = 800
posicion_x=400 # o round(ancho_pantalla/2 - ancho_ventana/2)
posicion_y=50   # o round(alto_pantalla/2 - alto_ventana/2)
ventana.geometry(f"{alto_ventana}x{ancho_ventana}+{posicion_x}+{posicion_y}")
#para evitar resizable
ventana.resizable(0,0)
#estados para ventanas
ventana.wm_state("iconic")#normal, iconic(minimizada),withdrawn(oculta)
#se pone pantalla completa al inicio
fuente = ("Roboto",36,"bold")
etiqueta = tk.Label(ventana, text="Primer etiqueta",
                    bd=25,
                    cursor="arrow",
                    disabledforeground="black",
                    font=fuente,
                    fg="white",
                    borderwidth=1,
                    relief="solid")

boton = tk.Button(ventana, text="Primer boton",
                  bd=25,
                  cursor="hand2",
                  disabledforeground="black",
                  font=fuente )

entrada = tk.Entry(ventana, width=50,
                   bd=25,
                   disabledforeground="black",
                   font=fuente
                   )
marco = tk.Frame(ventana)
marco.pack()
#texto = tk.Text(ventana, width=50)
#Posicionar ventanas bloqueos, etc
#METODO INDEX(posicion del cursor)
texto = tk.Text(ventana, width=50,)
def posicionCursor (event):
    pos = texto.index(tk.INSERT)
    print(pos)
    pass
#Asociar pulsaciones de teclas
texto.bind("<Key>", posicionCursor)
button1 = tk.Button(ventana, text="Primer boton").pack(anchor = tk.NW)
#PACK
#NW(northwest),norteast(NE)....
#Se puede poner before o after en el pack para la precedencia de los elementos
#atributo fill: both,none,x o y
#padding con padx y pady , side
#GRID
#Los grids se forman con labels y .grid indicando row=i column=j columnspan para ocupar mas de un espacio de columna
#y lo mismo respectivamenre con rowspan , se hace lo mismo de nw,s,n con sticky

#EN VENTANA se puede usar .rowconfigure para resposividad (numfila, weight); el peso es lo q divide los pixeles
#para porcentajes y asi hacerlos responsivos tambien con columnconfigure; con sticky = nsew para distribuir
#responsivamente en todo el espacio
#tambien se puede usar maxsixe y minsize para ´poner restricciones en la responsibidad se puede usar como atributo
#en row y column configure, o añadirlo a los omponentes con .minsize y .maxsize


etiqueta.pack()
boton.pack()
entrada.pack()
texto.pack()
ventana.mainloop()