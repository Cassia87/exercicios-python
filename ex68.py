# Faça um programa que jogue par ou ímpar.
# O jogo só será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=-' * 10)
print('Jogo do Par ou Ímpar')
print('=-' * 10)

vitorias = 0  # contador de vitórias

while True:
    jogador = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? ')).strip().upper()
    computador = randint(0, 10)

    soma = jogador + computador
    resultado = 'PAR' if soma % 2 == 0 else 'IMPAR'

    print(f'O computador escolheu {computador} e você escolheu {jogador}.')
    print(f'A soma deu {soma} → {resultado}')

    if escolha == resultado:
        vitorias += 1
        print('Você venceu!')
        print(f'Vitórias consecutivas: {vitorias}')
        print('-' * 30)
    else:
        print('Você perdeu!')
        print(f'Total de vitórias consecutivas: {vitorias}')
        break

