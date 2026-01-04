#bEscreva um programa que faça o computador
# "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual
#foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

import random

print(""" 
░░█ █▀█ █▀▀ █▀█   █▀▄ █▀█   █▄░█ █░█ █▀▄▀█ █▀▀ █▀█ █▀█   █▀ █▀▀ █▀▀ █▀█ █▀▀ ▀█▀ █▀█
█▄█ █▄█ █▄█ █▄█   █▄▀ █▄█   █░▀█ █▄█ █░▀░█ ██▄ █▀▄ █▄█   ▄█ ██▄ █▄▄ █▀▄ ██▄ ░█░ █▄█
""")
num = random.randint(0, 5)
chute = int(input(f'Tente descobrir o número secreto: '))
if chute == num:
    print(f'Você acertou!')
elif chute > num:
    print('O número secreto é menor')

