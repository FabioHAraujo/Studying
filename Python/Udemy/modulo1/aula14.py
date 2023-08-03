a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

#o conteúdo dentro das chaves é um placeholder que pode ser substituído durante o format.
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}' # Utilizando Parametros
formato = string.format(
    nome1=a, nome2=b, nome3=c # Determinando os parametros
)
print(formato)

formato2 = 'a={} b={} c={}'.format(a,b,c)
print(formato2)

string2 = 'a={} b={} c={}'
formato3= string2.format(a,b,c)
print(formato3)

string3 = 'a={0} b={1} c={0} d={2} e={1}'
formato4= string3.format(a,b,c)
print(formato4)