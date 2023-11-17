import random
comptes = {}
clients = {}
compte_client = {}
client_counter = 1
def ajouter_compte():
    global client_counter
    num_client = client_counter
    code_secret = input("Entrez le code secret du client : ")
    clients[num_client] = code_secret
    num_compte = num_client * 100 + random.randint(0, 100)
    solde_initial = float(input("Entrez le solde initial du compte : "))
    comptes[num_compte] = solde_initial
    compte_client[num_client] = num_compte
    client_counter += 1
    print("Compte ajouté avec succès. Numéro de compte :", num_compte)
    print (comptes)
    
def supprimer_compte():
    n = int(input('donner le numero de compte '))
    for i in comptes :
        if n == i[comptes].values():
            comptes.remove(i)
ajouter_compte()
supprimer_compte()

        