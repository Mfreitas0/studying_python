"""
LIST
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

#         1    2    3    4    5
lista = ['A', 'B', 'C', 'D', 'E']
#    -    5    4    3    2    1

# fatiamento [0:3:1] 0-INICIO/3-FIM/1-PASSO A PASSO.
print(f'FATIAMENTO')
print(lista[0:3])
print(lista[:3:1])
print(lista[0:3:2])
print(lista[::2])

print()

# EXTEND -Uma forma de mescla lists (concatenacao)
print('EXTEND')
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)

print(f'l1 {l1}')
print(f'l2 {l2}')

print()

# APPEND -inseri um novo valor no final da list
print('APPEND')
l2.append('b')
print(f'l2 {l2}')
print()

# INSERT - Adciona um novo item em qualquer posicao(indixe) que vc deseja
print('INSERT')
l2.insert(0, 'banana')

print(f'l2 {l2}')
print()

# POP -deleta o ultimo valor da list
print("POP")
print(f'l2={l2}')
l2.pop()
print(f'l2 apos o pop() = {l2}')
print()

# DEL - Pode escolher uma fatia da list e deleta-la
print('Del')
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del (lista[3:5])
print(f'O novo valor de lista é: {lista}')
print()
lista.insert(0, 'banana')
print(lista)
del (lista[0])
print(f'Novo valor apos deletar somente um valor: {lista}')
print()

# MAX, MIN -Retorna o maior e menor valor da lista
print('Max, Min')

print(max(lista))
print(f'O Maior vaLor: {max(lista)}')
print(f'O Menor vaLor: {min(lista)}')
print()

# VARRED DE ELEMENTO
print('VARREDURA DE ELEMENTO')

lista2 = ['String', True, 10, -1.2]

for elem in lista2:
    print(f'O tipo do elem é {type(elem)} e seu valor é {elem}')

# JOGO DA FORCA
secreta = 'perfume'
digitadas = []
chances = 3

while True:
    if chances < 1:
        print(f'ACABARAM SUAS CHANCES!!!')
        break

    letra = input('Digite uma Letra: ')

    if len(letra) > 1:
        print('Opa! Digite apenas uma LETRA.')

    digitadas.append(letra)

    if letra in secreta:
        print(f'ISSO AI! a letra {letra} pertence a palavra secreta.')
    else:
        print(f'TRISTE, a letra "{letra}", NÃO EXISTE na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreta:
        print(
            f'Parabens, VOCÊ GANHOU, a palavra secreta era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')

    if letra not in secreta:
        chances -= 1

    print(f'Você tem {chances} chances.')