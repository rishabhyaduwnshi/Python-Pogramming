def PetLover(pet):
    pet.talk()
    if(hasattr(pet,'walk')):
        pet.walk()

class Duck:
    def walk(self):
        print("Duck is walking")
    
    def talk(self):
        print("Duck is talking")
        
class Dog:
    def walk(self):
        print("Dog is walking")
    
    def talk(self):
        print("Dog is talking")

pet = Duck()
PetLover(pet)

pet = Dog()
PetLover(pet)
