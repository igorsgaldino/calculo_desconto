print('Qual fruta deseja comprar?')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')

produto = int(input('Qual sua escolha?'))
qtd = int(input('Qual a quantidade?'))

if (produto == 1):
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} maçãs. O valor total a pagar: {pagar}')
else:
    if (produto == 2):
        pagar = qtd * 3.6
        print(f'Você comprou {qtd} laranjas. O valor total a pagar: {pagar}')   
    else:

        if (produto == 3):
            pagar = qtd * 1.85
            print(f'Você comprou {qtd} maçãs. O valor total a pagar: {pagar}')
        else:
            print('Produto inexistente!')