# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente. Ao final, mostre
# o conteúdo das três listas geradas.
numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    res = str(input(('Deseja continuar? [S/N]: '))).strip().upper()[0]
    if res == 'N':
        break
    pares = list(num for num in numeros if num % 2 == 0)
    impares = list(num for num in numeros if num % 2 != 0)

print(f'Lista de números: {numeros}')
print(f'Lista de pares: {pares}')
print(f'Lista de impares: {impares}')