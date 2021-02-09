class Ticket:
    def __init__(self, busId, place, name = None, lastName = None):
        self.busId = busId
        self.place = place
        self.name = name
        self.lastName = lastName

    def getBusId(self):
        return self.busId

    def setBusId(self, busId):
        self.busId = busId

    def getPlace(self):
        return self.place

    def setPlace(self, place):
        self.place = place

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName):
        self.lastName = lastName

    def __str__(self):
        return str(self.busId) + str(self.place) + str(self.name) + str(self.lastName)





