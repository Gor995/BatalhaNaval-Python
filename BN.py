#Projeto feito usando uma hora a cada semana, então não faço a minima ideia do que certas parte do codigo fazem

import time
import random

pontosP = 0
pontosB = 0
running = True
barcosX = []
barcosY = []

barcos2X = []
barcos2Y = []

jog1 = {
    1:[0,0,0,0,0],
    2:[0,0,0,0,0],
    3:[0,0,0,0,0],
    4:[0,0,0,0,0],
    5:[0,0,0,0,0]
}

jog2 = {
    1:[0,0,0,0,0],
    2:[0,0,0,0,0],
    3:[0,0,0,0,0],
    4:[0,0,0,0,0],
    5:[0,0,0,0,0]
}

mirou = [(0,0)]

def bot2():#ta funfando, n sei como
    for i in range(3):
        li2X = random.randint(1,5)
        co2Y = random.randint(1,5)
        TpA = [(li2X, co2Y)]
        TpANova = ()
        if barcos2X.__len__() > 0 and barcos2Y.__len__() > 0:
            TpANova = (li2X,co2Y)
            for i in range(TpA.__len__()):
                if TpA[i] == TpANova:
                    #print("Debug")
                    pass
            barcos2X.append(li2X)
            barcos2Y.append(co2Y)
        else:
            barcos2X.append(li2X)
            barcos2Y.append(co2Y)
            
        jog2[co2Y][li2X - 1] = 1#funfando

    #print('Colunas bot: ', barcos2X, 'Linhas bot: ', barcos2Y) #Debug

def jogar1():
    global jog1
    for i in range(3):
        print('Coordenada Coluna(Y) para seu barco numero: ', i+1, ' ira ficar: ')
        liX = int(input())
        barcosX.append(liX)
        
        print('Coordenada Linha(X) para seu barco numero: ', i+1, ' ira ficar: ')
        coY = int(input())
        barcosY.append(coY)

        print('Colunas: ', barcosX, 'Linhas: ', barcosY)
        jog1[coY][liX - 1] = 1

jogar1()
bot2()

#print('\n', jog2[1], '\n', jog2[2], '\n', jog2[3], '\n', jog2[4], '\n', jog2[5]) #Debug
print('\n', jog1[1], '\n', jog1[2], '\n', jog1[3], '\n', jog1[4], '\n', jog1[5])

#-----------------------------------logica da gameplay-----------------------------------

def jogando():
    global pontosP
    print('Coordenadas do disparo: ')
    repete = True

    while repete:
        inpx = int(input('Coluna(Y): '))
        inpy = int(input('Linha(X): '))

        if inpx == int or inpy == int: #por que == e não !=??????????????????
            print("Erro")
            repete = True
        else:
            repete = False
            
    if jog2[inpy][inpx-1] == 1:
        print("Player acertou um navio inimigo")
        pontosP+=1
        jog2[inpy][inpx-1] = 0
        
        print('\n', jog2[1], '\n', jog2[2], '\n', jog2[3], '\n', jog2[4], '\n', jog2[5]) #debug
    else:
        print('Player errou')

def roboJoga():
    mirou = set()
    global pontosB
    
    while True:
        li2XJ = random.randint(1, 5)
        co2YJ = random.randint(1, 5)
        coord = (li2XJ, co2YJ)

        if coord not in mirou:
            mirou.add(coord)
            break

    if jog1[co2YJ][li2XJ - 1] == 1:
        print("Bot acertou um de seus navios")
        pontosB +=1
        
        jog1[co2YJ][li2XJ - 1] = 0
    else:
        print("Bot errou")


#-----------------------------------jogo rodando-----------------------------------
while running:
    time.sleep(0.5)
    jogando()
    roboJoga()
    if pontosP >= 3:
        print("Player ganhou")
        break
    elif pontosB >= 3:
        print("Player perdeu")
        break
    
    print('\n', jog1[1], '\n', jog1[2], '\n', jog1[3], '\n', jog1[4], '\n', jog1[5])

