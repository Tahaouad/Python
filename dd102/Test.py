def somme(a,b):
    s=a+b
    return s
def division(a,b):
    d=a/b
    return d
a=int(input("donnez a"))
b=int(input("donnez b"))
print("1-somme\n2-division")
menu=int(input("choisir 1 ou 2"))
match menu:
    case 1:
        print(somme(a,b))
    case 2:
        print(division(a,b))
    case _:
        print('ERR')

