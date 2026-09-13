import tkinter
import tkinter as tk
from operator import concat
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
ventana.wm_state("normal")#normal, iconic(minimizada),withdrawn(oculta)
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
#tambien se puede poner pad como atributo en configure para gestionar el tamaño pero por dentro

#Se puede usar grid_anchor para ubicar la tabla en la ventana (con ejes cardenales tambien)

#POSICIONAMIENTO ABSOLUTO: place(x=,y=,width,height) para hacerlo relativo se usa con porcentajes 0.num y el prefijo rel
#Anchor tambien jala con este :D

#se usa place para colocar grids dentro de otros grids. y en vez de poner ventana se pone en los marcos.

#BOTONCITO DE ELECCION MULTIPLE: tk.Listbox() se insertan los elementos con .insert (se puede meter individualmente o
# en lista=('','') se pone con *lista, elmodo de seleccion es con seleccionmode = tk.----, se pueden obtener el numero
#de elementos con .size(), con .get() pus geteas xd, se puede delitear, la visualizacion inicial es con .see( n )
# siendo n el numero del elemento de la lista
lista = tk.Listbox(ventana)
elecciones = ('Enrique','Pedro','Jose','Pedrito','juanpablo','dnaiel')
lista.insert(0,*elecciones)
lista.pack(pady=10)

def mostrarSeleccion():
    seleccion = lista.curselection()
    elementosSeleccionados = [lista.get(i) for i in seleccion]

lista.bind("<<ListboxSelect>>",lambda evento: mostrarSeleccion())

#existen scrollbars para pus escrolear xd
scrollbar = tk.Scrollbar(ventana)
scrollbar.pack (side = "left",fill = "y")
#el scrollbar se puede empaquetar para limitar la barra y se puede orientar con orientation

#TIPOS DE EVENTOS:
#Raton,teclado y foco, geometria y estado,eventos temporales
#se definen en funciones o metodos controladores

def doble_cliq_izquierdo(e):
    print("Doble clic con el boton izquierdo")

ventana.bind("<Double-Button-1>", doble_cliq_izquierdo)
#.bind es vincular y el primer argumento es el evento en si en este caso doble cliq
#Tambiwn se puede con command en algunos
def saludo():
    print("Saludo")

boton3 = tk.Button(ventana, text="Saludo", command=saludo,
                  cursor="hand2",
                  font=fuente)
boton3.pack(anchor = tk.NW)
#Se pueden crear objetos con tk.Event() donde se encapsula el tipo de evento widget, teclas , etc.
#Existe: .type,.widget,.char,.keysym,keycode,state,x,y,x_root,time,num,delta

#EVENTOS NO VIRTUALES: gestionados por el SO,se representan en etiqueta, y VIRTUALES: gestionados por tkinter con << >>
#Hay preestablecidos y se pueden hacer nuevos ; estos eventos nuevos son con .event_generate()

#EVENTO RATON: se toman como funciones o archivos aparte, tienen q estar declarados-
#EVENTO BUTTON: con cualquier boton comun de un raton, se puede combiar valores por ejemplo de etiquetq con una
#funcion con el objeto + .config dentro del event controller
#Hay double-button, buttonPress y buttonRelease tambien hay triple-button
def clic(e):
    print("Clic")
def clicder(e):
    print("Clic derecho")
boton3.bind("<Button-1>", clic)
boton3.bind("<Button-2>",clicder)
#existe el evento motion que sirve para cuando el cursor pasa por encima se puede hacer Bn-button para rastrear ,
# el arrastre de algo, para realizar animaciones de entrada y salida del cursor sobre un espacio se usa <enter>
# y leave, mousewheel esta ahi

#TECLADO: key-press(solo, indica q se uso el teclado, con .keysym se guarda la tecla presionada), para teclas en
#especifico sirve con <nombre que tenga la tecla en el SO>, con esto se pueden hacer acciones con crtl-algo y mas cosas.
#con keycode nos da el codigo de cada tecla y finalmente tambien esta keypress y keyrelease q funcionan como el mouse.

#GEOMETRIA y ESTADO: se puede usar <Config> en el bind para verificar el tamaño de la ventana o un objeto en especifico
#con el evento.width o .height, tambien esta expose que determina un poco el estado. se puede retirar el texto con
#pack_forget(). Map y Unmap sirven para determinar si la ventana esta visible o minimizada
#Con destroy se detecta si se destruye algo xd, y se destruye cerrando una ventana o con destroy()

#EVENTOS TEMPORALES: metodo after ej .after(tiempo en ms, metodo a ejecutar), basicamente es un countdown para realizar
#algo, se podria usar para secuenciar. con .after_cancel(var del .after) podemos cancelar el temporizador antes de q
# este se ejecute, con .after_info(objeto de el/los after) se pude determinar el id de los eventos , .after_idle(metodo)
#nos sirve para realizar verificaciones constantemente como para actividades en segundo plano.

#Eventos Foco : se dan cuando un elemento gana o pierde el primer plano .focus_display{on/of}()

#VARIABLES DE CONTROL: EL  texto o valores de las etiquetas y otros objetos no se actualiza de forma manual, se necesita
#un metodo por lo general, pero con las variables de control de tkinter nos podemos ahorrar muchas funciones.
#se llaman con tkinter.StringVar(), o tkinter.IntVar(), DoubleVar y booleanVar.
#NOTA: EN TKINTER SE USAN LOS ATRIBUTOS VARIABLE Y TEXTVARIABLE PARA ENLAZAR WIDGETS CON VARIABLES YA SEA DE STRING O
#OTRA COSA. TEXTVARIABLE SE USA PARA LABEL Y ENTRY , LAS VARIABLE PARA CHECK Y RADIO BUTTON.

#Checkbutton: se usa con .Checkbutton(objeto, text="Lo que sea"), se pueden asignar valores personalizados a las opciones,
#con on/offvalue, y la variable con variable como atributos los 3.También se puede determinar si deseaas que el
# checkbutton este selecionado o deselecccionado desde el inicio. para hacer que funcionen individualmente pero
# sincronizadas se requieren de una variable de control por checkbutton.

#Radiobutton: similar a checkbutton, solo q solo deja una opcion para todo . para que todos los radios se relacionen
#hay q enlazarlos a una variable de control, en este caso con la misma variable de control pero le asignamos un value con
#el atributo value. Para registrar el valor se puede usar un button con un command= lambda: funcion(option.get()).pack,
#el Lambda se utiliza porque se pasan argumentos. Se puede hacer sin el boton pero se ira cambiando de manera inmediata,
#Lo que no siempre es recomendable, esto se hace poniendo el metodo como command, tambien directamente en el metodo, se
# puede usar la var con .get para evitar el uso de la lambda, con .set() en la variable de control podemos establecer
# un valor por defecto.

#MESSAGEBOX: hay q especificar con import from tkinter messagebox as msg por ejemplo, para ni tener q poner cada vez
# tkinter.mesa.... ,existe .showinfo("Titulo","Contenido"), showWarning, tambien esta showerror.Estos son mensajes
#No interactivos, los interactivos son  : askyesno y hay q guardar el valor y asknocancel y askretrycancel, en
# askquestion que es igual a askyesno se devuelve el string en ves de el booleano y finalmente askyesnocancel.

#WIDGET SCALE(): Es una barra deslizante con valores limites, util para barras de brillo o volumen. Los atributos son:
#from/to, showValue=boleano, orient, command, lenght:para hacerlo mas o menos rapido el recorrido, tickinterval: muestra
#los valores por intervalos fijos y el sliderlenght q es para la longitud de el slider, con resolution se ve de cuanto
#en cuanto avanza, y se pueden poner estilos incluyendo un atributo label

#PANEDWINDOW WIDGET: Este nos sirve para poner frames con .add y sirve como la de windows y se pueden redimensionar los
#paneles desde el UI. con paneconfig y se puede usar stretch="always" para distribuir el espacio equitativamente, se
#puede distribuir el tamaño de los marcos,se pueden usar estilos y usarse vertical y horizontal.

#SPINBOX: valor numerico que se puede incrementar se usa from_/to, increment para el gap, se pueden usar tambien valores
#de texto con values=lista, se usa textVariable y la variable de control puede establecer valores por defecto, tambien
#se pueden usar estilos tambien. COn wrap: si es true deja moverse en ambas direcciones pero en false solo deja ascender.

#MODULO ESTILO TTK: se importa from tkinter tkk, se pone en ves de tk en los objetos y adopta los estilos del SO, los temas
#claro y oscuro se pueden configurar creando un style = ttk.Style() con .theme_use("nuevo EStilo"), esto permite tener
#otro tipo de estilos diferentes al del SO ya definidos en ttk https://wiki.tcl-lang.org/page/List+of+ttk+themes, este
#style es basicamente un css por lo que se puede establecer con .configure("Tobjeto", atributos), hay que descargar los
#temas y ponerlos con ttkthemes import themedtk y la ventana hay q hacerla una raiz, lo demas funciona igual.

#COMBOBOX: widget de ttk que es una lista desplegable es con ttk.Combobox(), los valores se pasan en una lista en
# values = y el state es para deteminar si el usuario puede modificar o solo seleccionar con 'readonly', seu puede usar
#como los demas con un boton y una funcion q lea o con un bind(<<Comboboxselected>>, funcion) en este la funcion(evento)
#tambien se puede .config(state="disabled") para bloquear, con .current(i) se puede determinar una seleccion inicial.
#si usamos state="normal" se puede editar y posteriormente mandar nuevos valores que se guardan durante la ejecucion

#MENU, este si es de tkinter de base, se declara con tk.Menu () y a ese menu le creamos un tk.Menu(menuGeneral,tearoff=0)
#El teoroff indica si el menu se puede desprender o no, esto mediante boleanos, on 0 es false y !=0 es true
#este segundo menu es el primer desplegable por asi decirlo y a este se ñe agregan los comandos con . command(label="")
#despues añadimos con .add_cascade(label,menu=segundoMenu) y con ventana.config(menu=menuInicial), se pueden hacer barra
#dividorias dentro de la cascadas con un metodo .add_separador entre la declaracion de los comandos.
#Se pueden adjuntar checkbutton a los menus con .add_checkbutton (label,variableControl), las variables de control deben
# ser boleanas, los radiobuttons se pueden añadir de igual forma, solo que con String variables, hay casos donde algunas
#opciones no tiene sentido estar habilitadas, por lo que a veces nos conviene tener las opciones desactivadas, esto con
#.entryconfig("command", state="disabled"), se pueden hacer submenus dentro de los submenus añadiendo con tk.Menu(submenu)
#añadir los comandos normalmente y añadir una cascada pero en la nueva variable del subsubmenu, loa atajos se ponen dentro
#de la adicion de los comandos con accelerate ="" y se delaran loe eventos con .bind en la ventana.

#MENUBUTTON: es como la anterior con la diferencia de no tener soporte, es como un boton con cascada

#VENTANAS SECUNDARIAS: con TopLevel ventana_secundaria = tk.TopLevel() se personaliza igual  que la principal.

#SIZEGRIP: es un icono en la esquina para indicar al usuario que es redimensionable de ttk, se ubica con
# .place(relx,rely,anchor="se)

#MANEJO IMAGENES: en tk con .PhotoImage (file("ruta")), esta imagen se carga en un soporte con la propiedad image, los
#archivos deben ser png se puede usar .subsample(i,j) para reducir el tamaño en alto y ancho en el ratio inticado
#podemos importat Image y ImageTk de PIL para manejar imagenes de mejor manera. Primero se abre la imagen con Image.open
#(ruta), despues la onvertimos a Image.PhotoImage(Imagen_pil) y ahi ya se usa normalmente. El icono de la ventana se
#puede modificar con ,iconPhoto(False,imagen), tambien podemos redimensionar imagenes, esto con .resize((x,y)) y esta
#imagen se puede guardar con .save(), esto se puede recortar con una lista que contenga: lista = (izq,arr,der,abjo)
#y la imagen con .crop(lista), la imagen se rota con .rotate(direccion en grados), tambien se puede convertir una
#img a blaconegro con .convert() se puede convertir entre "L", "RGB","CMYK". La libreria se ve con
# https://pillow.readthedocks.io/en/stable/handbook/index.html

#WIDGET NOTEBOOK: son marcos mostrados en pestañas, HERMOSO, se llama con ttk.Notebook(ventana), se crean los frames
# necesarios, 1 por pestaña y estos marcos se añaden con .add(marco,texto), ahora lo importante como se manipulan?,
# para modificar el nombre de la ventana se realiza con: .tab(i,nuevotexto), siendo la i el numero tipo array empezando
# con 0. se desabilita con state='diabled'. Se pueden controlar las ventanas mediante funciones con botones, esto en la
#funcion se toma con notebook.select(i) con .index("current")

#FILEDIALOG:Sirve para el manejo de archivos es de tkinter pero se recomienda importatlo separado, se usa
# .askopenfilename() y se guarda en ina variable detro de askopenfile se pueden pasar argumentos como (title,
# initialdit=".", filetypes=[("tipoArchivo","*  .algo"),("Todos los archivo","*.*")])todos para la ventana,
#Si se pone ,as de un archivo se requeriria de un for y  .askopenfilenames(), tambien esta asksaveasfilename() que
#funciona igual solo q en ves de abrir guardar, con ask directory pide la ruta de directorio

#Treeview: muestra elementos de forma jerarquica o tabular, metodo de ttk. como en un explorador de archivos o una tabla
#como todos con .Treeview(), se necesita una lista de columnas que se insertan como atributo columns y despues se
# definen los encabezados con .heading(tupla, text), las filas se añaden con .insert("",tk.END,values=()), el primer
#atributo es la jerarquia pero al trabajar con tablas pues no hay, la segunda indica que las filas se añadiran una
#tras otra, y los valores pus son los valores, a las columnas se estilizan con .column("nombreTupla", otros atributos)
#Treview reserva una columna #0 que guarda par poner un arbol jerarquico esta se oculta, cuando se haga el treview
#se pone el atributo show="headings", este eidget tiene mucho potencial para manejo de datos y archivos.
#Para hacer el arbol se usa en el .column y el heading "#0" esto crea una especie de menu desplegable

#CANVAS: con este se puede dibujar y crear animaciones , Es de tk,primero se hace el lienzo con .Canvas()y los taributos
# son los de diseño y esta highlightthickness, y dentro de este canvas se pueden crear lineas rectangulos ovalos y
# poligonos , indicando las medidas (xi,yi,xf,yf,estilos), las animaciones se hacen con canvas.move y canvas.coords

#PROGRESS BAR: pus es una barra de progreso, es de ttk, y es Progressbar(ventana,orient,lenght,mode), en mode se pone,
# determinate o indeterminate para moverla, con .configure(maximum,value), ya con funciones y var_control se puede hacer
#que se vaya moviendo, para el movimiento tiene los metodos .start(mseg por paso) y .stop(), tambien esta .cget("value")
#para obtener el progreso como tal de la barra

#POO CON tkinter: primero creamos clases para separar

#EJEMPLO

class MiInterfaz:
    def __init__(self):
        pass
#Todo tiene que llevar self


etiqueta.pack()
boton.pack()
entrada.pack()
texto.pack()
ventana.mainloop()