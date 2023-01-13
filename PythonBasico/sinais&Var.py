"""
+ - CONCATENAÇÃO
** - POTENCIAÇÃO
% - RESTO DIVISAO
"""

#VARIAVEIS  

nome = 'Marcos Freitas'
idade = 23 #int
altura =1.60 #float
e_maior = idade > 18 #bool
peso = 69
data = 2022

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('E maior:', e_maior)
print(idade + altura)
 
imc = peso / altura ** 2

#PRINTs
print('Oi ',nome,'Seu IMC é: ', imc)#OPCAO DE PREENCIMENO NO PRINTS
print(f'Oi {nome} seu IMC é {imc:.2f}') #OPCAO DE PREENCIMENO NO PRINT
print('Oi {} seu IMC é {:.2f}\n'.format(nome,imc))#OPCAO DE PREENCIMENO NO PRINT

#TESTIZINHO
data_nascimento = data - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}Kg')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {data_nascimento}.')