"""
ENTRADA DE DADOS -INPUT
"""
# input("Qual o seu nome?")

nome = input("Qual o seu nome? ")#INPUT PODE SER USADO PARA DAR VALOR A UMA VARIAVEL.
idade = input("Qual sua idade? ")
print(f'O usuario digitou {nome} e o tipo da variavel é' f'{type(nome)}')
print()#Paragrafo
print(f'{nome} tem {idade} anos.')

ano_nascimento = 2022-int(idade) #Deve ser feito o cast/converter a entrada pelo INPUT que é str para INT
print()#Paragrafo
print(f'{nome} nasceu em  {ano_nascimento}. ')

#calculadora (somente soma)

numero_1 = input("Digite um numero: ")
numero_2 = input("Digite outro numero: ")

print(int(numero_1) + int(numero_2) ) #LEMBRE DE CONVERTER EM INT