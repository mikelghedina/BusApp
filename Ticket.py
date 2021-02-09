class Ticket:
    def __init__(self, place, name=None, lastname=None):
        self.place = place
        self.name = name
        self.lastname = lastname

    def getPlace(self):
        return self.place

    def setPlace(self, place):
        self.place = place

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getLastName(self):
        return self.lastname

    def setLastName(self, lastname):
        self.lastname = lastname

    def __str__(self):
        return "Num Plaza: " + str(self.place) + ", Nombre: " + str(self.name) + ", Apellido: " + str(self.lastname)+"\n"






