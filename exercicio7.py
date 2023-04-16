import names.txt

with open('names.txt', 'r') as arquivo:
    nomes = arquivo.read().split()

contador = {}

for nome in nomes:
    if nome in contador:
        contador[nome] += 1
    else:
        contador[nome] = 1

for nome, ocorrencias in contador.items():
    print(f'{nome}: {ocorrencias}')
