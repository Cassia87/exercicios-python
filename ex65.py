# Crie um programa que leia vários números inteiros pelo teclado e ao final
# mostre a média dos valores e qual foi o menor e o menor valor digitado.

cont = 0
soma = 0
maior = menor = None

while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break

    soma += num
    cont += 1

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma / cont

print(f'A média dos números digitados é: {media:.2f}')
print(f'O maior número é {maior} e o menor é {menor}')


