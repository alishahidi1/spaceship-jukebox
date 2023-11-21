class Spaceship():
    
    def __init__(self,name=None):
        if name is None:
            self.callSign = "Nameless spaceship"
            self._shieldStrength = 100
        else:
            self.callSign = name
            self._shieldStrength = 100



    #methods
    def fireMissile(self):
        return "Pew!"
    
    def reduceShield(self, amount):
        self._shieldStrength -= amount
        

#instantiation
myShip = Spaceship()
print(myShip.callSign)