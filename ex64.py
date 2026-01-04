# Crie um programa que leia vários números inteiros pelo teclado
# até o usuário digitar 999. Ao final mostre a quantidade de
# números digitados e a soma desses números.

cont = 0
soma = 0
num = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
    cont += 1

print(f'A quantidade de números digitados foi {cont} e a soma dos números é {soma}')

