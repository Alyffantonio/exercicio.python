# Escreva um algoritmo para ler o
# número total de eleitores de um
# município, o número de votos brancos,
# nulos e válidos. Calcular e escrever o
# percentual que cada um representa em
# relação ao total de eleitores.

votos_branc=int(input("Digite a quantidade de votos em branco: "))
votos_nulos=int(input("Digite a quantidade de votos nulos: "))
votos_val=int(input("Digite a quantidade de votos validos: "))

eleitores = votos_val + votos_nulos + votos_branc

votos_val = (votos_val/eleitores)*100
votos_nulos = (votos_nulos/eleitores)*100
votos_branc = (votos_branc/eleitores)*100

print(f"Quantidade de eleitores: {eleitores}\n"
      f"percentual de votos nulos em relação ao total de eleitores: {votos_nulos:.2f}\n"
      f"percentual de votos em branco em relação ao total de eleitores {votos_branc:.2f}\n"
      f"percentual de votos validos em relação ao total de eleitores {votos_val:.2f}")
