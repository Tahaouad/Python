class Voiture:
    def __init__(self,c,A):
        self.coleur = c
        self.anne = A
    def __del__(self):
        print("je suis le destrecteur")
v1 = Voiture("red",2020)
v2 = Voiture("green",2022)
del v1 # l'appelle de destrecteur 
print(v2)
print(Voiture.__doc__)#c est pour la documentation
print(v2.__dict__)#c est pour afficher les attribut et leur valeur sous forme dictionnaire
print(dir(v2))#pour aficher les méthodes accesibles pour l'objet v2
                                             
