contador=0
senha='sen@c2026'
user='admin'

while (contador < 3):
    password=input(f'login: {user}\nDigite sua senha: ')
    if senha==password:
        print(f'Acesso concedido')
        break
    contador += 1
    print(f'Senho incorreta')
else:
    print(f'Acesso Bloqueado!')
