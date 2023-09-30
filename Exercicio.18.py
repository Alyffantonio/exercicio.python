# As maçãs custam R$ 1,30 cada se forem
# compradas menos de uma dúzia, e R$ 1,00
# se forem
# compradas pelo menos 12. Escreva um
# programa que leia o número de maçãs
# compradas, calcule e
# escreva o custo total da compra.


qnt_macas = int(input("Digite a quantidade que vai comprar: "))

valor_macas = 1.30

total_pag = qnt_macas * valor_macas
if qnt_macas >= 12:
    valor_macas = 1.00
    total_pag = valor_macas * qnt_macas


print(f"{total_pag:.1f}")