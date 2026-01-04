# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
maior = menor = 0

while True:
    pessoas.append(input('Nome: '))
    pessoas.append(float(input('Peso: ')))

    if len(dados) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    dados.append(pessoas[:])
    pessoas.clear()

    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break

print(f'Você cadastrou {len(dados)} pessoas.')

print(f'O maior peso é {maior}. Peso de: ', end='')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()

print(f'O menor peso é {menor}. Peso de: ', end='')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()

print(dados)
