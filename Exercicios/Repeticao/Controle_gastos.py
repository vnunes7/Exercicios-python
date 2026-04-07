# Este exercicio tem como objetivo criar um sistema de controle de gastos

# O usuário deve digitar a quantidade de transações e o valor de cada uma
# O sistema precisa retornar o valor total gasto pelo usuário e o valor médio

print('-' * 30)
print('       Gestão de Gastos')
print('-' * 30)

qtd_transacoes = int(input('Informe a quantidade de compras realizadas no dia: '))
valor_gasto = 0
total_gasto = 0

for i in range(1, qtd_transacoes+1):
    valor_gasto = float(input(f'Informe o valor da {i}º compra R$ '))
    total_gasto += valor_gasto


if qtd_transacoes == 1:
    media_gastos = total_gasto / qtd_transacoes
    print(f'Hoje ocorreu apenas uma compra no valor de R$ {total_gasto:.2f}, com o valor médio de R$ {media_gastos:.2f}')
elif qtd_transacoes > 1:
    media_gastos = total_gasto / qtd_transacoes
    print(f'Hoje ocorreu {qtd_transacoes} compras no valor total de R$ {total_gasto:.2f}, com o valor médio de R$ {media_gastos:.2f}')
elif qtd_transacoes == 0:
    print('Hoje não ocorreu nenhuma compra!')
else:
    print('Valor Invalido!')