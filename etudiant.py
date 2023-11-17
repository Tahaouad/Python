
etudiants = [
    {
        'cin' : 'MC308405',
        "nom": "douyry ahmed",
        "notes": {
            "mathématiques": 18,
            "français": 16,
            "svt": 15,
        },
    },
    {
        'cin' : 'BB308405',
        "nom": "ouad taha",
        "notes": {
            "mathématiques": 19,
            "français": 17,
            "svt": 16,
        },
    },
]
while True :
    """Affiche le menu et demande à l'utilisateur de faire un choix."""
    print("Menu étudiant")
    print("1. Ajouter un étudiant")
    print("2. Rechercher un étudiant")
    print("3. Supprimer un étudiant")
    print("4. Afficher les listes des notes d'un étudiant")
    print("5. Afficher la moyenne d'un étudiant")
    print("6. quitter ")

    choix = int(input("Entrez le numéro de l'option que vous souhaitez : "))
    if choix == 1 :
        dic = {'cin' : input('donner le cin '),
            "nom": input('donner le nom'),
            "notes": {
                "mathématiques": float(input('donner la note de mathématiques')),
                "français": float(input('donner la  note français')),
                "svt": float(input('donner la note "svt"'))}}
        print(dic)
        etudiants.append(dic)
        print (etudiants)
    if choix == 2 :
        cin = input('donner le cin de votre etudiant a rechercher ')
        for j in etudiants:
            if cin == j['cin']:
                print('existe')
                print(j)
                break
            elif cin != j['cin']:
               pass
            else : 
                print('n existe pas ')
                
    if choix == 3:
        cin = input('donner le cin de votre etudiant a rechercher ')
        for j in etudiants:
                if cin == j['cin']:
                    etudiants.remove(j)
                    print('supprime')
                    break
                else : 
                    print('n existe pas ')
                    break
    if choix == 4:
        
        cin = input('donner le cin de votre etudiant a rechercher ')
        for j in etudiants:
            if cin == j['cin']:
                for matiere, note in j["notes"].items():
                    print(matiere ,':', note)
    if choix == 5 :
        cin = input('donner le cin de votre etudiant a rechercher ')
        for j in etudiants:
            if cin == j['cin']:
                cp = 0
                for note in j["notes"].values():
                    cp = cp + note
        print (cp/3)
    if choix == 6 :
        break
        

    




