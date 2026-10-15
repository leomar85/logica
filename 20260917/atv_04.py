soma=0
acumulador=0
print(f'condição deparada: -1')
while True:
    nota=float(input(f'Digite a nota:'))
    soma += nota
    acumulador+= 1
    if nota == -1:
        break
media=soma/acumulador
print(f'A média da Turma é {media:.2f}')