# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido
# quando o número solicitado for negativo.
cont = 0
while True:
    num = int(input('Digite um número inteiro para ver a tabuada ou um número negativo para sair: '))
    if num < 0:
        break

    print(f'A tabuada do {num}: ')
    for cont in range(1, 11):
        print(f'{num} x {cont} = {num * cont}')




