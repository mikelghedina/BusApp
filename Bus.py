class Bus(object):
    """ Clase Autobus """

    def __init__(self,idBus, arrTickets):
        self.idBus = idBus
        self.tickets = []

    
    """ STATIC METHODS """
    @staticmethod
    def generarAutobuses(cantAutobuses, cantAsientos):
        arrAutobuses = []

        for id in range(0,cantAutobuses):
            arrAutobuses.append( Bus(id) )
        

        return arrAutobuses


    """GETTERS AND SETTERS"""
    def getIdBus(self):
        return self.idBus
     


  


