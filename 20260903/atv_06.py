soma= 0

for i in range(10):
    n=int(input(f'Digite um numero: '))
    soma+=n
    i+=1
    
media= soma/i
print(f'A média dos valores é={media}')