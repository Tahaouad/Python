#n=int(input())
s,max,min=0,0,10
#for i in range (n):
a=int(input("donner  a\n"))
while True:
    while a < 1 or a >10 :
            print("donner une valeur entre 1 et 10 " )
            a=int(input())
    print("vouler vous continuer oui/non")
    r=str(input())
    if r=='oui' :
             a=int(input("donner  a\n"))
    else :
             break
    
    if a>max :
         max=a
    if a<min :
        min=a
    
    s=s+1/a
print("Sélectionner un choix")
print("1:Somme des inverses\n2:Minimum\n3:Maximum")
choix=int(input())
match (choix):
     case 1: print("la somme des inverses des entiers est :",s) 
     case 2: print("le minimum est  :",min)
     case 3: print("le maximum est :",max)
     case _: print("choix indisponible")
