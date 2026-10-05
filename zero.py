lado=int(input("Digite o lado"))

perimetro = lado * 4

if perimetro>=10:
    print("perimetro maior que dez")
    print("perimetro:", perimetro)                    #se >=10
#Perimetro maior que 10
#se ==10
elif perimetro==10:
    print("perimetro igual a dez")
    print("perimetro:", perimetro)
#Perimetro igual a 10
#senão
else:
    print("perimetro menor que dez")
    print("perimetro", perimetro)