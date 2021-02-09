from busTickets import Ticket

class Bus(object):
    """ Clase Autobus """

    def __init__(self, id):
        self.id = id

        self.arrTickets = []

    
    """ STATIC METHODS """
    @staticmethod
    def generarAutobuses(cantAutobuses, cantPlazas):
        arrAutobuses = []
        arrTickets = []

        for id in range(0, cantAutobuses):
            bus = Bus(id)
            for i in range(cantPlazas):
                arrTickets.append(Ticket(bus.getIdBus(), i))
            bus.setArrTickets(arrTickets)



        return arrAutobuses


    """GETTERS AND SETTERS"""
    def getIdBus(self):
        return self.id

    def setArrTickets(self, arrTickets):
        self.arrTickets = arrTickets
     


  


