class person:
    def __init__(self,nom,prenom,cin):
        self.nom = nom
        self.prenom = prenom
        self._cin = cin
    def getcin(self):
        return self._cin
    def __str__(self):
        return(self.nom+""+self.prenom+""+ self._cin)
class vacine(person):
    def __init__(self,cv,dv,remarque,nom,prenom,cin):
        self.__code_vaccination = cv
        self.__date_vacination = dv
        self.remarque = remarque
        person.__init__(self,nom,prenom,cin)
    def getcode(self):
        return self.__code_vaccination
    def setcode(self,new_code):
        self.__code_vaccination = new_code
    def get_date(self):
        return self.__date_vacination
    def set_date(self,new_date):
        self.__date_vacination = new_date
    def __str__(self):
        return(self.nom+" "+self.prenom+" "+ self.getcin()+" "+self.__code_vaccination+" "+self.__date_vacination+""+self.remarque)
v=vacine("1111","13-5-2005","remarque","douyry","ahmed","mc308405")
class infovacin :
    def __init__(self,nom_vac,ref_vac,dure_dose):
        self.nom_vaccinaion = nom_vac
        self.reference_vacination = ref_vac
        self.duree_dose = dure_dose
    def __str__(self):
        return(self.nom_vaccinaion+" "+self.duree_dose+" "+self.reference_vacination)
iv=infovacin("va1","11111","5 mois")
class doses:
    def __init__(self,cd,dp,dd,ddr,vacin,vaccine):
        self.code_does = cd
        self.date_premiere = dp
        self.date_deuxieme = dd
        self.ddr = ddr
        self.vacin = vacin
        self.vaccine = vaccine
    def __str__(self):
        return(self.code_does+" "+self.date_premiere+" "+self.date_deuxieme+" "+self.ddr+" "+self.vacin.nom_vaccinaion+" "+self.vaccine.getcode())
d1=doses("a1","15-56-2002","15-9-305","15jrs",iv,v)
class centre:
    def __init__(self,nom,adresse,listevacin,liste,liste_doses):
        self.nom_centre = nom
        self.addresse = adresse
        self.liste_vaccin = listevacin
        self.liste_vaccine = liste
        self.liste_doses = liste_doses
    def __str__(self):
        return (self.nom_centre+" "+self.addresse +" "+str(self.liste_vaccin)+" "+str(self.liste_vaccine)+" "+str(self.liste_doses))
c1=centre("agdal","hay agdal",iv,v,d1)
def ajouter_vacciné():
    nom=str(input("Donner le nom de Vaccine : "))
    prenom=str(input("Donner le prenom de Vaccine : "))
    cin=str(input("Donner le cin de Vaccine : "))
    cv=str(input("Donner le code de vaccine : "))
    dv=str(input("donner la date de vaccination : "))
    remarque=str(input("Remarque : "))
    Vaccine1=vacine(cv, dv, remarque, nom, prenom, cin)
    print(Vaccine1)
def ajouter_vaccin():
    global T
    T=[]
    n=int(input("donner le nombre a ajouter des vaccin :"))
    for i in range(n):
        nom_vac=str(input("Nom vaccin : "))
        ref_vac=str(input("reference de vaccin : "))
        dure_dose=str(input("Duree de Dose de vaccin : "))
        vaccin1=infovacin(nom_vac, ref_vac, dure_dose)
        print(vaccin1)
        T.append(vaccin1)
def rechercher():
    rf = input("donner la reference de vaccin")
    for i in range (len(T)):
        if rf == T[i].ref_vac:
            print(T[i].ref_vac)
def Modifier():
    rf = input("donner la reference de vaccin")
    for i in range (len(T)):
        if rf == T[i].ref_vac:
            T[i].nom_vaccinaion=input("donner le neuveux nom :")
def supprimer():
    rf = input("donner la reference de vaccin")
    for i in range (len(T)):
        if rf == T[i].ref_vac:
             remove(i)
            
a1=Pati



        
        

        
    
    
    