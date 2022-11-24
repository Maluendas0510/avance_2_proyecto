
from tkinter import *
from tkinter import messagebox



def DESAYUNOS():
    messagebox.showinfo("Comp 1.0", "Se esta comprobando...")
    z = int(x.get())
    
    if("desayunos"):
        if(opcion==1):
            print("\n---DESAYUNOS---\n 1.-Tortilla con queso y hierbas-\nIngredientes: 3 huevos batidos, 1 cucharada de hierbas de olor, 1 cucharada de mantequilla sin sal, 50 gramos de queso . \nModo de preparar: se mezcla todos los ingredientes excepto la mantequilla y el queso.calienta la mantequilla en un sartén y cuando esté caliente agrega la mezcla. Espera hasta que se forme el omelet, entonces coloca el queso encima y dobla por la mitad, se cocina por un minuto hasta que se derrita el quesoDisfruta.")
        elif(d==1):
            print("\n 2.-Panquecas de plátano-\nIngredientes: Tres plátanos hechos puré,100 gramos de mantequilla, 1 cucharada de miel. \nPreparación: forma las panquecas con el puré de plátano. Una vez formadas, fríelas en la mantequilla una por una, por alrededor de dos minutos.acompaña con miel y disfruta.")
        elif(d==1):
            print("\n 3.--Batido de papaya y piña--\n Ingredientes :\n 1 taza, (225 gramos) de piña en trozos,media taza (120 gramos) de papaya en trozos, media taza (125 ml) de cubos de hielo,60 ml de miel. \nPreparación: Vierte todos los ingredientes en la licuadora y licúa hasta que se mezclen. Sirve inmediatamente.")




    bt_desayuno = Button(frame_operaciones, text="sen(x)", command=DESAYUNOS)
    bt_desayuno.place(x=50,y=80, width=100, height=30)


def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos seran borrados.")
    x.set("")
    t_resultados.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrara.")
    ventana_principal.destroy()
    
    

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "skyblue2", width = 480 , height = 120)
frame_operaciones.place(x = 10, y = 220)

# Boton de inicio
logo = PhotoImage(file = "img/375.png")
bt_comp = Button(frame_operaciones, text="comprobar", image=logo, command=comp)
bt_comp.place(x = 45, y=45, width=100, height=30)

# titulo de la ventana
ventana_principal.title("Funciones")

# tamañan de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg= "black")

# etiqueta para el titulo de la app
titulo = Label(ventana_principal, text= "PROYECTO SEAT")
titulo.config(bg="black", fg="white", font=("Arial",18))
titulo.place(x=50,y=10, width=400, height=40)
# boton lineal
bt_desayunos = Button(ventana_principal, text="Desayunos", command=desayunos)
bt_desayunos.place(x=50,y=80, width=100, height=30)
#Boton borrar
bt_sumar = Button(frame_operaciones, text="Borrar")
bt_sumar.place(x=190, y=45, width=100, height=30)


#Boton borrar
bt_sumar = Button(frame_operaciones, text="Borrar",command=borrar)
bt_sumar.place(x=190, y=45, width=100, height=30)

# Boton salir
bt_salir = Button(frame_operaciones, text="Salir",command=salir)
bt_salir.place(x=335, y=45, width=100, height=30)

# fram resultados

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="skyblue1", width=480, height=140)
frame_resultados.place(x=10, y = 350)

#area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="lightsteelblue1", fg="black", font=("Arial",20))
t_resultados.place(x=10,y=10, width=460, height= 120)

ventana_principal.mainloop()