from Bus import Bus
from Ticket import Ticket


class Enterprise:

    def __init__(self):
        self.busesList = []

    def getBusesList(self):
        auxString = ""
        for i in self.busesList:
            auxString += i.__str__()
        return auxString

    def __str__(self):
        return self.getBusesList()

    def createBuses(self):

        total_buses = int(input("Escribir el numero de buses que tiene la organización: "))
        total_places = int(input("Escribir el numero de plazas totales del bus: "))

        for i in range(total_buses):
            self.busesList.append(Bus(i, total_places))

    def sellTickets(self, busId, numTicketsToSell):
        if busId >= 0 and busId < len(self.busesList):
            self.busesList[busId].sellTickets(numTicketsToSell)
        else:
            message = "This bus doesn't exist, try again."








