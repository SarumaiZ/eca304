from string import *
import os

"""
letras={}

for i in ascii_uppercase:
    letras[i]=i

for j in ascii_uppercase:
    nova=input(f"Para a letra {letras[j]}, digite a letra que deseja trocar: ").lower()
    if nova in letras.values():
        while nova in d.values():
            nova=input(f"Para a letra {letras[j]}, digite a letra que deseja trocar: ").lower()
    letras[j]=nova
print(letras)"""

conversor = {'8': '8', 'C': 'e', 'Y': 'n', 'U': 'x', 'G': 'u', 'Q': 'j', '^': '^', "'": "'", '~':
'~', 'Z': 'm', '/': '/', 'R': 'k', '+': '+', 'E': 't', 'D': 'r', '|': '|', 'K': 'a', '1': '1',
'?': '?', 'O': 'g', '\x0b': '\x0b', 'I': 'o', '4': '4', '(': '(', 'A': 'q', '.': '.', '{': '{',
'!': '!', '\r': '\r', ']': ']', '0': '0', '-': '-', 'B': 'w', '}': '}', '$': '$', 'S': 'l', 'W':
'v', 'V': 'c', 'F': 'y', '7': '7', ';': ';', ' ': ' ', '*': '*', ')': ')', '%': '%', '#': '#',
'9': '9', '@': '@', '6': '6', '>': '>', '\\': '\\', '=': '=', '\x0c': '\x0c', 'H': 'i', 'M': 'd',
'J': 'p', ',': ',', '<': '<', 'L': 's', '5': '5', 'P': 'h', 'X': 'b', '\t': '\t', '&': '&', '`':
'`', ':': ':', 'N': 'f', '\n': '\n', '_': '_', '3': '3', '[': '[', '2': '2', 'T': 'z', '"': '"'}
os.system('cls')
#frase = "Pastel de escarola com queijo, eu estou com vontade, diga-se de passagem. Soube que meu amigo aqui do lado esta vendendo".upper()
frase = input("Digite a frase: ").upper()
novaFrase=""
fraseRenovada=""
for i in frase:
    novaFrase+=conversor[i]
print(f"\nEsta é a frase encriptada: {novaFrase}\n")

for i in novaFrase:
    for j in conversor:
        if conversor[j]==i:
            fraseRenovada+=j
print(f"Esta é a frase decriptada: {fraseRenovada}\n")