# Escreve um programa que leia dois números e compare
# qual é maior e menor ou se são iguais.

n1, n2 = map(int, input('Digite dois números separados por espaço: ').split())
if n1 > n2:
    print(f'O número {n1} é maior que o {n2}')
elif n1 < n2:
    print(f'O número {n2} é maior que o {n1}')
else:
    print('Os números são iguais')