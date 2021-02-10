from Ticket import Ticket


class Bus:
    def __init__(self, id, places):
        self.id = id
        self.ticketsList = self.createTicketsList(places)

    def getIdBus(self):
        return self.id

    def setIdBus(self, id):
        self.id = id

    def getTicketsList(self):
        auxString = "Bus con id: " + str(self.id) + "\n"
        for i in self.ticketsList:
            auxString += i.__str__()
        return auxString

    def __str__(self):
        return self.getTicketsList()

    def createTicketsList(self, places):
        auxTicketsList = []
        for i in range(0, places):
            auxTicketsList.append(Ticket(i))
        return auxTicketsList

    def sellTickets(self, numTicketsToSell):
        if numTicketsToSell >= 0 and numTicketsToSell < len(self.ticketsList):
            del self.ticketsList[:numTicketsToSell]
        else:
            message = "You cannot sell more tickets"

