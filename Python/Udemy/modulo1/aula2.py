"""
CRLF = Carriage Return Line Feed  - (Localizado lá embaixo no VSCode)
Sistemas Windows usam CRLF e sistemas Unix usam LF.
O CRLF significa que existe um feed de linha com retorno de linha.
Sendo assim, não ocorre apenas a quebra de linha, mas um return também.
Ao fim de cada linha, existe automaticamnete um:
\r\n
Este é responsável por retornar a linha e após isso quebrar ela.
Por padrão, o windows tem aceitado \n e já realizdado o \r.
"""


print(12, 34, sep='', end='\r\n')
print(12, 34, sep='', end='#')
print(12, 34, sep='', end='\n')
print(56, 78, sep='-', end='\n')