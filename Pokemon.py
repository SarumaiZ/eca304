#Matheus Gonçalves Zaitune da Silva 19.01247-0
#Gabriel Semitan 19.00961-5

import os

class Pokemon:
    def __init__(self, nome, ID):
        self._nome = nome
        self._ID = ID
        self.HP = 0
        self.AT = 0
        self.DF = 0
        self.SP_AT = 0
        self.SP_DF = 0
        self.SP = 0
        self.golpes = []

    def atribuiHP(self, HP):
        while(HP>100 or HP<0):
            if(HP>100):
                print("\nValor maior que o limite, digite novamente")
                HP = int(input("Digite um valor para HP entre 0 e 100: "))
            if(HP<0):
                print("\nValor menor que o limite, digite novamente")
                HP = int(input("Digite um valor para HP entre 0 e 100: "))
        self.HP = HP

    def atribuiAT(self, AT):
        while(AT>150 or AT<0):
            if(AT>150):
                print("\nValor maior que o limite, digite novamente")
                AT = int(input("Digite um valor para AT entre 0 e 150: "))
            if(AT<0):
                print("\nValor menor que o limite, digite novamente")
                AT = int(input("Digite um valor para AT entre 0 e 150: "))
        self.AT = AT

    def atribuiDF(self, DF):
        while(DF>120 or DF<0):
            if(DF>120):
                print("\nValor maior que o limite, digite novamente")
                DF = int(input("Digite um valor para DF entre 0 e 120: "))
            if(DF<0):
                print("\nValor menor que o limite, digite novamente")
                DF = int(input("Digite um valor para DF entre 0 e 120: "))
        self.DF = DF

    def atribuiSP_AT(self, spat):
        while(spat>100 or spat<0):
            if(spat>100):
                print("\nValor maior que o limite, digite novamente")
                spat = int(input("Digite um valor para SP_AT entre 0 e 100: "))
            if(spat<0):
                print("\nValor menor que o limite, digite novamente")
                spat = int(input("Digite um valor para SP_AT entre 0 e 100: "))
        self.SP_AT = spat

    def atribuiSP_DF(self, spdf):
        while(spdf>100 or spdf<0):
            if(spdf>100):
                print("\nValor maior que o limite, digite novamente")
                spdf = int(input("Digite um valor para SP_DF entre 0 e 100: "))
            if(spdf<0):
                print("\nValor menor que o limite, digite novamente")
                spdf = int(input("Digite um valor para SP_DF entre 0 e 100: "))
        self.SP_DF = spdf

    def atribuiSP(self, SP):
        while(SP>150 or SP<0):
            if(SP>150):
                print("\nValor maior que o limite, digite novamente")
                SP = int(input("Digite um valor para SP entre 0 e 150: "))
            if(SP<0):
                print("\nValor menor que o limite, digite novamente")
                SP = int(input("Digite um valor para SP entre 0 e 150: "))
        self.SP = SP

    def aprendeGolpe(self, g):
        self.golpes.append(g)
    
    def info(self):
        #os.system('cls')
        print()
        print("-"*30)
        print("Nome: {0}\tID: {1}".format(self._nome, self._ID))
        print("HP    "+"{:3} ".format(self.HP)+"|"*((self.HP//10)+1))
        print("AT    "+"{:3} ".format(self.AT)+"|"*((self.AT//10)+1))
        print("DF    "+"{:3} ".format(self.DF)+"|"*((self.DF//10)+1))
        print("SP_AT "+"{:3} ".format(self.SP_AT)+"|"*((self.SP_AT//10)+1))
        print("SP_DF "+"{:3} ".format(self.SP_DF)+"|"*((self.SP_DF//10)+1))
        print("SP    "+"{:3} ".format(self.SP)+"|"*((self.SP//10)+1))
        print("Golpes: "+"{0}".format(self.golpes))
        print("-"*30)
        print()

os.system('cls')

nome = input("Digite o nome do novo Pokemon: ")
pk1=Pokemon(nome, 0)

hp = int(input("\nDigite a vida do Pokemon {0}: ".format(nome)))
pk1.atribuiHP(hp)

at = int(input("\nDigite o ataque do Pokemon {0}: ".format(nome)))
pk1.atribuiAT(at)

df = int(input("\nDigite a defesa do Pokemon {0}: ".format(nome)))
pk1.atribuiDF(df)

spat = int(input("\nDigite a velocidade de ataque do Pokemon {0}: ".format(nome)))
pk1.atribuiSP_AT(spat)

spdf = int(input("\nDigite a velocidade de defesa do Pokemon {0}: ".format(nome)))
pk1.atribuiSP_DF(spdf)

sp = int(input("\nDigite a velocidade do Pokemon {0}: ".format(nome)))
pk1.atribuiSP(sp)

gol = input("\nDigite o novo golpe do Pokemon {0}: ".format(nome))
pk1.aprendeGolpe(gol)

pk1.info()