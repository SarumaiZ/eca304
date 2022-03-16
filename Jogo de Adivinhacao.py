import random
import os

op='s'
while(op=='s'):

    print("\n")
    print("* "+"-"*29+" *")
    print("|\tJogo de Adivinhação\t|")
    print("* "+"-"*29+" *\n")

    inicio = random.randrange(0, 401)
    fim = random.randrange(600, 1001)

    print(f"Descubra o número sorteado entre {inicio} e {fim}\n")

    lista = list(range(inicio, fim))
    rand = random.choice(lista)
    chute = -1
    i=0
    while(chute!=rand):
        chute = int(input("Digite o seu chute: "))
        if(chute>rand):
            print("Menor\n")
        elif(chute<rand):
            print("Maior\n")
        i+=1
    print(f"\nO número sorteado foi: {rand}\nO número digitado foi: {chute}")
    print(f"Tentativas: {i}\n")
    op=input("Deseja jogar novamente? (S/N): ").lower()
    os.system('cls')