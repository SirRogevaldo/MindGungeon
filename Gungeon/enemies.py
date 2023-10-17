import time, copy, time

# Class Creation
class Prototype:
    # Constructor:
    def __init__(self):
        # Mocking an expensive call
        time.sleep(3)
        # Base attributes
        self.health = None
        self.attack = None
        self.speed = None
        self.atkSpeed = None

    # Clone Method:
    def clone(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Shotgun(Prototype):
    def __init__(self, health, attack, speed, atkSpeed):
        # Call superclass constructor, time.sleep() and assign base values
        # Concrete class attribute
        self.recoil = 30
    
    def clone(self):
        return copy.deepcopy(self)  

class Mage(Prototype):
    def __init__(self, height, age, defense, attack):
        self.mana = 360
        self.manaRegen = 1

    def clone(self):
        return copy.deepcopy(self)
    
class Sniper(Prototype):
    def __init__(self, height, age, defense, attack):
        self.cooldown = 30

    def clone(self):
        return copy.deepcopy(self)