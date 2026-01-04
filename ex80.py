# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for c in range(5):
    lista.append(int(input('Digite um número: ')))

print(f'Lista ordenada: {sorted(lista)}')
print(f'Lista reversa: {sorted(lista, reverse=True)}')
