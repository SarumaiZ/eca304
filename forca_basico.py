from random import choice
import os

def imprime(ponto, certas, erradas, palavra, categ):
    os.system('cls')
    print("*************** Forca ***************")
    if categ==1:
        print("\nCategoria: Animal\n")
    if categ==2:
        print("\nCategoria: Objeto\n")
    if categ==3:
        print("\nCategoria: Comida\n")
    if categ==4:
        print("\nCategoria: Lugar\n")
    if categ==5:
        print("\nCategoria: Especial")
    print("Palavra secreta: " + palavra + "\n")
    print("A palavra possui %i letras\n" %len(palavra))
    if(ponto == 0):
        print("=======[_] \n||      |  \n||         \n||         \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 1):
        print("=======[_] \n||      |  \n||     (_)  \n||         \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 2):
        print("=======[_] \n||      |  \n||     (_)  \n||      |  \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 3):
        print("=======[_] \n||      |  \n||     (_)  \n||     /|  \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 4):
        print("=======[_] \n||      |  \n||     (_)  \n||     /|\ \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 5):
        print("=======[_] \n||      |  \n||     (_)  \n||     /|\ \n||     /   \n||         \nHHHHHHHHHHHH")
    elif(ponto == 6):
        print("=======[_] \n||      |  \n||     (_)  \n||     /|\ \n||     / \ \n||         \nHHHHHHHHHHHH")

    print("\nLetras erradas:",erradas)
    print("Letras corretas:",certas)

def iniciaPalavra(tamanho):
    return '_'*tamanho

def sorteia(lista):
    return choice(lista)

op='S'
teste=0
while (op=='S'):
    os.system('cls')
    lista = []
    animal = ['cachorro', 'gato', 'galinha', 'cavalo', 'camelo', 'girafa', 'elefante','rato','arara','formiga','lagarto','tubarao']
    objeto = ['arame','camisa','cama', 'mesa', 'garfo', 'sapato','martelo','copo','sofa','ventilador','televisao']
    comida = ['lanche','manteiga','laranja', 'pera', 'melancia','arroz','feijao','macarrao','camarao','carne','sopa']
    lugar = ['fazenda','cidade','parque','shopping','teatro','museu', 'cinema','casa','escola','biblioteca']
    prazer = ['prazer', 'zezinho', 'wandinho','kiunku', 'samurai','murilovers']
    s=" Categorias ".center(20,'-')    
    print(s)
    print("\n1 - Animal\n2 - Objeto\n3 - Comida\n4 - Lugar\n5 - Especial\n")
    x = int(input("Digite qual categoria deseja jogar: "))
    if x==1:
        lista=animal
    if x==2:
        lista=objeto
    if x==3:
        lista=comida
    if x==4:
        lista=lugar
    if x==5:
        lista=prazer
    palavra = sorteia(lista)
    vazio = iniciaPalavra(len(palavra))
    certa = []
    errada = []
    ponto=0
    os.system('cls')
    while(ponto<6 and vazio != palavra):
        chute = input("Digite uma letra: ").lower()
        if (chute==palavra):
            print("\nacertou...\n")
            break
        else:
            if len(chute)==1:
                if(chute in palavra):
                    if(chute not in certa):
                        certa.append(chute)
                        for i in range(len(palavra)):
                            if palavra[i]==chute:
                                vazio = vazio[:i]+chute+vazio[i+1:]
                else:
                    if chute not in errada:
                        errada.append(chute)
                        ponto+=1
                imprime(ponto, certa, errada, vazio, x)
            elif (len(chute)<len(palavra)):
                print("\nPor favor, digite apenas uma letra\n")
            else:
                print("\nVocê chutou e errou, tente novamente.\n")
                break
    if ponto==6:
        print("\nVocê foi enforcado!")
        print("A palavra correta era "+palavra+"\n")
    if vazio==palavra:
        print("\nParabéns!!! Você acertou\n")
    op = input("Deseja jogar novamente?(S/N): ").upper()