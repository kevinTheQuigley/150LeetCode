'''How is the super function used?

Used to call and modify previous functions of a parentclass of a main class

Use an example parent class Mammal which has four legs
To create a Dog class with can bark
Lastly create a dog called Spot, print how many legs it has and make a noise

'''

'''

'''

class Mammal:
    def __init__(self):
        self.legs=4
        self.is_alive=True
        self.makes_noise=True

class Dog(Mammal):
    def __init__(self,name:str,borkieness:int):
        proxy = super()
        proxy.__init__()
        self.name = name
        if self.makes_noise and borkieness>5:
            self.borking=True

spot = Dog("Spot",6)
if spot.borking:
    print(spot.name+" is Borking mad!")


















