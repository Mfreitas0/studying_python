"""
OPERADORES LOGICOS
 AND, OR, NOT
 IN e NOT IN
"""
#-------------------------------------------------
#(verdadeiro E falso) = FALSO --PRECISA QUE AMBAS AS ALTENATIVAS ESTEJAM VRDD
""""comparacao1 and comparacao"""

#--------------------------------------------------
# (verdadeiro OU verdadeiro) -- PRECISA QUE APENAS UMA ALTENATIVA ESTEJA VRDD
""""comp1 or comp2"""

#---------------------------------------------------
#NOT - É A INVERSA DA AFIMAÇÃO FEITA - NÃO É ex: not b > a (b=3, a=5)

#----------------------------------------
#IN - sabe se um dados esta presente em uma variaveis etc...
#EX:
nome= "Marcos Freitas"

if 'i' in nome:
    print("Existe a letra i no seu nome")
else:
    print("Não existe")
    
#---------------------------------------------------------------
#NOT IN -- inversao de in