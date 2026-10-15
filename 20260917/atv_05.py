senha='dev123'
tentativas=0

while (tentativas < 3):
    digitado=input(f'Digite a senha: ')
    if digitado==senha:
        print(f'Acesso Concedido')
        break
    tentativas+=1
    print(f'Acesso Negado!')
    print(f'{tentativas}/3 tentativa')
else:
    print(f'Acesso Bloqueado!!')