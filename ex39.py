# Faça um programa que leia o ano de nascimento de uma
# pessoa e mostre se ela está ou não na idade de se alistar.

ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = 2025 - ano_nascimento
if idade > 18:
    print(f'Você deveria ter se alistado há {idade - 18} anos')
elif idade < 18:
    print(f'Faltam {18 - idade} anos para o alistamento')
else:
    print('Você tem 18 anos e está na idade de se alistar')