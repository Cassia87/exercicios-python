# Faça um programa que leia o peso de 4 pessoas
# e mostre qual o menor e o maior peso da lista.
maior_peso = 0
menor_peso = 0
for i in range(1,5):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso



print(f'O menor peso é: {menor_peso}Kg')
print(f'O maior peso é: {maior_peso}Kg')
