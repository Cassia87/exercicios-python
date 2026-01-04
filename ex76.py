# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma
# listagem de preços, organizando os dados em forma tabular.

produtos = ('xampu', 12.50, 'hidratante', 23.45, 'batom', 45.90, 'colirio', 11.80)

print('=-' * 10)
print("""
𝕝𝕚𝕤𝕥𝕒𝕘𝕖𝕞 𝕕𝕖 𝕡𝕣𝕖𝕔𝕠𝕤
""")
print('=-' * 10)
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<34} ', end='')
    print(f'R$ {produtos[c+1]:>7.2f}')
print('-'*45)