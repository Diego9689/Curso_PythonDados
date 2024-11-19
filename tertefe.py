n = float(input())

# Convertendo o valor para centavos (evita problemas com ponto flutuante)
centavos = int(round(n * 100))

# Notas
cem = centavos // 10000
centavos %= 10000

nota50 = centavos // 5000
centavos %= 5000

nota20 = centavos // 2000
centavos %= 2000

nota10 = centavos // 1000
centavos %= 1000

nota5 = centavos // 500
centavos %= 500

nota2 = centavos // 200
centavos %= 200

# Moedas
moeda1 = centavos // 100
centavos %= 100

moedas050 = centavos // 50
centavos %= 50

moeda025 = centavos // 25
centavos %= 25

moeda010 = centavos // 10
centavos %= 10

moeda005 = centavos // 5
centavos %= 5

moeda001 = centavos // 1

# Exibindo os resultados
print(f"NOTAS:\n{cem:.0f} nota(s) de R$ 100.00\n{nota50:.0f} nota(s) de R$ 50.00\n{nota20:.0f} nota(s) de R$ 20.00"
      f"\n{nota10:.0f} nota(s) de R$ 10.00\n{nota5:.0f} nota(s) de R$ 5.00\n"
      f"{nota2:.0f} nota(s) de R$ 2.00\n"
      f"MOEDAS:\n{moeda1:.0f} moeda(s) de R$ 1.00\n{moedas050:.0f} moeda(s) de R$ 0.50\n{moeda025:.0f} moeda(s) de R$ 0.25\n"
      f"{moeda010:.0f} moeda(s) de R$ 0.10\n{moeda005:.0f} moeda(s) de R$ 0.05\n{moeda001:.0f} moeda(s) de R$ 0.01")
