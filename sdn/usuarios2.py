import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

# Función para manejar el evento del botón "Crear Usuario"
def crear_usuario():
    global usuario, contrasena

    # Cargar usuarios existentes
    df_usuarios = cargar_usuarios(archivo_usuarios)

    # Agregar nuevo usuario
    nuevo_usuario = pd.DataFrame({'Usuario': [usuario.get()], 'Contraseña': [contrasena.get()]})
    df_usuarios = pd.concat([df_usuarios, nuevo_usuario], ignore_index=True)

    # Guardar usuarios en el archivo Excel
    df_usuarios.to_excel(archivo_usuarios, index=False)

    # Limpiar campos
    usuario.set('')
    contrasena.set('')

    # Mostrar mensaje
    messagebox.showinfo('Usuario creado', 'Usuario creado exitosamente')

# Cargar usuarios existentes desde el archivo
def cargar_usuarios(archivo):
    if os.path.exists(archivo):
        df = pd.read_excel(archivo)
        return df
    else:
        return pd.DataFrame(columns=['Usuario', 'Contraseña'])

# Función principal
def main():
    global usuario, contrasena, archivo_usuarios

    ventana = tk.Tk()
    ventana.title('Registro de Usuarios')

    # Variables
    usuario = tk.StringVar()
    contrasena = tk.StringVar()
    archivo_usuarios = 'usuarios.xlsx'  # Definir archivo_usuarios aquí

    # Crear widgets
    etiqueta_usuario = tk.Label(ventana, text='Usuario:')
    etiqueta_contrasena = tk.Label(ventana, text='Contraseña:')
    entrada_usuario = tk.Entry(ventana, textvariable=usuario)
    entrada_contrasena = tk.Entry(ventana, textvariable=contrasena, show='*')
    boton_crear_usuario = tk.Button(ventana, text='Crear Usuario', command=crear_usuario)

    # Colocar widgets en la ventana
    etiqueta_usuario.grid(row=0, column=0, padx=10, pady=10)
    entrada_usuario.grid(row=0, column=1, padx=10, pady=10)
    etiqueta_contrasena.grid(row=1, column=0, padx=10, pady=10)
    entrada_contrasena.grid(row=1, column=1, padx=10, pady=10)
    boton_crear_usuario.grid(row=2, column=1, pady=10)

    # Iniciar el bucle de eventos de la ventana
    ventana.mainloop()

if __name__ == '__main__':
    main()
