# Faça um programa onde o computador gere um número aleatório
# entre 1 e 5 e o usuário tenha que tentar acertar e mostre
# ao final em quantas tentativas ele acertou.

import random

num = random.randint(1,5)
tentativas = 1
palpite = int(input('Tente adivinhar o número secreto (entre 1 e 5): '))
while palpite != num:
    palpite = int(input('Você errou! Tente novamente: '))
    tentativas += 1
print(f'O núemro secreto é: {num}')
print(f'Parabéns você acertou o número secreto em {tentativas} tentativas.')