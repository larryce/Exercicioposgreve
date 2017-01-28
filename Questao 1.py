quantpizza= int(input("Digite quantas pizzas voce deseja: "))
valorpizza = float(input("Digite o valor da pizza: "))

imposto = valorpizza * (8/100)
semimposto = valorpizza * quantpizza

totaldavenda = semimposto + imposto

print("O valor a ser cobrado e: ", totaldavenda)
