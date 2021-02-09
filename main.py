from busTickets import Ticket
from Bus import Bus

def createBusTickets():
    #print(bus + busLetters + "\n")
    total_buses = int(input("Escribir el numero de buses que tiene la organización: "))
    total_places = int(input("Escribir el numero de plazas totales del bus: "))
    # [VENDIDOS(0),RESTANTES(1)]
    buses = Bus.generarAutobuses(total_buses)
    return buses

createBusTickets()