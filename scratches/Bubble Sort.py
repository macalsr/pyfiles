lista = [4, 1, 3, 5, 2]
n = len(lista)  # pegar comprimento da lista

# percorrer todos os elementos da lista

for i in range(n):

    for j in range(n - i - 1):
    # se o elemento da esquerda for maior
    # que o elemento a direita
        if lista[j] > lista[j + 1]:

            # realiza a troca com o
            # auxilio da variavel 'aux'
            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux

print(lista)  # saida [1,2,3,4,5]
