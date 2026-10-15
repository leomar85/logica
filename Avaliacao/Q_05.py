contador=0
while True:
    try:
        n=int(input(f'Digite um nº inteiro positivo: '))
        contador-=1
    except ValueError:
        print(f'{contador}')