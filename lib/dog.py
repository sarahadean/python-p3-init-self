
##Object Initialization
class Dog:
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed

    def sit(self):
        print("The dog is sitting.")

    def get_adopted(self, owner_name):
        self.owner = owner_name
fido = Dog("Fido")
fido.name
#Fido

fido.owner = "Sophie"
#self.attribute = value
fido.owner
#Sophie

fido.get_adopted("Sophie")
print(fido.owner)

fido.sit()