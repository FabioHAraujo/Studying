"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = -1
while True:
    try:
        num = float(input('Por favor, digite um numero para descobrirmos se é par ou impar: '))
        if num%2 == 0:
            print("O número digita é par")
        else:
            print("O número digita é impar")
        break

    except:
        print('Você não digitou um número, tente novamente')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

while True:
    try:
        print("Olá, seja bem vindo, digite a hora atual, em seguida, os minutos: ")
        hora = int(input("Hora: "))
        min = int(input("Minutos: "))
        if hora >= 0 and hora <12:
            print(f"Bom dia, são {hora} e {min}")
        elif hora >= 12 and hora < 18:
            print(f"Boa tarde, são {hora} e {min}")
        elif hora >= 18 and hora <24:
            print(f"Boa noite, são {hora} e {min}")
        else:
            print("O dia só tem 24 horas amigão ^_^")
        break
    except:
        print('Você não digitou a hora corretamente :(')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

try:
    nome = input("Digite seu nome: ")
    if len(nome) < 5 and len(nome) > 0:
        print("Seu nome é curto")
    elif len(nome) < 7:
        print("Seu nome é normal")
    elif len(nome) >=7:
        print("Seu nome é muito grnade")
    else:
        print("Você não digitou nada")
except:
    print("Ah irmao... Colabora vai")


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

#   FEITO PELO PROFESSOR:

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

# try:
#     entrada_int = float(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro')

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

# entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Bom tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Bom noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Por favor, digite apenas números inteiros')

Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')

"""