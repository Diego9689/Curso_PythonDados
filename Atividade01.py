def hipo(x,b):
    l3=((x*x)+(b*b))
    l3=l3**(1/2)
    return l3
print("Digite os dois lados menores do triângulo")
L1=float(input("Digite o primeiro lado: "))
L2=float(input("Digite o segundo lado: "))
print(f"Lados digitados: {L1}, {L2} \nA Hipotenusa deste triâgulo é: {hipo(L1,L2)}")