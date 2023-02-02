variavel= ['Luiz Silva', 'João', 'Marcos']

for valor in variavel:
    print(valor)
    # continue #Quando usado ele pula para proxima interacao.
    break #Sai para fora do laço no primeiro laço
    print(valor)
    
    
for valor in variavel:
    if valor.lower().startswith('m'):
        print('Começa com M', valor)
    else:
        print('Não começa com M,', valor)
        
