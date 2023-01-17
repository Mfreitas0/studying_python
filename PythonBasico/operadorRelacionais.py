"""
Operadores Relacionais
++ > >= < <= !=
"""

nome = input('Qual o seu nome? ')
idade = input("Qual a sua idade? ")

idade_limite = 18

if int(idade) < idade_limite:
    print(f'{nome} você tem {idade} anos, idade minima é {idade_limite}!')
else:
    print(f'{nome} sua idade é {idade} anos, você possue a idade minima!!')
