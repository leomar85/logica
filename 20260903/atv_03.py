n1=int(input(f'Informe 1º nº: '))
n2=int(input(f'Informe 2º nº: '))

if n1 > n2:
    n1,n2=n2,n1
if n1%2 ==0:
    n1+=1
if n2%2 ==1:
    n2+=1

for i in range(n1,n1,2):
    print(f'{i}')

inicio=int(input(f'Digite o número inicial: '))
fim = int(input(f'Digite o númerofinal: '))

for i in range(inicio,fim,+1):
    if i % 2!=0:
        print(f'{i}, end="')