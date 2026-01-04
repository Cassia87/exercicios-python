# Faça um programa que solicite um número e
# mostre a tabuada desse número.

num = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')