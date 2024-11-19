cont=0
valido=0
while valido==False and cont<=3:
    u=input("Digite o seu login:\n")
    s=input("Digit a sua senha:\n")
    if u=="Diego" and s=="1234":
        u1=True
        s1 = True
        valido=True
        print("SENHA CORRETA\n BEM-VINDO")
    else:
        u1=False
        s1=False
    if u1==False and s1==False:
        print("SENHA INCORRETA \nTENTE NOVAMENTE"
              "\n================================")
        print(f"TENTATIVAS RESTANTES {3-cont}")

    cont=cont+1

    if cont>3:
        print("BLOAQUEDO \nEXCESSO DE TENTATIVAS")

#valido=0
#while valido==False:
 #   d = input("Digite um numero")
  #  if d.isdigit()==True:
   #     valido=True
    #else:
     #   print("numero ivalido")
      #  valido=False


