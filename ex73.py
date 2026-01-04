# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times_brasileirao = (
    "Atlético Mineiro",
    "Bahia",
    "Botafogo",
    "Ceará",
    "Corinthians",
    "Cruzeiro",
    "Flamengo",
    "Fluminense",
    "Fortaleza",
    "Grêmio",
    "Internacional",
    "Juventude",
    "Mirassol",
    "Palmeiras",
    "Red Bull Bragantino",
    "Santos",
    "São Paulo",
    "Vasco da Gama",
    "Vitória",
    "Sport"
)

print(f'Os cinco primeiros times são: {times_brasileirao[0:5]}')
print(f'Os últimos quatro times são: {times_brasileirao[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times_brasileirao)}')
print(f'O Flamengo está na posição {times_brasileirao.index('Flamengo')}')