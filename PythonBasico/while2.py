"""
while / else
contadores
acumuladores
"""

"""
Indices
"""
frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)

contador = 0
nova_string = ''

while contador < tamanho_frase:
    # print(frase[contador], contador)
    letra = frase[contador]
    # nova_string += frase[contador]  # concatena atriuindo a nova string
    # print(nova_string)
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    contador += 1

print(nova_string)
