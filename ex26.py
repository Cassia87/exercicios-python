# Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra "A", em que
# posição ela aparece a primeira vez e em que posição
# ela aparece a última vez.

frase = str(input('Digite sua frase preferida: ')).strip().upper()
print(f'A frase tem {frase.count('a')} letras A')
print(f'O primeiro a aparece pela primeira vez na posição {frase.find('a')} e a última vez na posição {frase.rfind('a')}')
