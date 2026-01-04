# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = 0
produtos_mais_cem_reais = 0
nome_produto_mais_caro = ''
valor_produto_mais_caro = 0

while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço do produto: '))
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    total += preco

    if preco > valor_produto_mais_caro:
        valor_produto_mais_caro = preco
        nome_produto_mais_caro = nome

    if preco > 100:
        produtos_mais_cem_reais += 1

    if resp == 'N':
        break

print(f'O valor da compra foi de R$ {total:.2f}')
print(f'Foram cadastrados {produtos_mais_cem_reais} produto(s) que custam mais que R$100.')
print(f'O produto mais caro é {nome_produto_mais_caro} e custa R$ {valor_produto_mais_caro:.2f}')

