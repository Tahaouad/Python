sa,sb,sab,pair,impair,p1,p2=0,0,0,0,0,0,0

for i in range (3):
                a=int(input(" joueur 1 doner un nombre entre  0 et 2 :"))
                while a<0 or a>2:
                    a=int(input(" joueur 1 doner un nombre entre  0 et 2 :"))
                sa=sa+a
for j in range (3):
    b=int(input(" joueur 2 donner u nombre entre 0 et 2  :" ))
    while b>2 or b<0:
        b=int(input("joueur  2 donner u nombre entre 0 et 2 : " ))
    sb=sb+b
if sa>sb:
    sab=sa-sb
elif sb>sa:
    sab=sb-sa
else :
    print("nothing")
if sab%2==0:
    pair=1
else :
    impair=1
if pair==1 and impair==0:
        if sa>sb:
            p1=p1+1
            print("player 1 +1pts")
        else:
            p2=p2+1
            print("player 2 +1pts")
if pair==0 and impair==1:
        if sa<sb:
            p1=p1+1
            print("player 1 +1pts")
        else:
            p2=p2+1
            print("player 2 +1pts")
                   
if p1==1:
    print("!PREMIER JOUEUR GAGNE!")
elif p2==1:
    print("!DEUXIEME JOUEUR GAGNE!")
else:
    print("NO WINNER")


















