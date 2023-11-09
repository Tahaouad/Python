def MotValide(mot):
  if len(mot) < 4 or len(mot) > 25:
    return False
  for c in mot:
    if ord(c) < 65 or ord(c) > 90:
      return False
  return True

def convertirCH(mot):
  
  tab = ['*'] * len(mot)
  for i in range(len(mot)):
    tab[i] = mot[i]
  return tab
print(convertirCH('Taha'))
def initialiserSolution(Tcar, n):
  mot = input("Saisir le mot à trouver (en majuscules, 4-25 caractères): ")
  while not MotValide(mot):
    mot = input("Saisir le mot à trouver (en majuscules, 4-25 caractères): ")
  Tcar = convertirCH(mot)

def creerEssai(Tessai, n):
  for i in range(n):
    Tessai[i] = '*'

def afficherC(Tcar, n):
  mot = ""
  for c in Tcar:
    mot += c
  print(mot)

def jouer(Tcar, Tessai, c, n):
  
  present = False
  for i in range(n):
    if Tcar[i] == c:
      Tessai[i] = c
      present = True
      break
  return present

def main():
  n = int(input("Saisir la taille du mot à trouver: "))
  Tcar = ['*'] * n
  Tessai = ['*'] * n
  initialiserSolution(Tcar, n)
  creerEssai(Tessai, n)
  nbEssais = 0
  while nbEssais < 7:
    afficherC(Tessai, n)
    c = input("Proposer une lettre: ")
    c = c.upper()
    if jouer(Tcar, Tessai, c, n):
      print("Bon essai!")
    else:
      print("Mauvais essai!")
      nbEssais += 1
  if nbEssais == 7:
    print("Perdu!")
  else:
    print("Gagné!")

if __name__ == "__main__":
    main()

