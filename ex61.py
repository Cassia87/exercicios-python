# Faça um programa que leia o primeiro termo e a razão de
# uma PA e mostre os 10 primeiros termos

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

contador = 0
termo = primeiro

while contador < 10:
    print(termo, end='-> ')
    termo += razao
    contador += 1


