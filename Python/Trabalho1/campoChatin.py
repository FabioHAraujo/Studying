def criaCampo(altura, largura):
    linha = []
    for i in range(altura):
        coluna = []
        for i in range(largura):
            valor = input()
            coluna.append(valor)
        linha.append(linha)
    return linha

while True:
    linhas = int(input())
    colunas = int(input())
    if linhas != 0 and colunas != 0:
        campo = criaCampo(linhas, colunas)
        for coluna in campo:
            print(coluna)
    else:
        break
