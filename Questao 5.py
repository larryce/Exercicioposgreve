quant=int(input("quantos cigarros voce fuma por dia? "))
anos=int(input("entre com quantos anos você fuma: "))
min=0
for min in range(1, quant+1):
    min += 10
tempo=(anos*365)*min
print("você perdeu", tempo ," minutos")