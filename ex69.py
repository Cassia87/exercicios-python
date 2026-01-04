# Crie um programa que leia a idade e o sexo de várias pessoas
# A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

homens = 0
mulheres_menores_vinte = 0
maioridade = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if idade >=18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menores_vinte += 1

    if resp == 'N':
        break

print(f'Quantidade de pessoas maiores de 18 anos: {maioridade} ')
print(f'Quantidade de homens: {homens} ')
print(f'Quantidade de mulheres com menos de 20 anos: {mulheres_menores_vinte} ')