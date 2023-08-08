"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[5])
print(variavel[4:]) # vai do 4 ao fim
print(variavel[4:8]) # vai do 4 ao 7
print(variavel[0:5]) # vai do 0 ao 4
print(variavel[-8:-2])
print(len(variavel)) # exibe o tamanho da string
print(variavel[0:len(variavel):1]) # chamado de passo, começa em 0 e vai de 1 em 1
print(variavel[0:len(variavel):2]) # chamado de passo, começa em 0 e vai de 2 em 2
print(variavel[0:9:2])
print(variavel[-1:-10:-1]) # Inverte a string
print(variavel[::-1])