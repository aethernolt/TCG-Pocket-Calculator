import card

class set:
    def __init__(self, name, packs):
        self.name = name
        self.packs = packs
    
    def printname(self):
        print(self.name)
    
    def listpacks(self):
        for x in self.packs:
            print(x)
    
    def add(self, toAdd):
        for x in toAdd:
            card.add(x)