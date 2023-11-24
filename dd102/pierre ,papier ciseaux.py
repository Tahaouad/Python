from random import randint
pj=0
po=0
eg=0
continuer=True
jeu = ["pierre","papier","ciseaux"]
ordinateur=jeu[randint(0,2)] 
while (continuer ):
    joueur = input("pierre , papier ,ciseaux ? ou taper fin pour arreter le jeu!\n")
    if (joueur=='fin'):
        continuer = False 
    elif (joueur == ordinateur ):
        eg=eg+1
        print("Egalité")
    elif (joueur =="pierre"):
        if(ordinateur =="papier"):
            print("perdu!",ordinateur,"recouvre",joueur )
            po=po+1
        else :
            print("gagné",joueur,"écrase",ordinateur)
            pj=pj+1
    elif (joueur =="papier"):
        if(ordinateur== "ciseaux"):
            print("perdu!",ordinateur,"cut",joueur )
            po=po+1
        else:
            print("you win!",joueur,"recouvre",ordinateur)
            pj=pj+1
    elif(joueur=="ciseaux"):
        if (ordinateur== "pierre"):
            print("perdu...",ordinateur,"écrase",joueur)
            po=po+1
        else:
            print("gagné",joueur,"cut",ordinateur )
            pj=pj+1
    else:
        print("votre choix n'est pas correct, vérifier l'ortographe !")
    ordinateur=jeu[randint(0,2)]
    print("*****Tour suivant*****")
print("*****points*****")
print("joueur",pj)
print("ordinateur :",po)
