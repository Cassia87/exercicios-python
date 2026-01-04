# Crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas e minúsculas.
# quantas letras ao todo (sem considerar espaços).
# quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'A quantidade letas de {nome} é {len(nome) - nome.count(" ")}')
print(f'Seu primeiro nome tem {nome.find(' ')} letras')
nome_separado = nome.split()
print(f'Seu terceiro nome é {nome_separado[2]} e ele tem {len(nome_separado[2])} letras')
