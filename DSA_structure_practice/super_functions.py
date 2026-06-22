'''How is the super function used?

Used to call and modify previous functions of a parentclass of a main class

Use an example parent class Mammal which has four legs
To create a Dog class with can bark
Lastly create a dog called Spot, print how many legs it has and make a noise

'''

'''

'''

class Mammal:
    def __init__(self,legs):
        self.legs=legs
    
    def make_mammal_noises(self):
        return "scritch scritch"
    
class Dog(Mammal):
    def __init__(self,borkieness:int,name:str):
        proxy=super()
        proxy.__init__(4)
        self.name=name
        self.borkieness=borkieness
    
    def make_noise(self):
        proxy=super()
        if self.borkieness>5:
            return "Bork Bork"
        else:
            return proxy.make_mammal_noises()

spot=Dog(6,'Spot')

print(spot.make_noise())
            






























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









class Mammal:
    def __init__(self):
        self.legs = 4
        self.is_alive = True
        self.makes_noise = True

    def describe(self):
        return f"I am a mammal with {self.legs} legs"

    def breathe(self):
        return "Inhale... Exhale..."

    def speak(self):
        return "*generic mammal noise*"


class Dog(Mammal):
    def __init__(self, name: str):
        proxy = super()
        proxy.__init__()        # Call parent constructor
        self.name = name

    def speak(self):
        return "Woof!"

    def demonstrate_proxy(self):
        proxy = super()

        # Call any parent method via the proxy
        print(proxy.describe())   # "I am a mammal with 4 legs"
        print(proxy.breathe())    # "Inhale... Exhale..."

        # This is the interesting one — proxy resolves to the
        # PARENT's speak(), bypassing Dog's override
        print(proxy.speak())      # "*generic mammal noise*"
        print(self.speak())       # "Woof!"


spot = Dog("Spot")
spot.demonstrate_proxy()








