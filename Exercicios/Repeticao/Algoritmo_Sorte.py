# Algoritmo da Sorte
# Esse exercicio tem como objetivo criar um jogo onde o usuario digita um número inteiro e o sistema verifica se ele está na sequencia de Fibonacci

# Para a sequencia de Fibonacci, o sistema se inicia com 1 e a cada novo numero é a soma dos dois numeros anteriores
# Exemplo: 1,1,2,3,5,8,13 ...


print('    Sequência de Fibonacci')
print('=' * 30)

fibo_anterior = 0
fibo_atual = 1

valor_entrada = int(input('Digite um valor: '))

while fibo_atual <= valor_entrada:

    if fibo_atual == valor_entrada:
        print('Ação bem sucedida, o número digitado faz parte da sequência de Fibonacci')
        break

    # gera o próximo número da sequência
    proximo = fibo_anterior + fibo_atual
    fibo_anterior = fibo_atual
    fibo_atual = proximo

else:
    print('Ação mal sucedida, o número não faz parte da sequência de Fibonacci')