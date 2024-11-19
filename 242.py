n=float(input())
cem=n//100
resto=n%100

nota50=resto//50
resto2=resto%50

nota20=resto2//20
resto3=resto2%20

nota10=resto3//10
resto4=resto3%10

nota5=resto4//5
resto5=resto4%5

nota2=resto5//2
resto6=resto5%2

moeda1=resto6//1
resto7=resto6%1

moedas050=resto7//0.50
resto8=resto7%0.50

moeda025=resto8//0.25
resto9=resto8%0.25

moeda010=resto9//0.10
resto10=resto9%0.10

moeda005=resto10//0.05
resto11=resto10%0.05

moeda001=resto11//0.01
print(f"NOTAS:\n{cem:.0f} nota(s) de R$ 100.00\n{nota50:.0f} nota(s) de R$ 50.00\n{nota20:.0f} nota(s) de R$ 20.00"
f"\n{nota10:.0f} nota(s) de R$ 10.00\n{nota5:.0f} nota(s) de R$ 5.00\n"
f"{nota2:.0f} nota(s) de R$ 2.00\n"
f"MOEDAS:\n{moeda1:.0f} moeda(s) de R$ 1.00\n{moedas050:.0f} moeda(s) de R$ 0.50\n{moeda025:.0f} moeda(s) de R$ 0.25\n"
f"{moeda010:.0f} moeda(s) de R$ 0.10\n{moeda005:.0f} moeda(s) de R$ 0.05\n{moeda001:.0f} moeda(s) de R$ 0.01")