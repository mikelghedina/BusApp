from busTickets import Ticket

class Bus:
    def __init__(self, id):
        self.id = id
        self.arrTickets = []

    def getIdBus(self):
        return self.id

    def setIdBus(self, id):
        self.id = id

    def setArrTickets(self, arrTickets):
        self.arrTickets = arrTickets

    def getArrTickets(self):
        for i in self.arrTickets:
            return i

    def __str__(self):
        return str(self.id) + self.getArrTickets()

