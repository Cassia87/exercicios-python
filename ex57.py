# Faça um programa que pergunte o sexo de uma pessoa mas
# só aceite 'M' ou 'F' como entrada e continue pedindo
# até receber a entrada correta.

resp = 'fm'
while resp not in 'FM':
    resp = input('Digite o seu sexo: [F/M] ')

print('Fim')
