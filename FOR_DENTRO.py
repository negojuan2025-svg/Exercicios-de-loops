numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_total = 0

# O primeiro for percorre as "linhas" (as sublistas)
for linha in numeros:
    print(f"Lendo a lista: {linha}")
    
    # O segundo for percorre cada "item" dentro daquela linha específica
    for numero in linha:
        print(f"  Número encontrado: {numero}")
        soma_total += numero # Acumula o valor na nossa variável de soma

print("-" * 25)
print(f"A soma total de todos os números é: {soma_total}")