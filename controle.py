class vehcule :
    def __init__(self,marque,Max,mileage):
        self.__marque = marque
        self.max_speed = Max
        self.mileage = mileage
    def get_marque(self):
        return self.__marque
    def set_marque(self,marque):
        self.__marque=marque
    def del_marque(self):
        del self.__marque
    def afficher(self):
        print(self.get_marque(),self.max_speed,self.mileage)
    Marque = property(get_marque,set_marque,del_marque,"vehcule")
vehicule1=vehcule("mercides", 320, 200)

class vehucles():
    def __init__(self):
        pass
class bus(vehcule):
    def __init__(self,marque,Max,mileage,capacité,matricule):
        self.capacité = capacité
        self.matricule = matricule
        vehcule.__init__(self,marque,Max,mileage)
        def afficher(self):
            print(self.capacité,self.matricule,self.get_marque(),self.max_speed,self.mileage)
bus1=bus("ford",250,300,500,11111)

bus1.afficher()
bus1.Marque="nissan"
bus1.afficher()


