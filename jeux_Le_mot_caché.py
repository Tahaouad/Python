def MotValide(mot):
    if 4 <= len(mot) <= 25 and all(65 <= ord(c) <= 90 for c in mot):
        return True
    return False

def initialiserSolution(n):
    mot = input("Saisir le mot à trouver (en majuscules, 4-25 caractères): ")
    while not MotValide(mot):
        mot = input("Saisir le mot à trouver (en majuscules, 4-25 caractères): ")
    Tcar = list(mot)
    return Tcar

def creerEssai(n):
    return ['*'] * n

def afficherC(Tcar):
    mot = ''.join(Tcar)
    print(mot)

def jouer(Tcar, Tessai, proposition):
    if len(proposition) != 1:
        print("Vous devez proposer une seule lettre.")
        return False

    c = proposition.upper()
    present = False
    for i in range(len(Tcar)):
        if Tcar[i] == c:
            Tessai[i] = c
            Tcar[i] = '*'  # Remove the guessed letter from Tcar
            present = True
            break

    if present:
        print("Bon essai!")
    else:
        print("Mauvais essai!")

    return present

def main():
    n = int(input("Saisir la taille du mot à trouver: "))
    Tcar = initialiserSolution(n)
    Tessai = creerEssai(n)
    nbEssais = 0

    while nbEssais < 7:
        afficherC(Tessai)
        c = input("Proposer une lettre: ")
        if not jouer(Tcar, Tessai, c):
            nbEssais += 1

        if '*' not in Tessai:
            print("Gagné!")
            break

    if nbEssais == 7:
        print("Perdu!")

if __name__ == "__main__":
    main()