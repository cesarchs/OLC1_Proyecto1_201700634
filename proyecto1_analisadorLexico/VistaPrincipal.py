# arreglar problema de importar y que no lo ejecute de una vez, aunque funciono poniendo el import en el metodo       
# import AnalisisLexicoHtml
# import AnalisadorLexicoCss

# from tkinter import *    # Carga módulo tk (widgets estándar)
# from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog

root = Tk()
root.title("PROYECTO 1 ANALIZADORE LEXICOS")
root.configure(background = "yellow")

'''FUNCIONES DEL MENU'''

archivo = ""

def nuevo():
    global archivo
    editor.delete(1.0, END)#ELIMINAR EL CONTENIDO
    archivo = ""

def abrir():
    global archivo
    archivo = filedialog.askopenfilename(title = "Abrir Archivo", initialdir = "C:/")

    entrada = open(archivo)
    content = entrada.read()

    editor.delete(1.0, END)
    editor.insert(INSERT, content)
    entrada.close()

def salir():
    value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
    if value :
        root.destroy()

def guardarArchivo():
    global archivo
    if archivo == "":
        guardarComo()
    else:
        guardarc = open(archivo, "w")
        guardarc.write(editor.get(1.0, END))
        guardarc.close()

def guardarComo():
    global archivo
    guardar = filedialog.asksaveasfilename(title = "Guardar Archivo", initialdir = "C:/")
    fguardar = open(guardar, "w+")
    fguardar.write(editor.get(1.0, END))
    fguardar.close()
    archivo = guardar

def analisarhtml ():
    import AnalisisLexicoHtml
    AnalisisLexicoHtml.nombre=archivo

def analisarCss ():
    import AnalisadorLexicoCss
    AnalisadorLexicoCss.nombre=archivo

# MENU Y BARRA DE OPCIONES
barraMenu = Menu(root)
root.config(menu = barraMenu, width = 1000, height = 600)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label = "Nuevo", command = nuevo)
archivoMenu.add_command(label = "Abrir", command = abrir)
archivoMenu.add_command(label = "Guardar", command = guardarArchivo)
archivoMenu.add_command(label = "Guardar Como...", command = guardarComo)
archivoMenu.add_separator()
archivoMenu.add_command(label = "Salir", command = salir)

archivoMenu2 = Menu(barraMenu, tearoff=0)
archivoMenu2.add_command(label = "Analisis HTML", command = analisarhtml)
archivoMenu2.add_command(label = "Analisis CSS", command = analisarCss)
archivoMenu2.add_command(label = "Analisis JAVASCRIPT", command = nuevo)

barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
barraMenu.add_cascade(label = "Analisadores", menu = archivoMenu2)
barraMenu.add_command(label = "Salir",  command = salir)

frame = Frame(root, bg="green")
canvas = Canvas(frame, bg="green")
scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
scroll = Frame(canvas, bg="black")

scroll.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scroll, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set, width = 1300, height = 600)

ttk.Label(scroll, text = "ANALISIS LEXICO", font = ("Arial", 17), background='black', foreground = "white").grid(column = 1, row = 0)

editor = scrolledtext.ScrolledText(scroll, undo = True, width = 50, height = 20, font = ("Arial", 15), background = 'white',  foreground = "black")

editor.grid(column = 1, row = 1, pady = 25, padx = 10)


editor2 = scrolledtext.ScrolledText(scroll, undo = True, width = 50, height = 20, font = ("Arial", 15), background = 'yellow',  foreground = "black")

editor2.grid(column = 5, row = 1, pady = 25, padx = 10)

frame.grid(sticky='news')
canvas.grid(row=0,column=1)
scrollbar.grid(row=0, column=2, sticky='ns')



editor.focus()
root.mainloop()
