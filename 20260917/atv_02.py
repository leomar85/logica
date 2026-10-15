soma=0
while True:
    valor=float(input(f'\nOBS: Digite 0 para encerrar o registro\nInforme o Valor do item R$: '))
    soma+=valor

    if valor == 0:
        break
print(f'\nTotal dos intens R$ {soma:.2f}')