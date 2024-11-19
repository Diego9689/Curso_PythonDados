#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
# Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
# caso haja uma divisão por 0 ou raiz de numero negativo.
# Entrada Leia três valores de ponto flutuante (double) A, B e C.Saída
# Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular".
# Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto,
# com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
# Exemplos de Entrada	Exemplos de Saída 10.0 20.1 5.1 R1 = -0.29788 R2 = -1.71212 0.0 20.0 5.0 Impossivel calcular
# 10.3 203.0 5.0 R1 = -0.02466 R2 = -19.68408 10.0 3.0 5.0 Impossivel calcular
#B²-4*A*C
#-B(+-)(B²-4*A*C)/2*A
#if A == 0:
 #   print("Impossivel calcular")
#baskhara= baskhara**(1/2)
def media():
    media1=((n*4)+(n1*2)+(n2*3)+(n3*1))/10
    return media1
n=int(input())
n1=int(input())
n2=int(input())
n3=int(input())
a=n*4/10
b=n1*2/10
c=n2*3/10
d=n3*1/10
print(media())
media=(a+b+c+d)#/10
print(media)