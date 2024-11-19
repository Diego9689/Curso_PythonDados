i=int(input("Digite a sua idade: "))
if i>2:
 ni=i-2
 hpc=ni*4
 hec=hpc+21
 print(f"Se você fosse um cão você teria {hec} anos")
elif i==0 or i<0:
    print("Idade inválida")
else:
    if i==1:
        nvi=i*10
        print(f"Se você fosse um cão você teria {nvi} anos")
    elif i==2:
        nid=i*10.5
        print(f"Se você fosse um cão você teria {nid:.2f} anos")
