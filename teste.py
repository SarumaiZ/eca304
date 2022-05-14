import os
os.system('cls')

ver=False
sender=","
carac = ""
numeros=[""]
i=0
cont=0
texto="236,05+36,09-6"
for dig in texto:
    if(dig in ["+", "-", "X", "/", "raiz"]):
        numeros.append("")
    numeros[i]=numeros[i]+dig
    if(dig in ["+", "-", "X", "/", "raiz"]):
        numeros[i]=numeros[i][:len(numeros[i])-1]
        i+=1
for alg in numeros[i]:
    if(alg == ','):
        ver=True
if(ver):
    carac=""
else:
    carac=sender
print(numeros)
print(texto+carac)