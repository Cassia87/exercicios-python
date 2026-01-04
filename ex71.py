# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada
# valor serão entregues. Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

import math
notas_cinquenta = 0
notas_vinte = 0
notas_dez = 0
notas_um = 0
resto = 0

while True:
    valor_saque = int(input('Qual o valor da saque: R$'))
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if valor_saque <= 0:
        print('Valor incorreto. Favor digitar um valor maior que zero.')
    elif valor_saque >= 50:
        notas_cinquenta = math.floor(valor_saque / 50)
        resto = valor_saque % 50
        notas_vinte = math.floor(resto / 20)
        resto = resto % 20
        notas_dez = math.floor(resto / 10)
        resto = resto % 10
        notas_um = math.floor(resto / 1)

    if (notas_cinquenta > 0):
        print(f'Notas de cinquenta: {notas_cinquenta}')
    if (notas_vinte > 0):
        print(f'Notas de vinte: {notas_vinte}')
    if (notas_dez > 0):
        print(f'Notas de dez: {notas_dez}')
    if (notas_um > 0):
        print(f'Notas de um: {notas_um}')

    if resp == 'N':
        break

print('Programa finalizado.')