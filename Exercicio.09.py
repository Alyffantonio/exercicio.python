# Faça um código que receba 4
# números e realize a soma deles e a
# média entre eles. e mostre os
# resultados.

cont = 0
soma = 0
for x in range(4):
    num = int(input("Digite um numero: "))
    soma = (soma + num)
    cont = soma/num

print("A soma dos números é:", soma)
print("A média dos números é:", cont)