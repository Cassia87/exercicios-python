# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numeros = []
for c in range(0, 5):
    numeros.append(int(input(f'Digite um número para a posição {c +1}: ')))
print(numeros)
print(f'O maior número da lista é {max(numeros)} e está na posição {numeros.index(max(numeros))}')
print(f'O menor número da lista é {min(numeros)} e está na posição {numeros.index(min(numeros))}')