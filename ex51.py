# Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.

print('==' * 10)
print('10 TERMOS DE UMA PA')
print('==' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
ultimo = primeiro + (9 * razao)

for i in range(primeiro, ultimo + 1, razao):
    print(i, end=' -> ')
