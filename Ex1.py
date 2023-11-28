from random import randint

def listAleaInt(n, a, b):
    return [randint(a, b) for i in range(n)]

ma_liste = listAleaInt(10, 1, 100)
print("Liste Avant",ma_liste)
index_minimum = ma_liste.index(min(ma_liste))
print("Indice de la valeur minimal est ",index_minimum)
ma_liste[0], ma_liste[index_minimum] = ma_liste[index_minimum], ma_liste[0]
print("Liste Après :", ma_liste)

