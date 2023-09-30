# Escreva um algoritmo para ler dois
# valores (considere que não serão lidos
# valores iguais) e escrevê-los em ordem
# crescente
n1 = 0
n2 = 0

while n1 == n2:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))

    if n1 > n2:
        print(n2, n1)
    elif n1 < n2:
        print(n1, n2)

    else:
        print("Não digite valores iguais, Digite novamente!")