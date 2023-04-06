# Solicita a quantidade de alunos ao professor
quantidade_alunos = int(input("Digite a quantidade de alunos na turma: "))

# Inicializa a lista de notas
notas = []

# Pede ao professor para digitar as notas de cada aluno
for i in range(quantidade_alunos):
    nota = float(input("Digite a nota do aluno {}: ".format(i+1)))
    notas.append(nota)

# Calcula a média da turma
media = sum(notas) / quantidade_alunos

# Exibe a média da turma na tela
print("A média da turma é: {:.2f}".format(media))