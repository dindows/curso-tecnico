nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
nota3 = float(input("Digite sua nota: "))
nota4 = float(input("Digite sua nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4
print("Sua média é", media)

if media <=3:
    print("Reprovado")
elif media <=5:
    print("Recuperação")
else:
    print("Aprovado")