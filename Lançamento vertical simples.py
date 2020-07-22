from math import *

#Lançamento vertical simples

g = -9.8    #aceleração da gravidade
y = 10      #h initial
vy = 0      #velocidade em y, pois v em x é constante
dt = 2      #tempo de queda
while y >= 0:
    y = y + (vy * dt)       # S = So + Vt
    vy = vy + (g*dt)          # V = Vo + at
    print(y,vy)                    #posição e velocidade



