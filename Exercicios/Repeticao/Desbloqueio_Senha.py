# O objetivo deste exercicio é desbloquear o sistema após o usuário digitar a senha e o fatorial do minutal atual

# Ao analisar o código do programa, descobrimos que a senha é composta pela palavra "LIBERDADE" seguida do fatorial dos minutos que a máquina estiver marcando no momento da digitação da senha

# Se a maquina estiver marcando 5 minutos a senha será LIBERDADE120.
# Crie um programa que receba do usuário os minutos atuais e exiba na tela a senha necessária para desbloqueio

print('***** DESCRIPTOGRAFIA DE SENHA *****')

minutos = int(input("Informe o número dos minutos do horario atual"))
fatorial = minutos

for numero in range(1,minutos):
    fatorial = fatorial * numero

print(f'A senha para desbloqueio é: LIBERDADE{fatorial}')