"""
WHILE 
UTILIZAO PAR REALIZAR AÇOES ENQUANTO UMA CONDIÇAO FOR VERDADEIRA

REQUESTOS: Entender condicoes e operadores
"""
# while True: loop infinito
#     nome = input("Qual o seu nome?")
#     print(f'Ola {nome}')

x = 0
while x < 5:

    # if x == 3:
    #     #continue  -- pula o bloco de codigo.
    #     # break - TERMINA O laço.

    print(x)
    x = x + 1  # x +=1

"""
b = 0  # linha
a = 0  # coluna
while a < 10:

    while b < 5:
        print(f'A vale {a} e B vale {b}')
        b += 1
        
    a += 1 
print("Acabou!")
"""

while True:
    print()
    num_1 =input('Digite um número: ')
    num_2 =input('Digite um número: ')
    operador = input('Digite um operador: ')
    sair =input('Deseja sair? [s]im ou [n]ão ')
    
    if sair == 's':
        break
    
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um númer')
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)
    
    # + = / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido')