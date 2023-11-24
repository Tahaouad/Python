tab=[]
r=0
tab1=[]
d=0
continuer=True
def remplire():  
    n=int(input("entrez le nombre du cases: "))
    for i in range (n):
      a=int(input("entrez la valeur du a: "))
      tab.append(a)
def afficher():
    remplire()
    print(tab)
def inverse():
    
    n=int(input("combien de cases tu peux remplir :"))
    for i in range (n):
       a=int(input("entrez la valeur du a: "))
       tab1.append(a)
       rev = tab1[::-1]
    print(rev)
def repeter():
    remplire()
    n=int(input("combien de cases tu peux remplir :"))
    for i in range (n,1):
        p=int(input("entrez un valeur: "))
        if tab[i]==p:
            r=r+1
        print (r)
def valeur_null():
    
    n=int(input("entrez le nombre du cases: "))
    for i in range (n):
        a=int(input("donner les valeur de a :"))
        while a==0 :
                print("entrer un autre valeur qui est non null")
                a=int(input("donner les valeur de a :"))
                tab.append(a)
    
def double():
    remplire()
    n=int(input("entrez le nombre du cases: "))
    for i in range (n):
        if tab[i]<=2:
            d=d+1
        if d==2:
            print(n,"nexist pas en double")
while (continuer ):
        print("1-saisir un tsbleau ")
        print("2-afficher un tableau")
        print("3-inverser un tableau ")
        print("4-calculer le nombre de repetition d un element dans une tableau ")
        print("5-verifier si un tableau ne contient que des valeurs non null ")
        print("6-verifier si un element existe en double dans une tableau ")
        print("7-pour arreter le programe tapez 7")
        
        choix=int(input("saisir votre choix "))
        if choix==1:
                remplire()
        elif choix==2:
                afficher()
        elif choix==3:
                inverse()
        elif choix ==4:
                repeter()
        elif choix==5:
                valeur_null()
        elif choix==6:
                double ()
        elif choix==7:
                continuer =False
        else :
            print("le choix n'existe pas ")
        
