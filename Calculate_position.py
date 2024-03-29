import os
import matplotlib.pyplot as plt
import numpy as np
import time
from math import *

os.system('cls')

def calcParam(a, b, c, d, theta):
    L = []
    K1 = d/a
    K2 = d/c
    K3 = (pow(a, 2)-pow(b, 2)+pow(c, 2)+pow(d, 2))/(2*a*c)
    A = cos(radians(theta))-K1-K2*cos(radians(theta))+K3
    B = -2*sin(radians(theta))
    C = K1 - (K2+1)*cos(radians(theta))+K3
    theta_4_1 = 2*degrees(atan((-B+sqrt(pow(B, 2)-4*A*C))/(2*A)))
    theta_4_2 = 2*degrees(atan((-B-sqrt(pow(B, 2)-4*A*C))/(2*A)))
    theta_3_1 = degrees(acos((-a*cos(radians(theta))+c*cos(radians(theta_4_1))+d)/(b)))
    theta_3_2 = degrees(acos((-a*cos(radians(theta))+c*cos(radians(theta_4_2))+d)/(b)))
    theta_3_1_sen = degrees(asin((-a*sin(radians(theta))+c*sin(radians(theta_4_1)))/(b)))
    theta_3_2_sen = degrees(asin((-a*sin(radians(theta))+c*sin(radians(theta_4_2)))/(b)))
    L = L+[theta_4_1, theta_4_2, theta_3_1, theta_3_2, theta_3_1_sen, theta_3_2_sen]
    return L

def grafico():
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_aspect('equal', adjustable='box')
    ax.legend(bbox_to_anchor=(1.3, 0.5))
    ax.grid()
    plt.show()
    plt.cla()
    plt.close()

opw = "s"
opb = "n"

while(opw.lower() == "s"):
    listaX = []
    listaY = []
    listaX2 = []
    listaY2 = []
    listaX3 = []
    listaY3 = []
    param = []
    ver=0
    os.system('cls')
    if opb.lower() != 's':
        a = float(input("Digite o tamanho da barra a [mm]: "))
        #a = 50
        b = float(input("Digite o tamanho da barra b [mm]: "))
        #b = 180
        c = float(input("Digite o tamanho da barra c [mm]: "))
        #c = 180
        d = float(input("Digite o tamanho da barra d [mm]: "))
        #d = 140
        opg = input("Seu mecanismo possui braço para garra?(S/N): ").lower()
        if(opg=='s'):
            garra=input("Digite qual braço possui a garra (b ou c): ")
            garraComp = float(input("Digite o comprimento da junta até a garra [mm]: "))
            #garraComp = 180 #o que teve o melhor movimento final
            #distancia da junta ate a ponta da garra de 100mm para diminuir a altura e provavelmente diminuir o balanço
            #outra opção é diminuir 10%-20%
        else:
            garra='x'
            garraComp=0.0
        op = int(input("\n1 - Inserir o valor de theta_2\n2 - Calcular para todos valores de theta_2\nDigite sua opção: "))
    else:
        opg = input("Seu mecanismo possui braço para garra?(S/N): ").lower()
        if(opg=='s'):
            garra=input("Digite qual braço possui a garra (b ou c): ")
            garraComp = float(input("Digite o comprimento da junta até a garra [mm]: "))
            #garraComp = 180 #o que teve o melhor movimento final
        else:
            garra='x'
            garraComp=0.0
        op = int(input("\n1 - Inserir o valor de theta_2\n2 - Calcular para todos valores de theta_2\nDigite sua opção: "))
    if(op == 1):
        fig, ax = plt.subplots(figsize=(6, 4), layout='constrained')
        theta_2 = float(input("\nDigite o valor de theta_2: "))
        ax.set_title("Posição do ponto para theta_2=%iº" % theta_2)
        param = calcParam(a, b, c, d, theta_2)
        print("\nThehta 4_1: %.2f\nTheta 3_1 (calculado pelo cosseno): %.2f\nTheta 3_1 (calculado pelo seno): %.2f\n\nTheta 4_2: %.2f\nTheta 3_2 (calculado pelo cosseno): %.2f\nTheta 3_2 (calculado pelo seno): %.2f\n" % (param[0], param[2], param[4], param[1], param[3], param[5]))
        PosX = a*cos(radians(theta_2))+b*(cos(radians(param[3])))
        PosY = a*sin(radians(theta_2))+b*(sin(radians(param[3])))
        if(garra=='b'):
            garraX = PosX+garraComp*cos(radians(param[3]))
            garraY = PosY+garraComp*sin(radians(param[3]))
            ver=1
        elif(garra=='c'):
            garraX = PosX+garraComp*cos(radians(param[1]))
            garraY = PosY+garraComp*sin(radians(param[1]))
            ver=1
        else:
            garraX=PosX
            garraY=PosY
            ver=0
        if(ver==1):
            ax.text(garraX+garraX*0.4, PosY, "Coordenada x da garra: %.2f \nCoordenada y da garra: %.2f" %(garraX, garraY), bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})
        listaX = [garraX, PosX, a*cos(radians(theta_2)), d, 0]
        listaY = [garraY, PosY, a*sin(radians(theta_2)), 0, 0]
        ax.scatter(np.array(listaX), np.array(listaY), label='Juntas')
        ax.plot(np.array([PosX, garraX]), np.array([PosY, garraY]), label='Barra da garra', color='blue')
        ax.plot(np.array([0, a*cos(radians(theta_2))]), np.array([0,a*sin(radians(theta_2))]), label='Barra a', color='red')
        ax.plot(np.array([a*cos(radians(theta_2)), a*cos(radians(theta_2)) + b*cos(radians(param[3]))]), np.array([a*sin(radians(theta_2)), a*sin(radians(theta_2)) + b*sin(radians(param[3]))]), label='Barra b', color='green')
        ax.plot(np.array([d, d+c*cos(radians(param[1]))]), np.array([0,c*sin(radians(param[1]))]), label='Barra c', color='c')
        ax.plot(np.array([0, d]), np.array([0, 0]),label='Barra d', color='yellow')
        ax.text(PosX-PosX*0.5, PosY/2, "Coordenada x: %.2f \nCoordenada y: %.2f" %(PosX, PosY), bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})
        grafico()
        opw = input("Deseja fazer outro cálculo?(S/N): ")
        if opw == 's':
            opb = input("\nDeseja utilizar os mesmos dados de tamanho de barra?(S/N): ")
    elif(op == 2):
        fig, ax = plt.subplots(figsize=(6, 4), layout='constrained')
        ax.set_title("Análise do movimento")
        print("\n| Theta 2 | Theta 3_1 (cos) | Theta 3_1 (sen) | Theta 4_1 | Theta 3_2 (cos) | Theta 3_2 (sen) | Theta 4_2 | Posição X | Posição Y")
        for theta_2 in range(0, 361):
            param = calcParam(a, b, c, d, theta_2)
            PosX = a*cos(radians(theta_2))+b*(cos(radians(param[3])))
            PosY = a*sin(radians(theta_2))+b*(sin(radians(param[3])))
            print("| %5i   | %11.2f     | %11.2f     | %8.2f  | %11.2f     | %11.2f     | %8.2f  | %8.2f  | %8.2f " % (theta_2, param[2], param[4], param[0], param[3], param[5], param[1], PosX, PosY))
            listaX.append(PosX)
            listaY.append(PosY)
            listaX2.append(a*cos(radians(theta_2)))
            listaY2.append(a*sin(radians(theta_2)))
            if(garra=='b'):
                garraX = PosX+garraComp*cos(radians(param[3]))
                garraY = PosY+garraComp*sin(radians(param[3]))
                ver=1
                listaX3.append(garraX)
                listaY3.append(garraY)
            elif(garra=='c'):
                garraX = PosX+garraComp*cos(radians(param[1]))
                garraY = PosY+garraComp*sin(radians(param[1]))
                ver=1
                listaX3.append(garraX)
                listaY3.append(garraY)
            else:
                garraX=PosX
                garraY=PosY
                ver=0
            if theta_2 % 5 == 0:
                if(ver==0):
                    ax.set(xlim=(-a-a*0.5-c/4, d+d*0.2+c/4),ylim=(-a-a*0.2, a+b+(a+b)*0.2))
                    ax.set_aspect('equal', adjustable='box')
                    ax.plot(np.array([0, a*cos(radians(theta_2))]),np.array([0, a*sin(radians(theta_2))]), color='red')
                    ax.plot(np.array([a*cos(radians(theta_2)), a*cos(radians(theta_2)) + b*cos(radians(param[3]))]), np.array([a*sin(radians(theta_2)), a*sin(radians(theta_2)) + b*sin(radians(param[3]))]), color='green')
                    ax.plot(np.array([d, d+c*cos(radians(param[1]))]),np.array([0, c*sin(radians(param[1]))]), color='c')
                    ax.plot(np.array([0, d]), np.array([0, 0]), color='y')
                    time.sleep(0.001)
                    plt.pause(0.0001)
                    ax.cla()
                if(ver==1):
                    ax.set(xlim=(-a-a*0.5-c/3-garraComp, d+garraComp),ylim=(-a-a*0.1, c+garraComp+garraComp*0.3))
                    ax.set_aspect('equal', adjustable='box')
                    ax.plot(np.array([PosX, garraX]), np.array([PosY, garraY]), color='blue')
                    ax.plot(np.array([0, a*cos(radians(theta_2))]),np.array([0, a*sin(radians(theta_2))]), color='red')
                    ax.plot(np.array([a*cos(radians(theta_2)), a*cos(radians(theta_2)) + b*cos(radians(param[3]))]), np.array([a*sin(radians(theta_2)), a*sin(radians(theta_2)) + b*sin(radians(param[3]))]), color='green')
                    ax.plot(np.array([d, d+c*cos(radians(param[1]))]),np.array([0, c*sin(radians(param[1]))]), color='c')
                    ax.plot(np.array([0, d]), np.array([0, 0]), color='y')
                    time.sleep(0.001)
                    plt.pause(0.0001)
                    ax.cla()
        maxX = max(listaX)
        minX = min(listaX)
        maxY = max(listaY)
        minY = min(listaY)
        ax.plot(np.array(listaX), np.array(listaY), label='Movimento final')
        listaX = [0, d, maxX, minX]
        listaY = [0, 0, maxY, minY]
        print("\n Máximo em X: %.2f \t Mínimo em X: %.2f \n Máximo em Y: %.2f \t Mínimo em Y: %.2f \n" % (maxX, minX, maxY, minY))
        ax.text(-d-d*0.1, (maxY+minY)/2, "Variação máxima em x: %.2f mm\nVariação máxima em y: %.2f mm" %(maxX-minX, maxY-minY), bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})
        if(minX<=0):
            ax.plot(np.array([0, minX, a/(sqrt(1+(pow(minY/minX, 2))))]), np.array([0, minY, (minY*a)/(minX*(sqrt(1+(pow(minY/minX, 2)))))]), label='Barras a+b (min)', color='m')
            listaX.append(a /(sqrt(1+(pow(minY/minX, 2)))))
            listaY.append((minY*a)/(minX*(sqrt(1+(pow(minY/minX, 2))))))
        else:
            ax.plot(np.array([0, minX, -a/(sqrt(1+(pow(minY/minX, 2))))]), np.array([0, minY, -(minY*a)/(minX*(sqrt(1+(pow(minY/minX, 2)))))]), label='Barras a+b (min)', color='m')
            listaX.append(-a/(sqrt(1+(pow(minY/minX, 2)))))
            listaY.append(-(minY*a)/(minX*(sqrt(1+(pow(minY/minX, 2))))))
        if(maxX<=0):
            listaX.append(-a/(sqrt(1+(pow(maxY/maxX, 2)))))
            listaY.append(-(maxY*a)/(maxX*(sqrt(1+(pow(maxY/maxX, 2))))))
        else:
            listaX.append(a/(sqrt(1+(pow(maxY/maxX, 2)))))
            listaY.append((maxY*a)/(maxX*(sqrt(1+(pow(maxY/maxX, 2))))))
        if(garra=='b'):
            maxgx=max(listaX3)
            maxgy=max(listaY3)
            mingx=min(listaX3)
            mingy=min(listaY3)
            if(maxX<=0):
                ax.plot(np.array([maxX, -(a+b+garraComp)/(sqrt(1+pow(maxY/maxX, 2)))]), np.array([maxY, -((a+b+garraComp)*maxY)/(maxX*(sqrt(1+pow(maxY/maxX, 2))))]), label='Barra da garra máximo', color='g')
                listaX.append(-(a+b+garraComp)/(sqrt(1+pow(maxY/maxX, 2))))
                listaY.append(-((a+b+garraComp)*maxY)/(maxX*(sqrt(1+pow(maxY/maxX, 2)))))
            else:
                ax.plot(np.array([maxX, (a+b+garraComp)/(sqrt(1+pow(maxY/maxX, 2)))]), np.array([maxY, ((a+b+garraComp)*maxY)/(maxX*(sqrt(1+pow(maxY/maxX, 2))))]), label='Barra da garra máximo', color='g')
                listaX.append((a+b+garraComp)/(sqrt(1+pow(maxY/maxX, 2))))
                listaY.append(((a+b+garraComp)*maxY)/(maxX*(sqrt(1+pow(maxY/maxX, 2)))))
            if(minX<=0):
                ax.plot(np.array([minX, -(-a+b+garraComp)/(sqrt(1+pow(minY/minX, 2)))]), np.array([minY, -((-a+b+garraComp)*minY)/(minX*(sqrt(1+pow(minY/minX, 2))))]), label='Barra da garra mínimo', color='m')
                listaX.append(-(-a+b+garraComp)/(sqrt(1+pow(minY/minX, 2))))
                listaY.append(-((-a+b+garraComp)*minY)/(minX*(sqrt(1+pow(minY/minX, 2)))))
            else:
                ax.plot(np.array([minX, (-a+b+garraComp)/(sqrt(1+pow(minY/minX, 2)))]), np.array([minY, ((-a+b+garraComp)*minY)/(minX*(sqrt(1+pow(minY/minX, 2))))]), label='Barra da garra mínimo', color='m')
                listaX.append((-a+b+garraComp)/(sqrt(1+pow(minY/minX, 2))))
                listaY.append(((-a+b+garraComp)*minY)/(minX*(sqrt(1+pow(minY/minX, 2)))))
        if(garra=='c'):
            maxgx=max(listaX3)
            maxgy=max(listaY3)
            mingx=min(listaX3)
            mingy=min(listaY3)
            ax.plot(np.array([maxX, maxgx]), np.array([maxY, maxgy]), label='Barra da garra máximo', color='c')
            ax.plot(np.array([minX, mingx]), np.array([minY, mingy]), label='Barra da garra mínimo', color='k')
            listaX = listaX+[maxgx, mingx]
            listaY = listaY+[maxgy, mingy]
        ax.plot(np.array([maxX, 0]), np.array([maxY, 0]),label='Barras a+b (max)', color='g')
        ax.plot(np.array([d, maxX]), np.array([0, maxY]),label='Barra c (max)', color='c')
        ax.plot(np.array([d, minX]), np.array([0, minY]),label='Barra c (min)', color='k')
        ax.plot(np.array(listaX2), np.array(listaY2),label='Movimento barra a', color='red')
        if(ver==1):
            ax.plot(np.array(listaX3), np.array(listaY3),label='Movimento da garra', color='blue')
            ax.text(d+d*0.2, (maxgx+mingy)/2, "Variação máxima da garra em x: %.2f mm\nVariação máxima da garra em y: %.2f mm" %(maxgx-mingx, maxgy-mingy), bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})
        ax.plot(np.array([0, d]), np.array([0, 0]),label='Barra d', color='yellow')
        ax.scatter(np.array(listaX), np.array(listaY), label='Juntas')
        grafico()
        opw = input("Deseja fazer outro cálculo?(S/N): ")
        if opw == 's':
            opb = input("\nDeseja utilizar os mesmos dados de tamanho de barra?(S/N): ")
    else:
        print("\nDigite um número válido!\n")
        time.sleep(2)