saldo = 500
saque = int(input("Digite o valor do saque:"))
if saque <= saldo:
    print("Saldo realizado com sucesso!")
else:
    print("Saldo insuficiente!")