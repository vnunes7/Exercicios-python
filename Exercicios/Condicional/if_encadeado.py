# Sistema para calcular Bhaskara
# Primeiro solicite os valores de A, B e C

import math

a = float(input('Digite o valor para A: '))
b = float(input('Digite o valor para B: '))
c = float(input('Digite o valor para C: '))

delta = b ** 2 - 4 * a * c

if delta > 0:
    #Caso delta for positivo
    x1 = -b + math.sqrt(delta) / 2 * a
    x2 = -b - math.sqrt(delta) / 2 * a
    print(f'\nPara a equação {a}x² + {b}x + {c} = 0, obtivemos os seguintes valores: \nX1 = {x1:.2f} e X2 = {x2:.2f}')
    print(f'\nValor Delta {delta}')
elif delta == 0:
    #Caso delta for zero:

    x = (-b + math.sqrt(delta)) / (2 * a)
    print(f'\nPara a equação {a}x² + {b}x + {c} = 0, obtivemos os seguinte valor: \nX = {x:.2f}')
    print(f'\nValor Delta {delta}')
else:
    print(f'Para a equação {a}x² + {b}x + {c} = 0, não existem valores reais para X')


