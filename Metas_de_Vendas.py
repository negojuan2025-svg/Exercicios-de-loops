venda = [250, 330, 440, 540, 350, 250, 368, 40, 250, 30, 30]
vendedores = ['maria', 'mara', 'joão', 'silva', 'santos', 'mario', 'carlos', 'marly', 'xuxa', 'chica', 'zinha']
meta = 50

# Inicializamos o índice em 0
i = 0

print("Vendedores que bateram a meta:")

# O loop continuará enquanto o índice for menor que o tamanho da lista
while i < len(venda):
    # Verificamos se a venda do vendedor atual é maior ou igual à meta
    if venda[i] >= meta:
        print(f"- {vendedores[i]}: vendeu {venda[i]}")
    
    # IMPORTANTE: Incrementamos o índice para não criar um loop infinito
    i += 1