import os
import time
import matplotlib.pyplot as plt
import numpy as np
from math import *

os.system('cls')
opw = "s"

while(opw.lower() == "s"):
    fig, ax = plt.subplots()
    listaX = [0]
    listaY = [0]
    os.system('cls')
    a = float(input("Digite o tamanho da barra a [mm]: "))
    b = float(input("Digite o tamanho da barra b [mm]: "))
    c = float(input("Digite o tamanho da barra c [mm]: "))
    d = float(input("Digite o tamanho da barra d [mm]: "))
    op = float(input("\n1 - Inserir o valor de theta_2\n2 - Calcular para todos valores de theta_2\nDigite sua opção: "))
    if(op==1):
        theta_2 = float(input("\nDigite o valor de theta_2: "))
        K1 = d/a
        K2 = d/c
        K3 = (pow(a, 2)-pow(b,2)+pow(c, 2)+pow(d, 2))/(2*a*c)
        A = cos(radians(theta_2))-K1-K2*cos(radians(theta_2))+K3
        B = -2*sin(radians(theta_2))
        C = K1 - (K2+1)*cos(radians(theta_2))+K3
        theta_4_1 = 2*degrees(atan((-B+sqrt(pow(B, 2)-4*A*C))/(2*A))) #
        theta_4_2 = 2*degrees(atan((-B-sqrt(pow(B, 2)-4*A*C))/(2*A)))
        theta_3_1 = degrees(acos((-a*cos(radians(theta_2))+c*cos(radians(theta_4_1))+d)/(b)))
        theta_3_2 = degrees(acos((-a*cos(radians(theta_2))+c*cos(radians(theta_4_2))+d)/(b)))
        theta_3_1_sen = degrees(asin((-a*sin(radians(theta_2))+c*sin(radians(theta_4_1)))/(b)))
        theta_3_2_sen = degrees(asin((-a*sin(radians(theta_2))+c*sin(radians(theta_4_2)))/(b)))
        print("Theta 4_1: %f" %theta_4_1)
        print("Theta 4_2: %f" %theta_4_2)
        print("Theta 3_1 (calculado pelo cosseno): %f" %theta_3_1)
        print("Theta 3_2 (calculado pelo cosseno): %f" %theta_3_2)
        print("Theta 3_1 (calculado pelo seno): %f" %theta_3_1_sen)
        print("Theta 3_2 (calculado pelo seno): %f" %theta_3_2_sen)
        PosX = a*cos(radians(theta_2))+b*(cos(radians(theta_3_2)))
        PosY = a*sin(radians(theta_2))+b*(sin(radians(theta_3_2)))
        listaX.append(PosX)
        listaY.append(PosY)
        listaX.append(a*cos(radians(theta_2)))
        listaY.append(a*sin(radians(theta_2)))
        listaX.append(d)
        listaY.append(0)
        ax.plot(np.array([0, a*cos(radians(theta_2))]), np.array([0, a*sin(radians(theta_2))]), label='Barra a', color='red')
        ax.plot(np.array([a*cos(radians(theta_2)), a*cos(radians(theta_2)) + b*cos(radians(theta_3_2))]), np.array([a*sin(radians(theta_2)), a*sin(radians(theta_2)) + b*sin(radians(theta_3_2))]), label='Barra b', color='green')
        ax.plot(np.array([d, d+c*cos(radians(theta_4_2))]), np.array([0, c*sin(radians(theta_4_2))]), label='Barra c', color='c')
        ax.plot(np.array([0, d]), np.array([0,0]), label='Barra d', color='yellow')
        ax.scatter(np.array(listaX), np.array(listaY), label='Ponto', color='blue')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title("Posição do ponto")
        ax.legend()
        plt.show()
        plt.cla()
        plt.close()
    elif(op==2):
        K1 = d/a
        K2 = d/c
        K3 = (pow(a, 2)-pow(b,2)+pow(c, 2)+pow(d, 2))/(2*a*c)
        print("Theta 2 \t Theta 3_1 (cos) \t Theta 3_1 (sen) \t Theta 4_1 \t Theta 3_2 (cos) \t Theta 3_2 (sen) \t Theta 4_2")
        for theta_2 in range(0, 361):
            A = cos(radians(theta_2))-K1-K2*cos(radians(theta_2))+K3
            B = -2*sin(radians(theta_2))
            C = K1 - (K2+1)*cos(radians(theta_2))+K3
            theta_4_1 = 2*degrees(atan((-B+sqrt(pow(B, 2)-4*A*C))/(2*A)))
            theta_4_2 = 2*degrees(atan((-B-sqrt(pow(B, 2)-4*A*C))/(2*A)))
            theta_3_1 = degrees(acos((-a*cos(radians(theta_2))+c*cos(radians(theta_4_1))+d)/(b)))
            theta_3_2 = degrees(acos((-a*cos(radians(theta_2))+c*cos(radians(theta_4_2))+d)/(b)))
            theta_3_1_sen = degrees(asin((-a*sin(radians(theta_2))+c*sin(radians(theta_4_1)))/(b)))
            theta_3_2_sen = degrees(asin((-a*sin(radians(theta_2))+c*sin(radians(theta_4_2)))/(b)))
            print("%6i \t %20.2f \t %20.2f \t %15.2f \t %10.2f \t %20.2f \t %15.2f" %(theta_2, theta_3_1, theta_3_1_sen, theta_4_1, theta_3_2, theta_3_2_sen, theta_4_2))
            PosX = a*cos(radians(theta_2))+b*(cos(radians(theta_3_2)))
            PosY = a*sin(radians(theta_2))+b*(sin(radians(theta_3_2)))
            listaX.append(PosX)
            listaY.append(PosY)
        ax.scatter(np.array(listaX), np.array(listaY), label='Movimento final')
        plt.show()
        plt.cla()
        plt.close()
    else:
        op = int(input("Digite um número válido!: "))
    opw = input("Deseja fazer outro cálculo?(S/N): ")