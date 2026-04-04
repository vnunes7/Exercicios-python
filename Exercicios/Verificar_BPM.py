# Exercicio: Verificar idade e BPM, e retornar se está na faixa adequada.
# Idade BPM
# Até 2 anos 120 a 140
# De 8 anos até 17 anos 80 a 100
# Adulto sedentário 70 a 80
# Idosos 50 a 60


print('VERIFICADOR DE BADIMENTOS CARDÍACOS\n'
      '')
idade = int(input('Informe sua idade: '))
bpm = int(input('Informe seu Batimento Cardiaco por Minuto: '))


if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print('Batimentos Cardiacos adequado')
    else:
        print('Batimentos Cardíacos inadequeado para idade fornecida.')
elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print('Batimentos Cardiacos adequado')
    else:
        print('Batimentos Cardíacos inadequeado para idade fornecida.')
elif idade >= 18 and idade < 60:
    if bpm >= 70 and bpm <= 80:
        print('Batimentos Cardiacos adequado')
    else:
        print('Batimentos Cardíacos inadequeado para idade fornecida.')
elif idade >= 60:
    if bpm >= 50 and bpm <= 60:
        print('Batimentos Cardiacos adequado')
    else:
        print('Batimentos Cardíacos inadequeado para idade fornecida.')
else:
    print('Não foi possível verificar o BPM para a idade fornecida.')
