from tkinter import *
from tkinter import messagebox
import random

# -----------------------------
# funciones de la app 
# -----------------------------

def tijera(): 
    messagebox.showinfo("Juego", "¡Has elegido tijera!")
    maq=random.randint (1,3)
    if maq == 1:
        resultado ="empate"
    elif maq == 2:
        resultado ="ganaste"
    else :
        resultado ="perdiste"
    t_resultados.insert(INSERT, resultado + "\n" )

def piedra():
    messagebox.showinfo("Juego", "¡Has elegido piedra!")
    maq=random.randint (1,3)
    if maq == 1:
        resultado ="empate"
    elif maq == 2:
        resultado ="ganaste"
    else :
        resultado ="perdiste"
    t_resultados.insert(INSERT, resultado + "\n" )
def papel():
    messagebox.showinfo("Juego", "¡Has elegido papel!")
    maq=random.randint (1,3)
    if maq == 1:
        resultado ="ganaste, la IA escogio piedra"
    elif maq == 2:
        resultado ="empate, la IA escogio papel"
    else :
        resultado ="perdiste, la IA escogio tijeras"
    t_resultados.insert(INSERT, resultado + "\n" )
# -----------------------------
# ventana principal de la app
# -----------------------------

ventana_principal = Tk()
ventana_principal.title("David Macías")
ventana_principal.geometry("800x500")
ventana_principal.resizable(0, 0)
ventana_principal.config(bg="ivory4")

# -----------------------------
# variables globales
# -----------------------------
a = StringVar()
b = StringVar()

# -----------------------------
# frame 1 entrada de datos
# -----------------------------

frame_1 = Frame(ventana_principal, bg="ivory2", width=780, height=240)
frame_1.place(x=10, y=10)

titulo = Label(frame_1, text="Colegio San José de Guanentá", bg="yellow", fg="blue", font=("Arial", 16))
titulo.place(x=250, y=10)

subtitulo1 = Label(frame_1, text="Especialidad en Sistemas", bg="yellow", fg="blue", font=("Arial", 12))
subtitulo1.place(x=300, y=50)

subtitulo2 = Label(frame_1, text="Piedra, Papel y Tijera", bg="ivory2", fg="blue", font=("Arial", 15))
subtitulo2.place(x=300, y=70)



# -----------------------------
# botón con imagen de piedra
# -----------------------------

img_piedra = PhotoImage(file="imagenes/piedra papel y tijeras.png")
bt_piedra = Button(frame_1, image=img_piedra, width=150, height=150)
bt_piedra.place(x=100, y=70)

# -----------------------------
# Frame 2 
# -----------------------------
frame_2 = Frame(ventana_principal, bg="ivory2", width=780, height=220)
frame_2.place(x=10, y=270)

img_bt_piedra= PhotoImage(file="imagenes/imagen.png") 
bt_piedra = Button(frame_2, image=img_bt_piedra, width=105, height=105, command=piedra) 
bt_piedra.place(x=150, y=7)

img_bt_papel = PhotoImage(file="imagenes/imagen2.png") 
bt_papel = Button(frame_2, image=img_bt_papel, width=105, height=105, command=papel) 
bt_papel.place(x=350, y=7)

img_bt_borrar = PhotoImage(file="imagenes/tijeritas.png") 
bt_borrar = Button(frame_2, image=img_bt_borrar, width=105, height=105, command=tijera) 
bt_borrar.place(x=520, y=7)


# ----------------------------
# frame 3
# ----------------------------


frame_3 = Frame(ventana_principal, bg="ivory2", width=790, height=130) 
frame_3.place(x=10, y=390) 
t_resultados = Text(frame_3, width=50, height=3, bg="green", fg="white", font=("Courier", 20)) 
t_resultados.pack()

# -----------------------------
# método principal
# -----------------------------
ventana_principal.mainloop()
