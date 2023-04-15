import random

while True:
    print("Jogo de Pedra, Papel e Tesoura")
    print("Escolha uma opção: ")
    print("1 para Pedra")
    print("2 para Papel")
    print("3 para Tesoura")

    player1 = int(input("Jogador 1: "))
    player2 = int(input("Jogador 2: "))

    while player1 not in [1, 2, 3] or player2 not in [1, 2, 3]:
        print("Jogada inválida. Tente novamente.")
        player1 = int(input("Jogador 1: "))
        player2 = int(input("Jogador 2: "))

    if player1 == player2:
        print("Empate!")
    elif player1 == 1 and player2 == 3 or player1 == 2 and player2 == 1 or player1 == 3 and player2 == 2:
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")

    continuar = input("Deseja continuar jogando? (s/n) ")

    if continuar.lower() != "s":
        break

print("Obrigado por jogar!")
