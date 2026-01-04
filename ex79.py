# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente.

lanche = []
while True:
    l = str(input('Digite o nome de uma comida: ')).strip().lower()
    if l in lanche:
        print('Valor duplicado, não vou adicionar...')
    else:
        lanche.append(l)
        print(f'{l} adicionado com sucesso!')
    res = str(input('Deseja continuar adicionando? [S/N]: ')).strip().lower()[0]
    if res == 'n':
        break
print(f'Lanches adicionados: {lanche}')
