while True:
    try:
        temperatura=int(input(f'Informe a temperatura: '))
        break
    except ValueError:
        print(f'Informa uma temperatura valida!')
if temperatura < 15:
    print(f'Frio')
elif 15<= temperatura <= 25:
    print(f'Agradavel!')
else:
    print(f'Calor')

