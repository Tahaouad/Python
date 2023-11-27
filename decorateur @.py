class EtudiantGeek:
    def __init__(self):
        self.__age = 0
        
    @property
    def age(self):  
        return self.__age
    
    @age.setter 
    def age(self, a): 
        self.__age = a

    @age.deleter
    def age(self):
        del self.__age
E1 = EtudiantGeek()
print(E1.age)
E1.age = 12
print(E1.age)
print(E1.age)
print(E1.age)

