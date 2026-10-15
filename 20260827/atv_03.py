nota1=float(input(f"Informe a 1º nota: "))
nota2=float(input(f"Informe a 2º nota: "))

media= nota1+nota2/2

if  media > 7.0:
    print(f"Média {media:.2f}, Aluno APROVADO")
else:
    print(f"Média {media:.2f}, Aluno em RECUPERAÇÃO")