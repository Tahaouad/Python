from random import randint
LIST_CLIENTS = [{"ID": 1,"PWD" :"1244"},
                {"ID": 2,"PWD" :"12424"},
                {"ID": 3,"PWD" :"332R3"},
                {"ID": 4,"PWD" :"W35678"},
                {"ID": 5,"PWD" :"UTSDJC"},
                ]

LIST_COMPTE = []
def add_compte(id_client,solde) :
    client = {"Num_compte" :str(id_client)+str(randint(1,100)),"solde" : solde }
    LIST_COMPTE.append(client)
add_compte(1,300)
add_compte(3,100)
print(LIST_COMPTE)



