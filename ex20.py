import random
n1, n2, n3 = map(str, input('Digite 3 nomes separados por espaço: ').split())
nomes = [n1, n2, n3]
random.shuffle(nomes)
print(nomes)