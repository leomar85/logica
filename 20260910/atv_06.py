frase = input(f'Digite uma frase:\n')
contador = 0

for caractere in frase:
    if caractere == ' ':
        contador +=1

print(f'Na frase {frase}, possui {contador} em branco.')
