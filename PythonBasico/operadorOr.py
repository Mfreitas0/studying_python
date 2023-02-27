"""
OPERADOR NOOLEANO OR
"""

nome = input('Qual o seu nome? ')

""" 
if nome:
    print(nome)
else:
    print('Você não digitou nada')
"""
print( nome or 'Você não digitou nada!!') 

print(nome or None or False or 0 or 'Você não digitou nada' or 'outra coisa')
#VAI PARA NA PRIMEIRA CONDIÇÃO QUE DER TRUE

