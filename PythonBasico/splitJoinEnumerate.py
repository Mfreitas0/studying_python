"""
Split, join, Enumerate
*Split - Dividir uma string #str
*Join - Juntar uma lista #str
*Enumrate - Enumera elemntos da lista #list / interaveis
"""

string = 'Po Brasil é o país do futebool, O Brasil é penta'
print('SPLIT')
# TRANFORMA A STRING EM UMA LISTA, COM CADA PALAVRA COMO UM VALOR.
lista_1 = string.split(' ')
# TRANFORMA A STRING EM UMA LISTA, UM VALOR A CADA VIRGULA.
lista_2 = string.split(',')

palavra = ' '
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A plavra que apareceu mais vezes é {palavra}')
print()

# JOIN -  NORMALMENTE USADA PARA TRANSFORMAR UMA LIST EM UMA STRING
print('JOIN')
frase = 'O Brasil é penta.'
lista_3 = frase.split(' ')

string2 = ','.join(lista_3)

print(frase)
print(lista_3)
print(string2)
print()


# ENUMERATE
print('ENUMERATE')

outraLista = [
    [1, 2],
    [3, 4],
    [5, 6],
]

for v in enumerate(outraLista):
    print(v)
    

listaIndice = [
    [0, 'Marcos'],
    [1,'Maria'],
    [2,'Macarrão']
]
    
for indice, valor in listaIndice: #É EXATAMENTE OQUE A FUNCAO ENUMERATE FAZ
    print(indice, valor)
print('enumurete() = Desempacotamento de valores')