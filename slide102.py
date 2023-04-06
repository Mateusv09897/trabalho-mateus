# Define as variáveis iniciais
primeiro_termo = 2
razao = 3
soma = 0
termo_atual = primeiro_termo

# Calcula a soma dos termos da PA
while termo_atual <= 100:
    soma += termo_atual
    termo_atual += razao

# Exibe a soma na tela
print("A soma dos elementos da PA é:", soma)