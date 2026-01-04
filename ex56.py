# Faça um programa que leia o nome, a idade e o sexo de 4 pessoas.
# Mostre ao final a média de idade do grupo, qual o nome do homem
# mais velho e quantas mulheres tem menos de 20 anos.

soma = 0
homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres = 0
mulher_menos_vinte = 0
for p in range(1,4):
    print(f'======= {p}ª pessoa =======')
    nome = str(input(f'Nome: ')).strip().upper()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [F/M]: ')).strip().upper()
    if p == 1 and sexo in 'Mm':
        homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if idade > homem_mais_velho and sexo in 'Mm':
        homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if sexo in 'Ff':
        mulheres += 1

    if sexo in 'Ff' and idade < 20:
        mulher_menos_vinte += 1

    soma = soma + idade
media = soma / 4
print(f'A média das idades é: {media:.2f}')
print(f'O homem mais velho tem {homem_mais_velho} anos e se chama {nome_homem_mais_velho}')
print(f'Existem {mulher_menos_vinte} mulheres com menos de 20 anos')