
"""

numero = input('Vou dobrar o número que você digitar: ')


# errado - imprime NUMERONUMERO - ex >  10 vira 1010
print(f'O dobro de {numero} é {numero*2}')

numero_float = float(numero)
print(f'O dobro de {numero} é {numero_float*2}')
print(f'O dobro de {numero} é {numero_float*2:.0f}')

"""

"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')