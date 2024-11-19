def tarifa():
    if n==1:
        tp=10.95
    elif n==0:
        tp=0
    elif n<0:
        tp=0
    else:
         k=n-1
         to=k*2.95
         tp=to+10.95
    return tp
try:
    n=int(input("Digite o total de itens comprados: "))
    tp=tarifa()
    print(f"A quantidades de itens comprados foi de: {n}\nO valor total do frete foi de: {tp} ")
except:
    print("erro na execução ou Digito invalido")