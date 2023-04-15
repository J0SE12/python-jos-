while True: OK
    palavra = input("Digite uma palavra: ").lower()
    if palavra == palavra[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")

    continuar = input("Deseja digitar outra palavra? (s/n) ")
    if continuar.lower() != "s":
        break

