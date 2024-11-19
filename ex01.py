def valida(x,t,a):
    if a + b > c and a + c > b and b + c > a:
        r=True
    else:
        r=False
    return r
def traopezio(x,t,a):
    ar=(x+t)*a/2
    return ar
def perimetro(x,t,a):
    p=x+t+a
    return p

def programa(x,t,a):
    if valida(x,t,a)==True:
       s=print(f"Perimetro = {perimetro(x,t,a)}")
    else:
       s=print(f"Area = {traopezio(x,t,a)}")
    return s
da=input()
a,b,c=da.split()
a=float(a)
b=float(b)
c=float(c)
programa(a,b,c)