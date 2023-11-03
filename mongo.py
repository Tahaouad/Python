import pymongo

server = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = server["Articles"]
mycol = mydb["article"]

def add_article():
    Reference = input('Donnez la reference :')
    Designation = input('Donnez la designation :')
    Qte = int(input('Donnez la quantite :'))
    Prix_vente = float(input('Donnez le prix de vente : '))
    Prix_Achat = float(input("Donnez le prix d'achat : "))
    
    mydict = {
        'Reference': Reference,
        'Designation': Designation,
        'Qte': Qte,
        'Prix vente': Prix_vente,
        "Prix d'achat": Prix_Achat
    }
    
    if Prix_Achat < Prix_vente and Qte > 0:
        x = mycol.insert_one(mydict)
    else:
        pass

def read_article():
    articles = mycol.find()
    
    for article in articles:
        for key, value in article.items():
            print(key ,":", value)
        print("-----------------------------------------------------------------------") 

def search_article():
    global reference,article
    reference = input('Donnez la reference :')
    query = {"Reference": reference}
    article = mycol.find_one(query)
    
    if article:
        for key, value in article.items():
            print(key, ":", value)
    else:
        print("Aucun article trouve avec la reference:", reference)

def update_article():
    search_article()
    query = {"Reference": reference}
    
    
    if article:
        
        
        Designation = input('Donnez la nv designation :')
        Qte = int(input('Donnez la nv quantite :'))
        Prix_vente = float(input('Donnez le prix de vente nv : '))
        Prix_Achat = float(input("Donnez le prix d'achat nv: "))
    
        val = {
            "$set": {'Designation': Designation , 'Qte': Qte , 'Prix vente': Prix_vente , "Prix d'achat": Prix_Achat}}
        
        mycol.update_one(query, val)
        print("Article modifier avec succès.")
    else:
        print("Reference inconue")
def delete_one():
    global reference
    reference = input("Donnez la reference d'article a supprimer:")
    query = {"Reference": reference}
    article = mycol.delete_one(query)
    
    if article:
        print('Deleted')
    else:
        print("Aucun article trouve avec la reference:", reference)

read_article()
delete_one()
update_article()