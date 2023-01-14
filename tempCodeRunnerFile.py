"""
ENTRADA DE DADOS -INPUT
"""
# input("Qual o seu nome?")

nome = input("Qual o seu nome? ")#INPUT PODE SER USADO PARA DAR VALOR A UMA VARIAVEL.
idade = input("Qual sua idade? ")
print(f'O usuario digitou {nome} e o tipo da variavel é' f'{type(nome)}')
print()
print(f'{nome} tem {idade} anos.')

ano_nascimento = 2022-int(idade) #Deve ser feito o cast/converter a entrada pelo INPUT que é str para INT
print()
print(f'{nome} nasceu em  {idade} ')