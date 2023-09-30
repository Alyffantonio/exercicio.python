# 6. Ler um valor e escrever a mensagem É MAIOR
# QUE 10! se o valor lido for maior que 10, caso
# contrário escrever NÃO É MAIOR QUE 10!

num = int(input("Digite um numero: "))

if num > 10:
    print(f"o numero: {num} é maior que 10!")
else:
    print(f"o numero: {num} não é maior que 10!")