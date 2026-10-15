while True:
    try:
        n=int(input(f'Informe um nº Inteiro: '))
        break
    except ValueError:
        print(f'Valor invalido, Somente nº inteiros!!!')