# Pedimos o número ao usuário
numero = int(input("Digite um número para ver a sua tabuada: "))
i = 1 # Começamos multiplicando por 1

print(f"\nTabuada do {numero}:")
print("-" * 15)

# O loop roda enquanto o multiplicador for menor ou igual a 10
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i:2} = {resultado}")
    i += 1 # Incrementamos para passar para o próximo número

print("-" * 15)