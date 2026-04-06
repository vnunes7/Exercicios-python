# O objetivo desse exercicio é realizar um sistema que exiba qual foi a opção mais votada

# Como não estudamos loops ainda, iremos utilizar somente estrutura condicionais

''' Crie um algoritmo que possa digitar  o voto de cada um dos 5 membros da equipe
e ao final, exiba qual foi o console escolhido e com quantos votos '''

print('Gerenciador de votos')

# Criando opções para voto
playstation = 0
xbox = 0
nintendo = 0


# Solicitando entrada de dados
print('Informe o prêmio que deseja receber: ')
print('1. Playstation.')
print('2. XBOX.')
print('3. Nintendo.')

# Armazenando votos registrados e validando votos
func1 = int(input('\nPrimeiro Voto: '))
if func1 == 1:
    playstation += 1
elif func1 == 2:
    xbox += 1
elif func1 == 3:
    nintendo += 1
else:
    print('Opção invalida!')

func2 = int(input('Segundo Voto: '))
if func2 == 1:
    playstation += 1
elif func2 == 2:
    xbox += 1
elif func2 == 3:
    nintendo += 1
else:
    print('Opção invalida!')

func3 = int(input('Terceiro Voto: '))
if func3 == 1:
    playstation += 1
elif func3 == 2:
    xbox += 1
elif func3 == 3:
    nintendo += 1
else:
    print('Opção invalida!')

func4 = int(input('Quarto Voto: '))
if func4 == 1:
    playstation += 1
elif func4 == 2:
    xbox += 1
elif func4 == 3:
    nintendo += 1
else:
    print('Opção invalida!')
func5 = int(input('Quinto Voto: '))
if func5 == 1:
    playstation += 1
elif func5 == 2:
    xbox += 1
elif func5 == 3:
    nintendo += 1
else:
    print('Opção invalida!')

# Verificando premio ganhador
if  playstation > xbox and playstation > nintendo:
    print(f'Parabens! O console escolhido foi o Playstation, com o total de {playstation} votos.')
elif xbox > playstation and xbox > nintendo:
    print(f'Parabéns! O console escolhido foi o XBOX, com o total de {xbox} votos.')
elif nintendo > playstation and nintendo > xbox:
    print(f'Parabéns! O console escolhido foi o Nintendo, com o total de {nintendo} votos.')
else:
    print('Ocorreu um empate, tente novamente.')


