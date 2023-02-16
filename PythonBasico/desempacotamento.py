""""
DESEMPACOTAMENTO DE LIT
"""

lista = ["luis", "Joao", "Maria", 1, 2, 3]
# DESEMPACOTA CADA VALOR EM CADA VARIAVEL

n1, n2, *restantes_daLista = lista# PODE ADCIONAR MAIS UMA VARIAVEL QUE RECEBERA SOMENTE O ULTIMO VALOR.
# restante_daLista RECEBE TODOS OS VALORES E GUARDA EM LISTA.


print(n1, n2, restantes_daLista)
