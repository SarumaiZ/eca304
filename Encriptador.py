from string import *
from random import *
import os

def randomcript():
    d={}
    s=ascii_lowercase
    c=""
    for x in punctuation+whitespace+digits:
        d[x]=x
    for i in ascii_uppercase:
        c=choice(s)
        if c in d.values():
            while c in d.values():
                c=choice(s)
        if c.upper()==i:
            while c.upper()==i:
                c=choice(s)
        d[i]=c
    return d

def encripta(f, d):
    fn=""
    for i in f:
        fn+=d[i]
    return fn

def decripta(f, d):
    fn=""
    for i in f:
        fn+=d[i]
    return fn

def inverteDic(d):
    d2={}
    for chave in d:
        d2[d[chave]]=chave
    return d2

def criaDic():
    letras={}
    for x in punctuation+whitespace+digits:
        letras[x]=x
    for i in ascii_uppercase:
        letras[i]=i
    for j in ascii_uppercase:
        nova=input(f"Encriptação para {letras[j]}: ").lower()
        if len(nova)>1:
            while len(nova)>1:
                nova=input(f"Por favr, digite apenas uma letra para encriptar {letras[j]}: ").lower()
        elif nova in letras.values():
            while nova in letras.values():
                nova=input(f"Voce ja usou essa letra. Por favor digite outra letra para encriptar {letras[j]}: ").lower()
        letras[j]=nova
    return letras

conversor = {'!': '!', '"': '"', '#': '#', '$': '$', '%': '%', '&': '&', "'": "'", '(': '(', ')': ')', '*': '*',
'+': '+', ',': ',', '-': '-', '.': '.', '/': '/', ':': ':', ';': ';', '<': '<', '=': '=', '>': '>', '?': '?',
'@': '@', '[': '[', '\\': '\\', ']': ']', '^': '^', '_': '_', '`': '`', '{': '{', '|': '|', '}': '}', '~': '~',
' ': ' ', '\t': '\t', '\n': '\n', '\r': '\r', '\x0b': '\x0b', '\x0c': '\x0c',
'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'A': 'r', 'B': 'f',
'C': 'p', 'D': 'b', 'E': 'l', 'F': 'e', 'G': 'x', 'H': 'u', 'I': 'k', 'J': 'v', 'K': 'z', 'L': 'y', 'M': 'g', 'N': 'w',
'O': 'd', 'P': 'q', 'Q': 'h', 'R': 'c', 'S': 'o', 'T': 'm', 'U': 'j', 'V': 'n', 'W': 't', 'X': 'i', 'Y': 's', 'Z': 'a'}

os.system('cls')
dic={}
op="s"
while op=="s":
    print("O que voce deseja?\n\n1 - Criar os seus próprios caracteres de encriptação\n2 - Utilizar a codificação do prazer\n")
    opcrip=int(input("Digite a sua opção: "))
    if opcrip==1:
        os.system('cls')
        dic=criaDic()
        dicInverso={}
        dicInverso=inverteDic(dic)
        fraseOriginal=input("Digite a frase a ser encriptada: ")
        fraseOrigi=fraseOriginal.upper()
        fraseEncriptada=encripta(fraseOrigi, dic)
        fraseDecriptada=decripta(fraseEncriptada, dicInverso)
        print(fraseOriginal+"\t <- Esta é a frase original")
        print(fraseEncriptada+"\t <- Esta é a frase encriptada")
        print(fraseDecriptada+"\t <- Esta é a frase decriptada")
    elif opcrip==2:
        os.system('cls')
        conversorInverso={}
        conversorInverso=inverteDic(conversor)
        fraseOriginal=input("Digite a frase a ser encriptada: ")
        fraseOrigi=fraseOriginal.upper()
        fraseEncriptada=encripta(fraseOrigi, conversor)
        fraseDecriptada=decripta(fraseEncriptada, conversorInverso)
        print(fraseOriginal+"\t <- Esta é a frase original")
        print(fraseEncriptada+"\t <- Esta é a frase encriptada")
        print(fraseDecriptada+"\t <- Esta é a frase decriptada")
    else:
        print("Por favor digite uma opção válida")
    op=input("\nDeseja utilizar o encriptador novamente?(S/N): ").lower()