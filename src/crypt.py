#!/usr/bin/env python
#-*-encoding: utf-8 -*_

from tkinter import *
from tkinter import filedialog
from functions import crypt_text, decifrar_txt
from sys import exit
from PIL import ImageTk, Image

root = Tk()
root.title("CryptV1.0 - Herramienta de cifrado de archivos")
root.geometry("480x220")
root.configure(bg="#000")
root.resizable(0,0)

def explore():
	return filedialog.askopenfilename(
		initialdir="C:/",
		title="Selecciona el archivo de texto",
		filetypes=(("Text Files", "*.txt"),)
	)
	
def crypt():
	if crypt_text(explore()):
	    poppup("Archivo cifrado correctamente","green")
	else:
	    poppup("Error Inesperado","#F87474")

def decrypt():
	if decifrar_txt(explore()):
	    poppup("Archivo descifrado correctamente","yellow")
	else:
		poppup("Error Inesperado","#F87474")

def poppup(title_poppup, bgcolor):
	popupRoot = Tk()
	popupButton = Button(popupRoot,text=title_poppup,font=("Verdana", 12),bg=bgcolor).place(x=20, y=20)
	popupRoot.geometry('400x50+700+500')
	popupRoot.mainloop()

# controls
btn_file_input_a = Button(root, text="Cifrar archivo      ", command=crypt, bg="#FFB562").place(x=10, y=10)
btn_file_input_b = Button(root, text="Descifrar archivo", command=decrypt, bg="#3AB0FF").place(x=10, y=40)
# loading estetic elements

label = Label(root, text="Creado por: Jorge L. Herrera Chavez").place(x=120, y=200)

# img
img = ImageTk.PhotoImage(Image.open("imgLogo.png"))

imglabel = Label(root, image=img, bd=0).place(x=200, y=0)       

root.mainloop()

