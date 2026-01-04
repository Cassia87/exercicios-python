# Faça um programa que leia 6 números e faça a soma
# dos números pares.

soma = 0
for i in range(1, 7):
    num = int(input('Digite um número '))
    if num % 2 == 0:
        soma += num

print(f'A soma dos números pares é: {soma}')