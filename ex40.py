# Faça um programa que leia duas notas e mostre a
# média final e informe se o aluno foi aprovado.

n1, n2 = map(int, input('Informe duas notas separadas por espaço: ').split())
media = (n1 + n2) / 2
print(f'Sua média é: {media}.')
if media >= 7:
    print('Aprovado')
elif media >= 5 and media < 7:
    print('Em recuperação')
else:
    print('Reprovado')