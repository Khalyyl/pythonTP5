def differences(L):
    M=[]
    for i in range(1,len(L)):
        difference= L[i]-L[i-1]
        M.append(difference)
    print(M)

def itere(L,n):
    result = L
    for _ in range(n):
        result = differences(result)
    return result

liste_reels = [1.0, 2.5, 4.8, 7.2, 11.0]
resultat_itere_1 = itere(liste_reels, 1)
resultat_itere_2 = itere(liste_reels, 2)

print("itere(L, 1) =", resultat_itere_1)
print("itere(L, 2) =", resultat_itere_2)