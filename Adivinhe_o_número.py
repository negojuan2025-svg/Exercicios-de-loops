import random

# O computador escolhe um número entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas = 0
palpite = 0

print("🔢 Bem-vindo ao Jogo de Adivinhação!")
print("Eu pensei em um número entre 1 e 100. Tente adivinhar!")

# O loop continua enquanto o palpite for diferente do número secreto
while palpite != numero_secreto:
    palpite = int(input("Qual é o seu palpite? "))
    tentativas += 1 # Adiciona uma tentativa a cada rodada
    
    if palpite < numero_secreto:
        print("Muito baixo! Tente um número maior.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente um número menor.")
    else:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")