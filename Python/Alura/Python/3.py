print("#################################")
print("Bem Vindo ao jogo de Adivinhação!")
print("#################################")

numero_secreto = 42
chute = 0
acertou = False
while not acertou:
    chute = int(input("Digite o seu número: "))
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    acertou = chute == numero_secreto
    if(acertou):
        print("Você acertou!")
        print("Fim do jogo!")
    else:
        print("Você errou!")
        if(maior):
            print("O número que você chutou é maior que o número secreto, tente novamente.")
        elif(menor):
            print("O número que você chutou é menor que o número secreto, tente novamnente.")
