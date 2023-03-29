import random

# Jogo do Pedra, Papel ou Tesoura

# Inserir a escolha entre Pedra, Papel ou Tesoura
jogador = input("Escolha entre Pedra, Papel ou Tesoura: \n")
jogador1 = jogador.upper()

# Escolha do computador
PPT = ["PEDRA", "PAPEL", "TESOURA"]
computador = random.choice(PPT)

# Imprimir as respostas:
print(f"Você escolheu: {jogador1} \nComputador escolheu: {computador}")

# Critérios a serem seguidas para definir vitória ou derrota:
if jogador1 == computador:
    print("\nDeu empate!")
elif jogador1 == "PEDRA" and computador == "TESOURA":
    print("\nVocê venceu!")
elif jogador1 == "PAPEL" and computador == "PEDRA":
    print("\nVocê venceu!")
elif jogador1 == "TESOURA" and computador == "PAPEL":
    print("\nVocê venceu!")
else:
    print("\nVocê perdeu!")
