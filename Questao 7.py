def valpagamento(valprestacao, diasatraso):
 
    percenmulta=3
    valmulta=(valprestacao*percenmulta)/100
    percenjurosdias=0.1
    valjurosdia=(valprestacao*percenjurosdias)/100
    valtotaljurosdia=valjurosdia*diasatraso
    valtotal=valprestacao+valmulta+valtotaljurosdia
 
    return valtotal
valprestacao=eval(input("entre com o valor:"))
quantprestacoespagas=0
valprestacoespagas=0
 
while valprestacao!=0:
    quantprestacoespagas+=1
    diasatraso=int(input("entre com os dias em atraso:"))
    valtotalpagamento=valpagamento(valprestacao,diasatraso)
    valprestacoespagas+=valtotalpagamento
    print ("total a ser pago é:", valtotalpagamento)
 
    valprestacao=eval (input("entre com o valor:"))
 
print("numero de prestações pagas:",quantprestacoespagas)
print("valor de prestações pagas:",valprestacao)