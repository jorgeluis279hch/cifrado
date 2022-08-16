
#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# cifrado de ficheros y palabras
# created by Jorge L. Herrera

from os import path
from string import ascii_letters, digits, punctuation
from sys import argv

abc = ascii_letters + digits + punctuation

SECUENCE = 3


def cryptAndDecrypt(char, mode):
    index = abc.find(char)
    if index == -1:
        return char

    if index >= len(abc) - SECUENCE:
        total = index - len(abc)
        return abc[total + SECUENCE] if mode else abc[total - SECUENCE]

    else:
        return abc[index + SECUENCE] if mode else abc[index - SECUENCE]


def crypt_file(file):
    try:
        with open(file, "rt+") as f:
            file_content = f.read()
            encrypt = ''.join([cryptAndDecrypt(char, True) for char in file_content])
           
            f.seek(0)
            f.write(encrypt)
            f.truncate()


        if path.exists(file):
            return True

        else:
            print('Archivo invalido')

    except FileNotFoundError:
        print('Archivo no encontrado')


def decrypt_file(file):
    try:
        with open(file, "rt+") as f:
            reader = f.read()
            decrypt = ''.join([cryptAndDecrypt(char, False) for char in reader])
           
            f.seek(0)
            f.write(decrypt)
            f.truncate()


        if path.exists(file):
            return True

        else:
            print('Archivo invalido')

    except FileNotFoundError:
        print('Archivo no encontrado')
