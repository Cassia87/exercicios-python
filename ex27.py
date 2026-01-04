# Faça um programa que leia o nome completo
# de uma pessoa, mostrando em seguida o
# primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
nome_separado = nome.split()
print(f'Seu nome é: {nome_separado[0]} ')
print(f'Seu último sobrenome é: {nome_separado[-1]} ')

