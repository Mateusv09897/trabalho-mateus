# Cria uma matriz vazia de 3x3
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Pede ao usuário para digitar os valores da matriz
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input("Digite o valor da posição [{}, {}]: ".format(i, j)))

# Calcula a soma da diagonal principal
soma_diagonal = 0
for i in range(3):
    soma_diagonal += matriz[i][i]

# Exibe a soma da diagonal principal na tela
print("A soma da diagonal principal é:", soma_diagonal)