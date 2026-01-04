# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o
# salário do comprador e em quantos anos ele vai pagar. A
# prestação mensal não pode exceder 30% do salário ou
# então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario: '))
anos_financiamento = int(input('Digite em quantos anos será o financiamento: '))
prestacao = valor_casa / (anos_financiamento * 12)
if prestacao > salario * 0.3:
    print(f'O empréstimo não pode ser concedido pois o valor da prestação será R$ {prestacao} e ultrapassa 30% do salário')
else:
    print(f'Empréstimo pode ser concedido e a prestação será R$ {prestacao:.2f}')