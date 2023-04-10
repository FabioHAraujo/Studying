print("#################################")
print("Bem Vindo ao jogo de Adivinhação!")
print("#################################")

numero_secreto = 42
chute = 0
foi = False
while not foi:
    chute = int(input("Digite o seu número: "))
    if chute == numero_secreto:
        foi = True
    else:
        print("Você errou!")
print("Você acertou!")
print("Fim do jogo!")
