soma=0
for i in range(5):
    valor=float(input(f'Informe o valor gasto no dia R$ '))
    soma+= valor
media=soma/i
print(f'Total gasto na semana foi R${soma:.2f}')
print(f'A média dos gastos é de R${media:.2f}')