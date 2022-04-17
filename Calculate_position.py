import os
import matplotlib.pyplot as plt
import numpy as np
from math import *

os.system('cls')
opw = "s"
opb = "n"

while(opw.lower() == "s"):
    fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
    listaX = []
    listaY = []
    listaX2 = []
    listaY2 = []
    os.system('cls')
    if opb.lower() != 's':
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
        listaX = listaX + [PosX, a*cos(radians(theta_2)), d, 0]
        listaY = listaY + [PosY, a*sin(radians(theta_2)), 0, 0]
        ax.plot(np.array([0, a*cos(radians(theta_2))]), np.array([0, a*sin(radians(theta_2))]), label='Barra a', color='red')
        ax.plot(np.array([a*cos(radians(theta_2)), a*cos(radians(theta_2)) + b*cos(radians(theta_3_2))]), np.array([a*sin(radians(theta_2)), a*sin(radians(theta_2)) + b*sin(radians(theta_3_2))]), label='Barra b', color='green')
        ax.plot(np.array([d, d+c*cos(radians(theta_4_2))]), np.array([0, c*sin(radians(theta_4_2))]), label='Barra c', color='c')
        ax.plot(np.array([0, d]), np.array([0,0]), label='Barra d', color='yellow')
        ax.scatter(np.array(listaX), np.array(listaY), label='Juntas')
        ax.text(PosX-PosX*0.5, PosY/2, "Coordenada x: %.2f \nCoordenada y: %.2f" %(PosX, PosY), bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title("Posição do ponto para theta_2=%iº"%theta_2)
        ax.legend()
        ax.set_aspect('equal', adjustable='box')
        ax.grid()
        plt.show()
        plt.cla()
        plt.close()
    elif(op==2):
        K1 = d/a
        K2 = d/c
        K3 = (pow(a, 2)-pow(b,2)+pow(c, 2)+pow(d, 2))/(2*a*c)
        print("Theta 2 \t Theta 3_1 (cos) \t Theta 3_1 (sen) \t Theta 4_1 \t Theta 3_2 (cos) \t Theta 3_2 (sen) \t Theta 4_2 \t Posição X \t Posição Y")
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
            PosX = a*cos(radians(theta_2))+b*(cos(radians(theta_3_2)))
            PosY = a*sin(radians(theta_2))+b*(sin(radians(theta_3_2)))
            print("%6i \t %20.2f \t %20.2f \t %15.2f \t %10.2f \t %20.2f \t %15.2f \t %8.2f \t %8.2f" %(theta_2, theta_3_1, theta_3_1_sen, theta_4_1, theta_3_2, theta_3_2_sen, theta_4_2, PosX, PosY))
            listaX.append(PosX)
            listaY.append(PosY)
            listaX2.append(a*cos(radians(theta_2)))
            listaY2.append(a*sin(radians(theta_2)))
            #if theta_2%90==0:
                #ax.plot(np.array([0, a*cos(radians(theta_2))]), np.array([0, a*sin(radians(theta_2))]), color='red')
                #ax.plot(np.array([a*cos(radians(theta_2)), a*cos(radians(theta_2)) + b*cos(radians(theta_3_2))]), np.array([a*sin(radians(theta_2)), a*sin(radians(theta_2)) + b*sin(radians(theta_3_2))]), color='green')
        maxX=max(listaX)
        minX=min(listaX)
        maxY=max(listaY)
        minY=min(listaY)
        print("\n Máximo em X: %.2f \t Mínimo em X: %.2f \n Máximo em Y: %.2f \t Mínimo em Y: %.2f \n" %(maxX, minX, maxY, minY))
        ax.text(-d-d*0.3, (maxY+minY)/2 , "Variação máxima em x: %.2f mm\nVariação máxima em y: %.2f mm" %(maxX-minX, maxY-minY), bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})
        ax.set_title("Análise do movimento")
        ax.plot(np.array([0, minX, a/(sqrt(1+(pow(minY/minX, 2))))]), np.array([0, minY, (minY*a)/(minX*(sqrt(1+(pow(minY/minX, 2)))))]), label='Barras a+b (min)', color='m')
        ax.plot(np.array([maxX, 0]), np.array([maxY, 0]), label='Barras a+b (max)', color='g')
        ax.plot(np.array([d, maxX]), np.array([0, maxY]), label='Barra c (max)', color='c')
        ax.plot(np.array([d, minX]), np.array([0, minY]), label='Barra c (min)', color='k')
        ax.plot(np.array(listaX), np.array(listaY), label='Movimento final')
        listaX = [0,d, maxX, minX, a/(sqrt(1+(pow(minY/minX, 2)))), a/(sqrt(1+(pow(maxY/maxX, 2)))) ]
        listaY = [0,0, maxY, minY, (minY*a)/(minX*(sqrt(1+(pow(minY/minX, 2))))), (maxY*a)/(maxX*(sqrt(1+(pow(maxY/maxX, 2))))) ]
        ax.plot(np.array(listaX2), np.array(listaY2), label='Movimento barra a', color='red')
        ax.plot(np.array([0, d]), np.array([0,0]), label='Barra d', color='yellow')
        ax.scatter(np.array(listaX), np.array(listaY), label='Juntas')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_aspect('equal', adjustable='box')
        ax.legend(bbox_to_anchor=(1.2, 0.5))
        ax.grid()
        plt.show()
        plt.cla()
        plt.close()
    else:
        print("\nDigite um número válido!\n")
    opw = input("Deseja fazer outro cálculo?(S/N): ")
    if opw=='s':
        opb = input("Deseja utilizar os mesmos dados de tamanho de barra?(S/N): ")