from busTickets import Ticket


class Bus:
    """ Clase Autobus """

    def __init__(self, id):
        self.id = id
        self.arrTickets = []

    """ STATIC METHODS """

    @staticmethod
    def generarAutobuses(cantAutobuses):
        arrAutobuses = []

        for i in cantAutobuses:
            bus = Bus(i)
            arrAutobuses.append(bus)
            print(bus)

        return arrAutobuses

    """GETTERS AND SETTERS"""

    def getIdBus(self):
        return self.id

    def setArrTickets(self, arrTickets):
        self.arrTickets = arrTickets

    def __str__(self):
        return str(self.id) + self.getArrTickets()

    def getArrTickets(self):
        for i in self.arrTickets:
            return i
