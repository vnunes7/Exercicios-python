# COM QUE ROUPA EU VOU ?
# UMA LOJA QUE VENDE ROUPA PERSONALIZADA DISPONIBILIZOU NO MÊS DO SEU ANIVERSÁRIO
# O CUPOM NIVER10, QUE CONCEDE 10% DE DESCONTO NO VALOR TOTAL DE UMA COMPRA FEITA NO SITE

# CASO O CUPOM TENHA SIDO DIGITADO CORRETAMENTE, DEVERÁ SER INFORMADO DO VALOR FINAL
# COM O DESCONTO APLICADO, CASO DIGITE DE FORMA INCORRETA DEVERÁ SER INFORMADO
# O VALOR DA COMPRA SEM DESCONTO

# UTILIZE UM IF COMPOSTO


# ----------------------


print('COM QUE ROUPA EU VOU? \n')

valor_compra = float(input('Informe o valor da compra realizada: '))
cupom_desconto = input('Informe o cupom de desconto: ')
valor_final = valor_compra * 0.90

if cupom_desconto.upper() == 'NIVER10':
    print(f'Cupom resgatado com sucesso, valor final da compra {valor_final:.1f}.')
else:
    print(f'Cupom "{cupom_desconto.upper()}" invalido.')
