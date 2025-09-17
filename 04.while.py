# crie um codigo que faca a conversao de moeda do real para dolar e vice-versa 

# estapas da resolucao:
# 1) criar uma variavel chamada cotacao
# 2) solicitar ao ususario a opcao de conversao desejada
# 3) apresentar o resultado da conversao de moeda 
# 4) perguntar se ele deseja continuar a conversao 


letra = 's'
while letra == 's':
    cotacao = float(input('digite a cotacao do dolar: '))
    print('-'*50)
    print(f'-'*15,'escolha a opcao','-'*15)
    print('-'*50)

    opcao = int(input('1 - converter dolar para real 2- converter real para dolar: '))

    if opcao == 1:
        valor = float(input('digite o valor em dolar a ser convetido por real U$: '))
        resultado = valor * cotacao 
        print(f'o valor em reais e : {resultado}')
    else:
        print("digite sua opcao valida")
    letra = input("deseja continuar? (s/n): ").lower()