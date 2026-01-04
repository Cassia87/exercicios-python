# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO".

cidade = input('Digite o nome da cidade: ')
palavra_encontrada = cidade.find('Santo', 0)
if palavra_encontrada != -1:
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')