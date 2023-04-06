# Solicita as notas das duas provas e do trabalho
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
trabalho = float(input("Digite a nota do trabalho: "))

# Calcula a média final com base nas notas das provas e do trabalho
media_final = (0.7 * (nota1 + nota2) / 2) + (0.3 * trabalho)

# Exibe a média final na tela
print("A média final é:", media_final)