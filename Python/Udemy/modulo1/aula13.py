# Exercicio - Calculo de IMC
nome = "Fábio Henrique"
altura = 1.70
peso = 93
imc = peso / altura**2


# f-strings (isso não é uma função, é só pra etender que este é o conteúdo de f-strings [f significa formatação/format]) {
linha_1 = f"{nome} tem {altura:.2f} de altura"
linha_2 = f"pesa {peso} quilos e seu imc é {imc:.2f}"
print(linha_1)
print(linha_2)
# }


print("Nome:", nome)
print("Altura:", altura, "metros")
print("Peso:", peso, "kg")
print("IMC de:", imc)