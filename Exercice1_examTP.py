NB_Jours = [31,28,31,30,31,30,31,31,30,31,30,31]
Mois = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
obs1 = [12,2,20]
obs2 = [12,10,20]

def Mois_Jours(Mois , NB_Jours):
    dict = {}
    for mois , jour in zip(Mois , NB_Jours):
        dict[mois] = jour
    return dict



def Ordre_Mois(Mois ):
    dict = {}
    for mois  in Mois :
        dict[mois] = Mois.index(mois) +1
    return dict





def valide(obs):
    if obs[1] > 12 or obs[1] < 1:
        return False
    if  obs[0] < 1:
        return False
    for month in Ordre_Mois(Mois):
       if (Ordre_Mois(Mois)[month] == obs[1]) and  (Mois_Jours(Mois , NB_Jours)[month] < obs[0]):
          return False
    return True



def num_jour(obs):
    if valide(obs):
        return sum(NB_Jours[0:obs[1]-1]) + obs[0]
    else:
        return -1
    


def avant(obs1,obs2):
    if num_jour(obs1) < num_jour(obs2):
        return True
    return False



def main():


    print(Mois_Jours(Mois , NB_Jours))
    print(Ordre_Mois(Mois))
    print(valide(obs1))
    print(num_jour(obs1))
    print(avant(obs1,obs2))



if __name__ == "__main__":
    main()


