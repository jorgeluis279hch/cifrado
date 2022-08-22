#!/usr/bin/env python
#-*-encoding: utf-8 -*-
# cryptV1.2.0
# python3.7.0

from tkinter import Tk, Button, Label, PhotoImage
from tkinter import filedialog
from src.functions import crypt_file, decrypt_file
from sys import exit
from PIL import ImageTk, Image
import customtkinter


# Theme
customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


root = Tk()
root.title("CryptV1.0 - Herramienta de cifrado de archivos")
root.geometry("480x240")
root.configure(bg="#fff")
root.resizable(0,0)

def explore():
	return filedialog.askopenfilename(
		initialdir="C:/",
		title="Selecciona el archivo de texto",
		filetypes=(("Text Files", "*.txt"),)
	)
	
def crypt():
	if crypt_file(explore()):
	    poppup("Archivo cifrado correctamente","green")
	else:
	    poppup("Error Inesperado","#F87474")

def decrypt():
	if decrypt_file(explore()):
	    poppup("Archivo descifrado correctamente","yellow")
	else:
		poppup("Error Inesperado","#F87474")

def poppup(title_poppup, bgcolor):
	popupRoot = Tk()
	popupButton = Button(popupRoot,text=title_poppup,font=("Verdana", 12),bg=bgcolor).place(x=20, y=20)
	popupRoot.geometry('400x50+700+500')

	popupRoot.mainloop()



# controls
btn_file_input_a = customtkinter.CTkButton(master=root, text="Cifrar archivo", command=crypt, fg_color=("#FFB562")).place(x=10, y=10)
btn_file_input_b = customtkinter.CTkButton(master=root, text="Descifrar archivo", command=decrypt, fg_color=("#3AB0FF")).place(x=10, y=40)



switch_var = customtkinter.StringVar(value="off")

def switch_event():
    print("switch toggled, current value:", switch_var.get())

# password
switch_1 = customtkinter.CTkSwitch(master=root, text="Usar contraseña", command=switch_event, variable=switch_var, onvalue="on", offvalue="off").place(x=10, y=80)


# Algorith
optionmenu_var = customtkinter.StringVar(value="Cifrado cesar")  # set initial value

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(master=root,
                                     values=["Cifrado cesar", "Cifrado de Vigenère","Algoritmo RSA"],
                                     command=optionmenu_callback,
                                     variable=optionmenu_var).place(x=10, y=100)

# loading estetic elements
label = Label(root, text="Creado por: Jorge L. Herrera Chavez").place(x=120, y=220)

# img
img = ImageTk.PhotoImage(Image.open("assets/lockFileImg.png"))
imglabel = Label(root, image=img, bd=0).place(x=200, y=0)       




root.mainloop()

