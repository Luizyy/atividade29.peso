# Exercício Python 29: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.


p = []

for pessoasp in range(5):
    kg = float(input("Digite seu peso:"))
    p.append(kg)
    
p2 = sorted(p)

print(p2[0], p2[4])