from Ticket import Ticket


class Bus:
    def __init__(self, id, places):
        self.id = id
        self.ticketsList = self.createTicketsList(places)
        # comentario

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

    def getTicketOfList(self, numPlace):
        for ticket in self.ticketsList:
            if ticket.getPlace() == numPlace:
                return ticket
        return False

    def createTicketsList(self, places):
        auxTicketsList = []
        for i in range(0, places):
            auxTicketsList.append(Ticket(i))
        return auxTicketsList

    def sellTickets(self, numticketSold, name, lastname):
        if numticketSold >= 0 and numticketSold < len(self.ticketsList)-1:
            self.ticketsList[numticketSold].setName(name)
            self.ticketsList[numticketSold].setLastName(lastname)
        else:
            return "You cannot sell more tickets"

    def returnTicket(self, numPlace):
        numPlace = numPlace - 1
        print(self.getTicketsList())
        if numPlace < len(self.ticketsList) and self.ticketsList[numPlace].name != None:
            self.ticketsList[numPlace].name = None
            self.ticketsList[numPlace].lastname = None
            return True
        else:
            return False

