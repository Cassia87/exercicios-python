# Faça um programa que calcule a soma entre todos
# os números que são ímpares e múltiplos de três e que
# se encontram no intervalo de 1 até 500.
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i

print(f'A soma dos múltiplos de 3 no intervalo entre 1 e 500 é: {soma}')
