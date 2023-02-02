# EXERCICIO PAR E IMPAR, PEDI UM NUMERO E INFORMA SE O NUMERO É PAR OU IMPAR
num = input("Digite um numero inteiro: ")

if num.isdigit():
    restoDiv = int(num) % 2

    if restoDiv == 0:
        print(f'O numero {num} que Você digitou é PAR!')
    else:
        print(f'O numero {num} que Você digitou é ÍMPAR!')

else:
    print("ERRO! Isso não é um número inteiro")
