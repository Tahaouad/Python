s,min,max,p,sa,faux=0,10,0,0,0,False
n=int(input("donner la valeur de n  :"))
for i in range(n) :
    a=int(input("donner la valeur de a  : "))
    while a<1 or a>10:
        print("donner un nombre entre 1 et 10")
        a=int(input("donner la valeur de a  :"))
    s=s+1/a
    if a>max :
            max=a
    if a<min :
            min=a
    if a==2 :
        p=p+1
    else :
        for j in range(2,a-1):
            if a%j==0:
                faux=True
        if faux==False :
            p=p+1
    sa=sa+a
    s=s+1/a
M=sa/n
print("1:Somme des inverses\n2:Minimum\n3:Maximum\n4:les nombres premires\n5:le moyen ")
choix=int(input("Sélectionner un choix\n"))
for i in range (6):
    match (choix):
     case 1: print("la somme des inverses des entiers est :",s) 
     case 2: print("le minimum est  :",min)
     case 3: print("le maximum est :",max)
     case 4: print(" le nombre des nomnres premiers est :",p)
     case 5: print("le moyen est : ",M)
     case _: print("choix indisponible")
    choix=int(input("Sélectionner un choix\n"))
