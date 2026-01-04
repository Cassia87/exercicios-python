# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

num = int(input('Digite um número e vamos verificar se ele é primo: '))

if num <= 1:
    print(f'{num} não é um número primo')
else:
    divisores = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1

    if divisores == 2:
        print(f'{num} é um número primo')
    else:
        print(f'{num} não é um número primo')

