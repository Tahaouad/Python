import datetime

class Patient:
    def __init__(self, nom, prenom, date_naissance=None, adresse=None, tel=None, email=None):
        self.code_patient = 0  # à gérer via une variable globale ou une base de données
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.adresse = adresse
        self.tel = tel
        self.email = email
    
    def afficher(self):
        print(f"Patient {self.nom} {self.prenom} (code {self.code_patient})")
        print(f"Date de naissance : {self.date_naissance}")
        print(f"Adresse : {self.adresse}")
        print(f"Téléphone : {self.tel}")
        print(f"E-mail : {self.email}")

class Visite:
    def __init__(self, code_patient, date_visite=None, heure_visite=None, montant_paye=0):
        self.date_visite = date_visite or datetime.date.today()
        self.heure_visite = heure_visite or datetime.datetime.now().strftime('%H:%M')
        self.code_patient = code_patient
        self.montant_paye = montant_paye
    
    def afficher(self):
        print(f"Visite le {self.date_visite} à {self.heure_visite}")
        print(f"Patient : code {self.code_patient}")
        print(f"Montant payé : {self.montant_paye}")

class RendezVous:
    def __init__(self, code_patient, date_rdv=None, heure_rdv=None, observation=None):
        self.date_rdv = date_rdv or datetime.date.today()
        self.heure_rdv = heure_rdv or datetime.datetime.now().strftime('%H:%M')
        self.code_patient = code_patient
        self.observation = observation
    
    def afficher(self):
        print(f"Rendez-vous le {self.date_rdv} à {self.heure_rdv}")
        print(f"Patient : code {self.code_patient}")
        print(f"Observation : {self.observation}")

class exceptionMontant(Exception):
    pass

class CabinetMedical:
    def __init__(self):
        self.patients = []
        self.visites = []
        self.rendez_vous = []
    
    def ajouterPatient(self, patient):
        self.patients.append(patient)
    
    def patientExistant(self, nom, prenom):
        for patient in self.patients:
            if patient.nom == nom and patient.prenom == prenom:
                return True
        return False
    
class exceptionMontant(Exception):
        pass
    
    def ajouterVisite(self, visite):
        if visite.montant_paye < 0:
            raise self.exceptionMontant("Le montant payé doit être positif.")
        self.visites.append(visite)
    
    def recetteDuJour(self, date):
        total = 0
        for visite in self.visites:
            if visite.date_visite == date:
                total += visite.montant_paye
        print("Recette du", date, ":", total, "euros")
    
    def patientsAyantDesVisites(self):
        derniere_semaine = datetime.today() - timedelta(days=7)
        for visite in self.visites:
            if visite.date_visite >= derniere_semaine:
                patient = self.getPatientByCode(visite.code_patient)
                print(patient.nom, patient.prenom)
    
    def annulerRDV(self, rendez_vous):
        self.rendez_vous.remove(rendez_vous)
    
    def exporterRDV(self, fichier):
        with open(fichier, "w") as f:
            for rdv in self.rendez_vous:
                f.write(str(rdv) + "\n")
a1=Patient("douyry", "ahmed")
a1.afficher()
a2=Patient("douyry", "youssef")
a2.afficher()
ajouterPatient()