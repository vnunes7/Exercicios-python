# O objetivo deste Exercicio é validar o desconto progressivo.
# Uma companhia area está ofertando descontos progressivos na compra de pacotes.
# Você deve criar um algoritmo que receba o valor bruto do pacote, categoria dos assentos e quantidade de pessoas

# O sistema deverá exbir Valor Bruto da Viagem, Valor de Desconto, Valor Liquido da Viagem, Valor Médio por Viajante

# Tabela:
# Economica: 2 Vianjantes - 3% | 3 Viajantes - 4% | 4 ou mais 5%
# Executiva: 2 Vianjantes - 5% | 3 Viajantes - 7% | 4 ou mais 8%
# Primeira Classe: 2 Vianjantes - 10% | 3 Viajantes - 15% | 4 ou mais 20%



print("Calculadora de Descontos Progressivo\n")
#Solicitando e guardando a Categoria
print('Informe a categoria do assento:')
print('1. Economica')
print('2. Executiva')
print('3. Primeira Classe')
categoria = int(input('R: '))

#Solicitando e guardando valor do pacote
valor_bruto = float(input('Informe o valor do pacote: '))

#Solicitando e guardando a quantidade de pessoas
qtd_pessoas = int(input('Informe a quantidade de pessoas: '))

valor_desconto = 0

# Validando categoria digitada e quantidade de pessoas
if categoria == 1:
    if qtd_pessoas == 2:
        valor_desconto = valor_bruto * 0.03
    elif qtd_pessoas == 3:
        valor_desconto = valor_bruto * 0.04
    elif qtd_pessoas >= 4:
        valor_desconto = valor_bruto * 0.05
elif categoria == 2:
    if qtd_pessoas == 2:
        valor_desconto = valor_bruto * 0.05
    elif qtd_pessoas == 3:
        valor_desconto = valor_bruto * 0.07
    elif qtd_pessoas >= 4:
        valor_desconto = valor_bruto * 0.08
elif categoria == 3:
    if qtd_pessoas == 2:
        valor_bruto = valor_bruto * 0.1
    elif qtd_pessoas == 3:
        valor_desconto = valor_bruto * 0.15
    elif qtd_pessoas >= 4:
        valor_desconto = valor_bruto * 0.2
else:
    print('Categoria invalida!')

# Realizando calculo de valor liquido e valor médio
valor_liquido = valor_bruto - valor_desconto
valor_medio = valor_bruto / qtd_pessoas

print(f'\nO valor da bruto da viagem é R${valor_bruto:.2f}, houve um desconto de R${valor_desconto:.2f}.\nApós o desconto o valor liquido é de R${valor_liquido:.2f}. e o preço medio por vianjante é R${valor_medio:.2f}.')
