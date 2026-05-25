soma = 0
numero = 1

# O loop continua enquanto a soma for menor ou igual a 20
while soma <= 20:
    print(f"Somando {numero}... (Total atual: {soma})")
    soma += numero
    numero += 1

print("---")
print(f"A soma final ultrapassou 20! Resultado: {soma}")