# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
maioridade = 0
menoridade = 0

for i in range(1,6):
    ano_nascimento = int(input('Digite o ano do seu nascimento: '))
    idade = atual - ano_nascimento
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1

print(f'A quantidade de pessoas maiores de idade é: {maioridade}')
print(f'A quantidade de pessoas menores de idade é: {menoridade}')
