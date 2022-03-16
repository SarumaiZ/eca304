import math
import cmath
import os
#calculadora
sn = 'S'

while (sn=='S'):

    op = int(input("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Raiz quadrada\nDigite a operação desejada: "))
    os.system('cls')

    if op==1:
        a = complex(input("Digite o primeiro valor: "))
        b = complex(input("Digite o segundo valor: "))
        if a.imag==0 and b.imag==0:
            r = a+b
            print("O resultado da soma é:",r.real)
        else:
            r = a+b
            print("O resultado da soma complexa é:",r)
    elif op==2:
        a = complex(input("Digite o primeiro valor: "))
        b = complex(input("Digite o segundo valor: "))
        if a.imag==0 and b.imag==0:
            r = a-b
            print("O resultado da subtração é:",r.real)
        else:
            r= a-b
            print("O resultado da subtração complexa é:",r)
    elif op==3:
        a = complex(input("Digite o primeiro valor: "))
        b = complex(input("Digite o segundo valor: "))
        if a.imag==0 and b.imag==0:
            r = a*b
            print("O resultado da multiplicação é:",r.real)
        else:
            r = a*b
            print("O resultado da multiplicação complexa é:",r)
    elif op==4:
        a = complex(input("Digite o primeiro valor: "))
        b = complex(input("Digite o segundo valor: "))
        if a.imag==0 and b.imag==0:
            r = a/b
            print("O resultado da divisão real é:",r.real)
        else:
            r = a/b
            print("O resultado da divisão complexa é:",r)
    elif op==5:
        a = float(input("Digite o valor: "))
        if  a>=0:
            r = math.sqrt(a)
            print("A raiz quadrada de {0:.2f} é: {1:.2f}" .format(a,r))
        else:
            r = cmath.sqrt(a)
            print(f"A raiz quadrada de {a} é: {r}")
    sn = input("\nDeseja fazer uma nova operação(S/N): ").upper()
    os.system('cls')