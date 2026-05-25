# Pedimos a palavra e convertemos para minúsculas para facilitar a comparação
palavra = input("Digite uma palavra: ").lower()

vogais = "aeiou"
contador = 0
i = 0

# O loop percorre a palavra letra por letra
while i < len(palavra):
    # Verificamos se a letra atual está dentro da string de vogais
    if palavra[i] in vogais:
        contador += 1
    i += 1

print(f"A palavra '{palavra}' tem {contador} vogais.")