# Faça um programa que mostre a sequência de Fibonacci de n elementos

n = int(input("Quantos termos da sequência de Fibonacci você quer ver? "))

a = 0
b = 1
contador = 0

while contador < n:
    print(a, end=" → ")
    c = a + b
    a = b
    b = c
    contador += 1


