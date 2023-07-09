#!/usr/bin/env python
grillevide=[[".",".","."] for i in range(3)]
#print(grillevide)

victoire=False
victoryx=["X" for i in range(3)]
victoryy=["O" for i in range(3)]

def grille(grille):
    '''print la grille'''
    for i in range(3):
        print(grille[i])
    #return "lignes=1,2 ou 3 et colonnes=1,2 ou 3"
#print(grille(grillevide))
'''Afiche la grille'''

def verifsolution(grille):
    '''Renvoi True is la grille est Gagnante sinon False'''
    listcond=[]
    #1
    for i in grille:
        if i==victoryx or i==victoryy:
            return(True)
    #2
    pos=0
    for i in range(3):
        for liste in grille:
            listcond+=liste[pos]
        if listcond==victoryx or listcond==victoryy:
            listcond=[]
            return(True)
        pos+=1
        listcond=[]
    pos=0
    #3
    listcond=[]
    for i in range(1):
        for liste in grille:
            listcond+=liste[pos]
            pos+=1
        if listcond==victoryx or listcond==victoryy:
            listcond=[]
            return(True)
    listcond=[]
    pos=2
    for i in range(1):
        for liste in grille:
            listcond+=liste[pos]
            pos-=1
        if listcond==victoryx or listcond==victoryy:
            listcond=[]
            return(True)
    return(False)
'''Retourne si il y a victoire'''
defi=dict(tour=1,j=1,joueur=1)
# tour=1
# j=1
# joueur=int

def turn(tour,j,joueur):
    '''Recois ligne et colone xy renovoi xy'''
    print("\nC'est au tour du Joueur",joueur,"[tour",tour,"]")
    grille(grillevide)#print la grille
    j=j*-1
    defi["j"]=j
    if j==1:
        joueur=1
        defi["joueur"]=joueur
    else:
        joueur=2
        defi["joueur"]=joueur
    if IA==1 and defi["joueur"]==1:
        futur=couppossible()
    elif IA==2 and defi["joueur"]==1:
        futur=coupexpert(grillevide)
    else:    
        futur=input("Rentrer numero de ligne ET colonne ensemble(EX:32)\n")
    #print(IA)
    turfu=list(futur)
    pos1=int(turfu[0])-1
    pos2=int(turfu[1])-1
    #print("grille vide",grillevide)
    while len(futur)!=2 or int(futur)<10 or int(futur)>34 or grillevide[pos1][pos2]!=".":
        if len(futur)!=2:
            print("ERREUR taille de 2 chiffre")
        if int(futur)<10:
            print("superieur a 10")
        if int(futur)>34:
            print("inferieur a 34(strictement)")
        if grillevide[pos1][pos2]!=".":
            print("utlisez un espace qui n'est pas deja assigne")
        #futur=input("Rentrer numero de ligne ET colonne ensemble(EX:33)\n")
        futur=input()
        turfu=list(futur)
        pos1=int(turfu[0])-1
        pos2=int(turfu[1])-1
        grille(grillevide)#print la grille
    #print(futur)
    listcoupspossibles.remove(int(futur))
    tour+=1
    defi["tour"]=tour
    #print(joueur)
    return futur
'''Afiche le tour et la grille pour les joueurs et Retourne le coup'''
#turn(**defi)
#turn(**defi)
#turn(**defi)
#turn(tour,j,joueur)
#turn(tour,j,joueur)
#print(grille(grillevide))
#faut dict

def applygrille(grille,assignation,joueur):
    #joueur=joueur*-1
    if joueur==1:
        signe="X"
    else:
        signe="O"
    #joueur=joueur*-1
    ass=list(assignation)
    ligne=int(ass[0])-1
    colonne=int(ass[1])-1
    #for i in grille[ligne]:
    #    i[colonne]=signe
    grille[ligne][colonne]=signe
    return(grille)
'''Retourne le grille avec le coup fait'''

L=list(range(10,34)) ; L=[i for i in L if i%5] ; L=[i for i in L if not i%10 in [4,5,6,7,8,9]]
listcoupspossibles=L

def couppossible():
    import random
    retour=random.choice(listcoupspossibles)
    return str(retour)
'''retourne un coup au hasard'''
def coupexpert(grille):
    import copy
    for i in listcoupspossibles:
        echo=copy.deepcopy(grille)
        choix=str(i)
        echo=applygrille(echo,choix,defi["joueur"])
        #print("c'est echo\t\t",echo)
        #print("c'est grillevide\t",grillevide)
        if verifsolution(echo)==True:
            #print("////////",choix)
            return choix
        echo=[]
    for i in listcoupspossibles:
        echo=copy.deepcopy(grille)
        choix=str(i)
        ogjoueur=defi["joueur"]
        defi["joueur"]=42
        echo=applygrille(echo,choix,defi["joueur"])
        defi["joueur"]=ogjoueur
        if verifsolution(echo)==True:
            return choix
        echo=[]
    echo=copy.deepcopy(grille)
    if echo[1][1]==".":
        return "22"
    return couppossible()


#MAIN
IA=int(input("Wellcome press:\n0 Pour du Pvp\n1 Pour un ordi\n2 Pour un niveau EXPERT\nChoix:"))
while IA not in [0,1,2]:
    IA=int(input("Entre 0 et 2 .....\nChoix:"))
#IA=2
grillevide=applygrille(grillevide,turn(**defi),defi["joueur"])
while not(verifsolution(grillevide)) and not(defi["tour"]==10):
    grillevide=applygrille(grillevide,turn(**defi),defi["joueur"])


if defi["joueur"]==1:
    defi["joueur"]=2
else:
    defi["joueur"]=1
print("\n\n")
if not(verifsolution(grillevide)):
    grille(grillevide)#print la grille
    print("Egalite Peronne n'as perdu")
else:
    if defi["joueur"]!=1:
        defi["joueur"]="IA"
    grille(grillevide)#print la grille
    print("Fin du jeu joueur",defi["joueur"],"a gagne")
