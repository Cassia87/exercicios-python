# Crie um programa que leia o nome de uma
# pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo: ')).strip().upper()
palavra_encontrada = nome.find('SILVA')
if palavra_encontrada != -1:
    print('Seu nome tem SILVA')
else:
    print('Seu nome não tem SILVA')