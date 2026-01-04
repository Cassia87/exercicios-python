# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# Ao final mostre:
# A) Quantas vezes apareceu o 9
# B) Em que posição foi digitado o primeiro 3
# C) Quais foram os números pares

tupla = (int(input('Digite um número: '))), (int(input('Digite um número: '))), (int(input('Digite um número: '))), (int(input('Digite um número: ')))
print(f'Você digitou os números: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 apareceu primeiro na posição {tupla.index(3)}')
else:
    print('O valor 3 não foi encontrado')

pares = tuple(num for num in tupla if num % 2 == 0)
print(f'Os números pares digitados foram: {pares}')