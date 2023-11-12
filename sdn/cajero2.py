import tkinter as tk
from tkinter import messagebox
import subprocess
import pandas as pd

login = tk.Tk()
menu = None
deposito_menu = None
retiro_menu = None
consulta_menu = None
usuario = tk.StringVar()
clave = tk.StringVar()
saldo_global = tk.DoubleVar()
cantidad = tk.DoubleVar()

# Asignamos el saldo inicial
saldo_global.set(300)

# Cargar usuarios desde el archivo Excel
def cargar_usuarios_desde_excel(archivo_excel):
    try:
        df = pd.read_excel(archivo_excel)
        return df
    except Exception as e:
        print(f"Error al cargar el archivo Excel: {e}")
        return None

# Validar usuario y clave con datos del archivo Excel
def validar_usuario_y_clave():
    global usuario, clave
    archivo_excel = "C:/Users/JULIAN/Desktop/usuarios.xlsx"  # Reemplaza con la ruta correcta
    usuarios_df = cargar_usuarios_desde_excel(archivo_excel)

    if usuarios_df is not None:
        # Imprime el DataFrame
        usuario_ingresado = usuario.get()
        clave_ingresada = clave.get()

        # Iterar a través de todas las filas del DataFrame
        for index, row in usuarios_df.iterrows():
            usuario_definido = str(row['Usuario']).strip()
            clave_definida = str(row['Contraseña']).strip()

            if usuario_definido == usuario_ingresado and clave_definida == clave_ingresada:
                crear_menu_opciones()
                return

        messagebox.showinfo("Error", "Usuario o contraseña incorrectos")
    else:
        print("No se pudo cargar el archivo de usuarios. Verifica la ruta y el formato del archivo.")

# Funciones para manejar las opciones del menú
def crear_menu_opciones():
    global menu
    menu = tk.Tk()
    menu.title("Opciones")
    menu.geometry("300x300")
    tk.Button(menu, text="Deposito", command=deposito).place(x=30, y=60)
    tk.Button(menu, text="Retiro", command=retiro).place(x=30, y=120)
    tk.Button(menu, text="Consulta", command=consulta).place(x=180, y=60)
    tk.Button(menu, text="Salir", command=menu.quit).place(x=180, y=120)
    login.iconify()

# Funciones para manejar las opciones del menú
def retiro():
    global retiro_menu
    global saldo_global
    retiro_menu = tk.Tk()
    retiro_menu.title("Retiro")
    retiro_menu.geometry("300x300")
    tk.Label(retiro_menu, text="Saldo Disponible").place(x=50, y=50)
    label = tk.Label(retiro_menu, text=str(saldo_global.get()))
    label.place(x=200, y=50)
    entry = tk.Entry(retiro_menu, textvariable=cantidad)
    entry.place(x=150, y=80)
    tk.Button(retiro_menu, text="Retirar", command=lambda: [get_retiro(entry.get()), actualizar_label(label)]).place(x=50, y=80)
    tk.Button(retiro_menu, text="Atrás", command=lambda: regresar_menu(retiro_menu)).place(x=200, y=200)
    menu.iconify()

def deposito():
    global deposito_menu
    global saldo_global
    deposito_menu = tk.Tk()
    deposito_menu.title("Deposito")
    deposito_menu.geometry("300x300")
    tk.Label(deposito_menu, text="Saldo Disponible").place(x=50, y=50)
    label = tk.Label(deposito_menu, text=str(saldo_global.get()))
    label.place(x=200, y=50)
    entry = tk.Entry(deposito_menu, textvariable=cantidad)
    entry.place(x=150, y=80)
    tk.Button(deposito_menu, text="Depositar", command=lambda: [set_deposito(entry.get()), actualizar_label(label)]).place(x=50, y=80)
    tk.Button(deposito_menu, text="Atrás", command=lambda: regresar_menu(deposito_menu)).place(x=200, y=200)
    menu.iconify()

def consulta():
    global consulta_menu
    global saldo_global
    consulta_menu = tk.Tk()
    consulta_menu.title("Consulta")
    consulta_menu.geometry("300x300")
    tk.Label(consulta_menu, text="Saldo Disponible").place(x=50, y=50)
    tk.Label(consulta_menu, text=str(saldo_global.get())).place(x=200, y=50)
    tk.Button(consulta_menu, text="Atrás", command=lambda: regresar_menu(consulta_menu)).place(x=200, y=200)
    menu.iconify()

# Funciones para manejar el saldo
def get_retiro(valor):
    global saldo_global
    if ((saldo_global.get() - float(valor)) < 0):
        messagebox.showinfo("Error", "Saldo Insuficiente")
    else:
        total = saldo_global.get()
        total -= float(valor)
        saldo_global.set(round(total, 2))

def set_deposito(valor):
    global saldo_global
    total = saldo_global.get()
    total += float(valor)
    saldo_global.set(round(total, 2))
    messagebox.showinfo("Éxito", "Depósito correcto")

def regresar_login():
    menu.iconify()
    login.deiconify()

def regresar_menu(sub_menu):
    sub_menu.iconify()
    menu.deiconify()

def actualizar_label(label):
    global saldo_global
    label.config(text=saldo_global.get())

# Función para crear el login
def crear_login():
    global saldo_global
    global login
    login.title("Ingreso al Cajero")
    login.geometry("300x300")
    tk.Label(login, text="Usuario").place(x=30, y=50)
    tk.Entry(login, textvariable=usuario).place(x=90, y=50)
    tk.Label(login, text="Clave").place(x=30, y=80)
    tk.Entry(login, textvariable=clave).place(x=90, y=80)
    tk.Button(login, text="Ingresar", command=validar_usuario_y_clave).place(x=130, y=110)
    tk.Button(login, text="Crear Usuario", command=crear_usuario).place(x=130, y=140)

# Función para crear usuario
def crear_usuario():
    try:
        # Reemplaza "python" con el intérprete de Python que estás utilizando
        subprocess.run(["python", "C:/Users/JULIAN/Desktop/usuarios2.py"])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo ejecutar el código: {e}")

# Ejecutar la aplicación
crear_login()
tk.mainloop()
