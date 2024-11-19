def multiplos(x,y):
    if y%x==0:
        c=print("Sao Multiplos")
    else:
        c=print("Nao sao Multiplos")
    return c

def multiplos1(x, y):
    if x % y == 0:
        c=print("Sao Multiplos")
    else:
        c=print("Nao sao Multiplos")
    return c
def maior(x,y):
    if a<b:
        f=multiplos(a,b)
    else:
        f=multiplos1(a,b)
    return f
n=input()
a,b=n.split()
a=int(a)
b=int(b)
maior(a,b)