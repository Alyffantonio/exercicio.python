# Escreva um algoritmo para ler a hora de
# início e a hora de fim de um jogo de Xadrez
# (considere apenas horas inteiras, sem os
# minutos) e calcule a duração do jogo em
# horas, sabendo-se que o tempo máximo de
# duração do jogo é de 24 horas e que o jogo
# pode iniciar em um dia e terminar no dia
# seguinte

hora_inicio = int(input('Digite a hora de inicio da partida de xadrez: '))
hora_fim = int(input('Digite a hora do fim da partida de xadrez: '))

if hora_inicio >= hora_fim:
    resultado = hora_fim - (hora_inicio - 24)
else:
    resultado = hora_fim - hora_inicio

print(f'A duração do jogo foi de {resultado}')