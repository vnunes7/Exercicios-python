# Você deve criar um sistema onde calcule a quantidade de calorias consumidas com base na quantidade de comidas

print('=' * 30)
print('    Calculadora de Calorias')
print('=' * 30)

qtd_comida = int(input('Quantas comidas foram consumidas durante o dia? '))
qtd_calorias = 0
total_calorias = 0
for i in range(1, qtd_comida+1):
    qtd_calorias = int(input(f'Para a {i}º, informe o valor de calorias: '))
    total_calorias = total_calorias + qtd_calorias

if qtd_comida == 1:
    print(f'\nHouve o consumo de {qtd_comida} comida com um total de {total_calorias} calorias.')
elif qtd_comida > 1:
    print(f'\nForam consumidas {qtd_comida} comidas e um total de {total_calorias} calorias.')
elif qtd_comida < 0:
    print(f'\nDados Invalidos!')
else:
    print('\nNão houve consumo de comida até o momento.')


