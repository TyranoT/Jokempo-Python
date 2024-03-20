import random
from time import sleep
jokempo = random.choice(['pedra','papel','tesoura'])
player = str(input('Escolha entre Pedra, Papel e Tesoura: ')).lower()

if player == jokempo:
    print('Processando...')
    sleep(1)
    print('PC: {}'.format(jokempo))
    print('->'*5+'EMPATE!'+'<-'*5)
elif player == 'pedra' and jokempo == 'papel':
    print('Processando...')
    sleep(1)
    print('PC: {}'.format(jokempo))
    print('->'*5+'JOGADOR PERDEU!'+'<-'*5)
elif player == 'pedra' and jokempo == 'tesoura':
    print('Processando...')
    sleep(1)
    print('PC: {}'.format(jokempo))
    print('->'*5+'JOGADOR VENCEU!'+'<-'*5)
elif player == 'papel' and jokempo == 'tesoura':
    print('Processando...')
    sleep(1)
    print('PC: {}'.format(jokempo))
    print('->'*5+'JOGADOR PERDEU!'+'<-'*5)
elif player == 'papel' and jokempo == 'pedra':
    print('Processando...')
    sleep(1)
    print('PC: {}'.format(jokempo))
    print('->'*5+'JOGADOR VENCEU!'+'<-'*5)
elif player == 'tesoura' and jokempo == 'pedra':
    print('Processando...')
    sleep(1)
    print('PC: {}'.format(jokempo))
    print('->'*5+'JOGADOR PERDEU!'+'<-'*5)
elif player == 'tesoura' and jokempo == 'papel':
    print('Processando...')
    sleep(1)
    print('PC: {}'.format(jokempo))
    print('->'*5+'JOGADOR VENCEU!'+'<-'*5)
else:
    print('Erro!')