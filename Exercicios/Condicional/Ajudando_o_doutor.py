# O Doutor Henry informou que todos alunos que obtiverem uma nota
# maior do que 8.5 na prova semestral serão convidados para uma visita de campo

# O programa deve solicitar o e-mail e a nota do aluno, exibindo a mensagem
# "ENVIANDO CONVITE" caso a nota do aluno satisfaça a condição proposta

# Utilize um if simples

# ------------------------------------

# Exercicio

print('------- AJUDANDO O DOUTOR -------')

email = input('Digite o seu e-mail, por gentileza: ')
nota = float(input('Digite a nota da prova semestra: '))

if nota >= 8.5:
    print(F'\nENVIANDO CONVITE PARA O E-MAIL: {email.upper()}')


