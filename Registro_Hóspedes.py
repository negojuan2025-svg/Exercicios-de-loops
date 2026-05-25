# 1. Identificar a quantidade de pessoas no quarto
quantidade = int(input("Quantas pessoas ficarão no quarto (1 a 4)? "))

# Criamos a lista vazia que armazenará os dados do quarto
quarto = []

# 2. Loop para registrar cada pessoa
for i in range(quantidade):
    print(f"\nRegistro do {i + 1}º hóspede:")
    nome = input("Nome do hóspede: ")
    cpf = input("CPF do hóspede: ")
    
    # Criamos uma sublista para essa pessoa específica
    # Já formatamos o CPF conforme o seu exemplo
    hospede = [nome, f"cpf:{cpf}"]
    
    # 3. Adicionamos a sublista dentro da lista 'quarto'
    quarto.append(hospede)

# Exibição do resultado final
print("\n--- Cadastro Finalizado ---")
print("Lista de ocupantes do quarto:")
print(quarto)