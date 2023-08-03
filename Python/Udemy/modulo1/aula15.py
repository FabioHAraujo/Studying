nome = input('Qual seu nome? ')
# print(f'O seu nome é {nome=}') # printa o nome da variável seguido do valor.
print(f'O seu nome é {nome}')


# Forma fácil de ao invés de considerar string já considerar inteiro no input
# Quebra o programa se a pessoa digitar letra
# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite outro número: ')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero1 = int(numero_1)
int_numero2 = int(numero_2)

print(f'A soma dos números é: {int_numero1 + int_numero2}')