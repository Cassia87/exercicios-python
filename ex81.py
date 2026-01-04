# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    res = str(input(('Deseja continuar? [S/N]: '))).strip().upper()[0]
    if res == 'N':
        break
print(f'Foram digitados {len(numeros)} números')
print(f'Lista reversa: {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print(f'O número 5 foi digitado {numeros.count(5)} vezes na lista')