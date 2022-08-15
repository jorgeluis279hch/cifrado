#!/usr/bin/env python

from string import ascii_letters, digits, punctuation
from sys import argv

abc = ascii_letters + digits + punctuation
SECUENCE = 3

def crypt(char, mode):
	index = abc.find(char)
	if index == -1:
		return char

	if index >= len(abc) - SECUENCE:
		total = index - len(abc)
		return abc[total + SECUENCE] if mode else abc[total - SECUENCE]

	else:
		return abc[index + SECUENCE] if mode else abc[index - SECUENCE]

if len(argv) == 1:
	print('''faltan parametros
	Modo de uso:
	python script.py < c | d > : donde c de cifrar y d de descifrar
	''')
elif len(argv) == 2:
	text = str(input("Texto: "))
	if argv[1] == "c":
		
		print(f"Encripted -> {SECUENCE}: {encrypt}")

	elif argv[1] == "d":
		decrypt = "".join([crypt(char, False) for char in text])
		print(decrypt)