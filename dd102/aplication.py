# BASE = [{"Nom":"moad",
#        "CIN":"TK33557",
#        "cod":143065225,
#        "Date_naissance":15_07_2005,
#        "Notes":{"Math":6,"PC":12.75,"svt":12,"Arabe":18,"francais":17,"englais":13}
#        },
#       {"Nom":"ahmed",
#        "CIN":"TK8874",
#        "cod":143065224,
#        "Date_naissance":21_07_2004,
#        "Notes":{"Math":12,"PC":18,"svt":18,"Arabe":9,"francais":13,"englais":10}
#        },
#       {"Nom":"mohammed",
#        "CIN":"TK5893",
#        "cod":143065223,
#        "Date_naissance":21_10_2005,
#        "Notes":{"Math":6,"PC":13,"svt":12.5,"Arabe":17,"francais":19,"englais":15}
#        },
#       {"Nom":"Salah EDine ",
#        "CIN":"TK1234",
#        "cod":143065222,
#        "Date_naissance":31_31_2006,
#        "Notes":{"Math":6,"PC":12,"svt":13.5,"Arabe":17,"francais":19,"englais":18}
#        }]
# print("========================================MES ETUDIANTS================================================")

# while True:
#     print("1-ajouter un étudiant\n2-rechercher un etudiant\n3-modifier les infos des etudian")
#     print("4-supprimer un etudiant\n5-moyenne d'un etudiant\n6-Quitter")
#     choix = int (input("choisire votre operation Monsieur/Madame : "))
#     while choix<1 or choix>6:
#         choix = int(input("choisir une autre operation qui entre 0 et 6: "))
#     if  choix == 1 :
#         BASE.append({"Nom:":input("donner le noms de nouveau d'etudiant"),
#                      "CIN:":input("donner la carte nationnal"),
#                      "cod:":int("donner le code d'etudiant"),
#                      "Date_naissance:":input("donner la Date_naissance "),
#                      "Notes:":{"math":int(input("note de math")),
#                                "PC":int(input("note de PC")),
#                                "svt":int(input("note de svt")),
#                                "arabe":int(input("note de arabe")),
#                                "francais":int(input("note de francais")),
#                                "englais":int(input("note de englais"))
#                                }
#                      })
#     if choix == 2:
#         code=int(input("donner le cod d' etudiant qui tu veut chercher:"))
#         for i in BASE:
#             if i["cod"]==code:
#                 print(i)

#     if choix==3:
#         cod=input("donner le code de etudiant")
#         for  i in BASE:
            
#             if i["cod"]==cod:
#                 pos=input("entrer la pposition")
#                 if pos!="Notes":
#                     value=input("entrer la valeure:")
#                     i[pos]=value
#                     print(i)
#                 else:
#                     for j in i["Notes"]:
#                         pos=input("entrer la nouvelle note:")
#                         value=input("entrer la valeure:")
#                         j[pos]=value
#                         print(i)

#     if choix==4:
#          cod=input("donner le code")
#          for i in BASE:
#              if i["cod"]==cod:
#                  i.clear()

#     if choix==5: 
#          s=0
#          cod=input("donner le code d'etudiant")
#          for i in BASE:
#              if i["cod"]==cod:
#                  for j in i["Notes"]:
#                      s=s+i["Notes"][j]
#          m=s/len(i["notes"])
#          print("la moyenne:",m)


#     if choix==6:
#          print("merci")
#          break
                   
   
                
                  
# list_etudiants = [{"nom" : 'TEST',"prenom" : 'TEST'},{"nom" : 'TEST2',"prenom" : 'TEST'},{"nom" : 'TEST3',"prenom" : 'TEST'}]

# cherche = input('Chercher par Nom: ')
# for etudiant in  list_etudiants :
#     if etudiant['nom'] == cherche : 
#         print(etudiant)
#         NV_NOM = input('Donner nv Nom : ')
#         NV_PRENOM = input('Donner nv PRENOM : ')
#         etudiant['nom'] = NV_NOM ;
#         etudiant['prenom'] = NV_PRENOM ;
#         print(etudiant)

# cherche = input('Chercher par Nom: ')

# for etudiant in  list_etudiants :
#     if etudiant['nom'] == cherche : 
#         print(etudiant)
#         VALIDATION = input('Confirmer N/O')
#         if VALIDATION == 'O' :
#             list_etudiants.remove(etudiant)
#             print('DONE')
#             print(list_etudiants)
#         else: 
#             pass
c = str(34567890)
code_clt = 345

CODE = ""
for i in c:
    CODE +=str(i)
    print(CODE)
    if CODE == str(code_clt) :
        print('done')
        break
    else :
        print('introuvable')
        
