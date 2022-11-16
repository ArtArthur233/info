"morpion"
#- fInitialiserPlateau()
#- fAfficherPlateau(pPlat)
#- fJouer(pPlat,pJoueur,pLig,pCol) -> True/False + plateau
#- fGagné(pPlat,pJoueur)->true/false ou fGagne(pPlat)->'X'/'O'/'N'
#- fJeu()

 
from unittest import result


pieces = {0: " ", 1: "X", 2: "O"}
tour = 1

def fIniPlateau():
    return [[0,0,0],[0,0,0],[0,0,0]]

def fAfficherPlateau(P,x):
    print('-------------')
    for i in range(x):
        for j in range(x):
            print( "| " + pieces[P[i][j]], end=' ')
        print("|")
        print('-------------')

def fJouer(pPlateau, pJoueur, pLig, pCol):
    if (pLig <= 2 and pCol <= 2):
        if pPlateau[pLig][pCol] == 0: 
            if pJoueur == 1:
                pPlateau[pLig][pCol] = 1
                return(2)
            else:
                pPlateau[pLig][pCol] = 2
                return(1)
        else:
            print("Case non disponible")
            return(0)
    else:
        print("Hors limite")
        return(0)

plateau = fIniPlateau()
    

while True:

    fAfficherPlateau(plateau, 3)
    colonne = int(input("colonne: ")) - 1
    ligne = int(input("ligne: ")) - 1

    result = fJouer(plateau, tour, ligne, colonne)
   
    if result == 0:
        print("erreur")
    else:
        tour = result






