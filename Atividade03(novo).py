def taf1(x):
    pkm=x*2.75
    total=pkm+4.5
    return total
def taf2(x):
    pkm=x*3.5
    total=pkm+5.85
    return total
def verifica(x):
    if x>=6 and x<20:
        tp=1
    else:
        tp=2
    return tp
def chama(x,y):
    if x==1:
        total=taf1(y)
    else:
        total=taf2(y)
    return total
def domigo(x,y):
    if dia=="Domingo":
        y=4
        saida=print(f"A bandeira usada foi a {verifica(y)}\nO valor total da corrida foi de: R${chama(verifica(y), km):.2f} ")
    else:
        saida=print(f"A bandeira usada foi a {verifica(hora)}\nO valor total da corrida foi de: R${chama(verifica(hora),km):.2f} ")
    return saida
try:
    T=0
    while T==0:
        dia=input("Qual é o dia ?\nAVISO\n\"Se for \"Domingo\" Digite a primeira letra em maiusculo e o restante em minusculo\"\n: ")
        hora=int(input("Digite o horario \"Só o numero das horas, sem os minutos\": "))
        km=float(input("Digite a quantidade de kilometros percorridos: "))
        domigo(dia,hora)
except:
    print("ERRO NA DIGITAÇÃO")

