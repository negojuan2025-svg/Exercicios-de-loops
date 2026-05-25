meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

print("Vendedores que bateram a meta:")
print("-" * 30)

# Percorremos cada item (sublista) dentro da lista vendas
for vendedor in vendas:
    # vendedor[0] é o nome, vendedor[1] é o valor da venda
    nome = vendedor[0]
    valor_venda = vendedor[1]
    
    if valor_venda >= meta:
        print(f"Parabéns {nome}! Venda: R$ {valor_venda:,.2f}")

print("-" * 30)