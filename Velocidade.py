import os
from math import *
import time
os.system('cls')

opw='s'

while(opw=='s'):
    os.system('cls')
    op = int(input("1 - Calcular velocidade para biela-manivela\n2 - Calcular velocidade para 4 barras\nDigite sua opção: "))
    if(op==1):
        os.system('cls')
        eloa=float(input("Digite o tamanho da barra a [mm]: "))
        elob=float(input("Digite o tamanho da barra b [mm]: "))
        t2=float(input("Digite o valor de theta_2 [graus]: "))
        w2=float(input("Digite o valor de w_2 [rpm]: "))
        vb=w2*2*pi*eloa/60000
        phi=degrees(asin(sin(radians(t2))*eloa/elob))
        beta=180-(90-phi)-(90-t2)
        vc=sin(radians(beta))*vb/sin(radians(90-phi))
        print("\nVb: %.2f m/s"%vb)
        print("Vc: %.2f m/s\n" %vc)
        #print("Beta: %.2f\nPhi: %.2f"%(beta, phi))
        opw=input("Deseja realizar outro cálculo?(S/N): ")
    elif(op==2):
        opw=input("Deseja realizar outro cálculo?(S/N): ")
    else:
        print("\nDigite um número válido!\n")
        time.sleep(2)