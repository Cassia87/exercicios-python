# Escreva um programa que eia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão:')
print("""
[1] Converter para binário
[2] Converter para octal
[3] Converter para hexadecimal
""")
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print(f'O numero {num} em binário é: {bin(num)[2:]}')
elif escolha == 2:
    print(f'O numero {num} em octal é: {oct(num)[2:]}')
elif escolha == 3:
    print(f'O numero {num} em hexadecimal é: {hex(num)[2:]}')
else:
    print('Escolha invalida')

