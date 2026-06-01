class Animal:
    def __init__(self,name:str):
        if name is not None:
            self.has_name=True
    
    def makes_noise(self):
        return "It's making a noise."
    
class Dog(Animal):
    def __init__(self,name:str):
        super().__init__(name)
        if self.has_name:
            self.name=name
    
    def bork(self):
        mn = super().makes_noise()
        print(mn," It's Borking!")

    def say_name(self):
        print("My name is "+self.name)

bruno = Dog("Bruno")

bruno.bork()
bruno.say_name()