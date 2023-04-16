import random

# gera um número aleatório entre 1 e 9
numero_aleatorio = random.randint(1, 9)

# solicita que o usuário adivinhe o número
tentativa = int(input("Adivinhe um número entre 1 e 9: "))

# verifica se a tentativa é menor, maior ou igual ao número aleatório
if tentativa < numero_aleatorio:
    print("Tentativa menor do que o número aleatório.")
elif tentativa > numero_aleatorio:
    print("Tentativa maior do que o número aleatório.")
else:
    print("Parabéns! Você acertou o número")
