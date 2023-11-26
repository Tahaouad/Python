class medcin:
    def __init__(self,code,specialité,secteur):
        self.__code = code 
        self.specialité = specialité
        self.secteur = secteur
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self,new_code):
        self.__code = new_code
    @code.deleter
    def code(self):
        del self.__code
    def __str__(self):
        return ("Code"+" "+self.__code+" "+"Spécialité"+" "+self.specialité+" "+"Secteur"+" "+self.secteur)
    
class syndicat:
    def __init__(self):
        pass
class Neuro(medcin):
    def __init__(self, code, specialité, secteur,clinique,enatendu):
        self.clinique = clinique
        self.enatendu = enatendu
        medcin.__init__(self,code,specialité,secteur)
medcin1 = medcin("1111", "yeux", "midicale")
medcin2 = Neuro("2222", "333333", "44444", "55555", "666666")
print(medcin1)
medcin1.code ="5555"
print(medcin1)
print(medcin2,medcin2.clinique,medcin2.enatendu)


