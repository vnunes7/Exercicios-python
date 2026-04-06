# Utilizando o Loop For para realizar média de pesos

caixas = 0
caixasoma = 0
for i in range(1,6):
    caixas = int(input(f'Informe o peso da caixa {i}: '))
    caixasoma = caixasoma + caixas


print(f'{caixasoma}kg de caixas, {i}')
media = caixasoma/i
print(f'O peso médio é de: {media:.1f}kg')
