from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def show(self):
        pass
    
    def display(self):
        print("Parent Display")

class Child(Parent):
    #overriding the abstract method
    def show(self):
        print("Child Show")

c = Child()
c.show()
