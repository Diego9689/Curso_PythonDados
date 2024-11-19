#def nota_do_aluno():
  #print(f"Digite a sua nota:")
#n4=int(input(nota_do_aluno()))
#n5=int(input(nota_do_aluno()))
#n6=int(input(nota_do_aluno()))
#def calcular_media():
    #media=(n4+n5+n6)/3
    #return media
#print(f"Sua média foi de: {calcular_media():.3f}")
#def my_msg(msg):
    #print(msg)
    #my_msg("ola mundo")
    #my_msg("bom dia")
    #my_msg("bem-vindo")
    #my_msg("ola")
#g=swap(n4,n5)
#print(g)
#def hipo():
#    l3=((L1*L1)+(L2*L2))
#    l3=l3**(1/2)
#    return l3
#print("Digite os dois lados menores do triângulo")
#L1=float(input("Digite o primeiro lado: "))
#L2=float(input("Digite o segundo lado: "))
#l3=hipo()
#print(f"Lados digitados: {L1}, {L2} \nA Hipotenusa deste triâgulo é: {l3}")
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
except error:
    print("erro na execução")

a,b=1,2