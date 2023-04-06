# Solicita o valor do ângulo em graus
angulo = float(input("Digite o valor do ângulo em graus: "))

# Calcula o valor do ângulo em radianos
angulo_rad = angulo * (3.14159 / 180)

# Determina o quadrante do ângulo
if angulo_rad >= 0 and angulo_rad < (3.14159 / 2):
    print("O ângulo está no primeiro quadrante.")
elif angulo_rad >= (3.14159 / 2) and angulo_rad < 3.14159:
    print("O ângulo está no segundo quadrante.")
elif angulo_rad >= -3.14159 and angulo_rad < (-3.14159 / 2):
    print("O ângulo está no terceiro quadrante.")
elif angulo_rad >= (-3.14159 / 2) and angulo_rad < 0:
    print("O ângulo está no quarto quadrante.")
elif angulo_rad == 0 or angulo_rad == 3.14159:
    print("O ângulo está sobre o eixo x.")
elif angulo_rad == (3.14159 / 2) or angulo_rad == (-3.14159 / 2):
    print("O ângulo está sobre o eixo y.")