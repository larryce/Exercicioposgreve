base = int(input("Digite a base: "))

expoente = int(input("Digite o expoente: "))

num = 1

result = 1



while (num <= expoente):
  result = result*base
  num += 1
print( base, "elevado a", expoente, "� igual a:", result)
