import os
from math import *
os.system('cls')

op='s'

while(op=='s'):
    os.system('cls')
    eloa=float(input("Digite elo A: "))
    elob=float(input("Digite elo B: "))
    t2=float(input("Digite theta_2: "))
    t2r=radians(t2)
    w2=float(input("Digite w_2: "))
    vb=w2*2*pi*eloa/60000
    phi=degrees(asin(sin(t2r)*eloa/elob))
    beta=180-(90-phi)-(90-t2)
    vc=sin(radians(beta))*vb/sin(radians(90-phi))
    print("Vb: %.2f"%vb)
    print("Vc: %.2f m/s" %vc)
    #print("Beta: %.2f\nPhi: %.2f"%(beta, phi))
    op=input("Denovo? ")