def remove_duplicatas(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

lista = [1, 2, 3, 2, 4, 3, 5]
nova_lista = remove_duplicatas(lista)
print(nova_lista)  # [1, 2, 3, 4, 5]

