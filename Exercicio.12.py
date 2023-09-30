# Faça um algoritmo que leia a idade de
# uma pessoa expressa em anos, meses e dias
# e escreva a idade dessa pessoa expressa
# apenas em dias. Considerar ano com 365
# dias e mês com 30 dias.


anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite o mes atual: "))
dias = int(input("Digite o dia atual: "))

idade_em_dias = (anos * 365) + (meses * 30) + dias

print("A idade em dias é:", idade_em_dias)
