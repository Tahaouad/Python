
tab=[]
tab1=[]
continuer=True

def saisir():
    n=int(input("combien de cases tu peux remplir :"))
    for i in range(n):
        a=int(input("donner les valeur de a : "))
        tab.append(a)
def afficher ():
    print(tab)
def inverser ():
       n=int(input("combien de cases tu peux remplir :"))
       for i in range(n):
            a=int(input("donner les valeur de a: "))
            tab1.append(a)
            rev = tab1[::-1]
       print(rev)   
def repitition ():
      n=int(input("combien de cases tu peux remplir :"))

      for i in range(n):
            a=int(input("donner les valeur de a :"))
            tab.append(a)
      x=int(input("donner la valeur de x :"))
      s=0
      for i in range(n):
          if tab[i]==x:
             s=s+1
      print(s)
def verification():
    n=int(input("combien de cases tu peux remplir :"))
    for i in range(n):
                a=int(input("donner les valeur de a :"))
                while a==0 :
                   print("entrer un autre valeur qui est non null")
                   a=int(input("donner les valeur de a :"))
                   tab.append(a)
def existe():
    n=int(input("combien de cases tu peux remplir :"))
    for i in range(n):
            a=int(input("donner les valeur de a: "))
            tab.append(a)
    p=0
    x=int(input("donner la valeur de x :"))
    for i in range (n):
        if tab[i]==x:
            p=p+1
    if p==0:
            print("l element que vous saisi n existe pas dans le tableau")
    if p==2:
            print("l'element existe en double")
    else :
            print("n'existe pas en double ")
cc=0
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
                saisir()
        elif choix==2:
                afficher()
        elif choix==3:
                inverser()
        elif choix ==4:
                repitition()
        elif choix==5:
                verification()
        elif choix==6:
                existe ()
        elif choix==7:
                continuer =False
        else :
            print("le choix n'existe pas ")


        
            
        
