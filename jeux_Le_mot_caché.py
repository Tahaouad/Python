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
# Procédure initialiserSolution
def initialiserSolution(Tcar, n):
  """
  Demande à l'utilisateur de saisir le mot à trouver et
  le remplit dans le tableau Tcar.
  """
  mot = input("Saisir le mot à trouver (en majuscules, 4-25 caractères): ")
  while not MotValide(mot):
    mot = input("Saisir le mot à trouver (en majuscules, 4-25 caractères): ")
  Tcar = convertirCH(mot)

# Procédure creerEssai
def creerEssai(Tessai, n):
  """
  Remplit le tableau Tessai par le caractère '*'.
  """
  for i in range(n):
    Tessai[i] = '*'

# Procédure afficherC
def afficherC(Tcar, n):
  """
  Affiche Tcar à l'écran comme une chaîne de caractères.
  """
  mot = ""
  for c in Tcar:
    mot += c
  print(mot)

# Fonction jouer
def jouer(Tcar, Tessai, c, n):
  """
  Retourne vrai si le caractère c est présent dans la solution et
  met à jour le tableau Tessai.
  Le caractère doit remplacé à la bonne place le caractère '*' (pour toutes ses occurrences).
  Le cas échéant, retourne faux.
  """
  present = False
  for i in range(n):
    if Tcar[i] == c:
      Tessai[i] = c
      present = True
      break
  return present

# Programme principal
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

