"""
FORMATANDO VALORES COM MODIFICADORES

:s - texo(strings)
:d - Inteiros (int)
:f - Numeros de ponto flutuanse (float)
:. -(NUMERO)f - Quantidade de casas decimais (float)
: -(CARECTERE)(> ou  < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esqueda
< - Direita
^- Centro
"""
num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = 'A ansiedade nervoso é tão grande que n conseguir fechar os olhos'
print(f'{nome:s}')

print(nome.lower()) #TUDO MINUSCULO  
print(nome.upper()) #TUDO MAIUSCULO
print(nome.title()) #PRIMEIRAS LETRAS MAIUSCULAS