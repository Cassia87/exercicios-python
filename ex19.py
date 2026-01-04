from random import choice
n1, n2, n3 = map(str, input('Digite 3 nomes separados por espaço: ').split())
nomes = [n1, n2, n3]
escolhido = choice(nomes)
print(f'O escolhido foi: {escolhido}')