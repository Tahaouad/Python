'''Verifier que l'utilisateur a entrer un nombre + Gerer l'erreur d'espace'''
b = True
while b:
    ch = input("Entrer: ")
    ch = ch.strip() #Eliminer espace
    if ch and ch.isdigit(): #isdigit() fonction qui return True si variable est digit
        number = int(ch)
        b = False      
    else:
        print("(Invalid data) entrer un nombre.")


















# '''Verifier type d'une variable'''
# x = 2
# print(isinstance(x, str)) #Return False si x est diferent de str

# '''Verifier si variable est numerique'''

# text = "12345"
# if text.isnumeric():
#     print("La chaîne contient uniquement des chiffres.")
