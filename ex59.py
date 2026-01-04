# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# O programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
resp = 0
while resp != 5:
    print("""
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    """)
    resp = int(input('Qual é a sua opção? '))
    if resp == 1:
        soma = n1 + n2
        print(f'A soma de {n1} e {n2} é {soma}.')
    elif resp == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação de {n1} e {n2} é {multiplicacao}.')
    elif resp == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é: {maior}.')
    elif resp == 4:
        print('Digite outros números')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif resp == 5:
        print('Finalizando o programa...')
    else:
        print('Opção inválida. Tente novamente.')


