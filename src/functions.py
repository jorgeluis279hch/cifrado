
#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# cifrado de ficheros y palabras
# created by Jorge L. Herrera

from os import path

SECUENCIA = 2

def crypt_text(file):
    try:
        with open(file, "rt+") as f:
            reader = f.read()

            to_char = [ord(_) + SECUENCIA for _ in reader]
            encrypt = ''.join([chr(_) for _ in to_char])
           
            f.seek(0)
            f.write(encrypt)
            f.truncate()


        if path.exists(file):
            return True

        else:
            print('Archivo invalido')

    except FileNotFoundError:
        print('Archivo no encontrado')


def decifrar_txt(file):
    try:
        with open(file, "rt+") as f:
            reader = f.read()

            to_char = [ord(_) - SECUENCIA for _ in reader]
            encrypt = ''.join([chr(_) for _ in to_char])

           
            f.seek(0)
            f.write(encrypt)
            f.truncate()


        if path.exists(file):
            return True

        else:
            print('Archivo invalido')

    except FileNotFoundError:
        print('Archivo no encontrado')
