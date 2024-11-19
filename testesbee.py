T = int(input().strip())
respostas = list(map(int, input().split()))
acertos = respostas.count(T)
print(acertos)