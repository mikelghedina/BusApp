from busTickets import Ticket
from Bus import Bus
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def createBusTickets():
    #print(bus + busLetters + "\n")
    total_buses = int(input("Escribir el numero de buses que tiene la organización: "))
    total_places = int(input("Escribir el numero de plazas totales del bus: "))
    # [VENDIDOS(0),RESTANTES(1)]
    buses = Bus.generarAutobuses(total_buses, total_places)
    clear_screen()
    return buses

createBusTickets()

def sellTickets(tl, numSell, busId):
    if 0 <= busId < len(tl):
        if numSell <= tl[busId][1]:
            tl[busId][1] -= numSell
            tl[busId][0] += numSell
            return "Vendidos " + str(numSell) + " tickets"
        else:
            return "Error, no se pueden vender mas tickets de los disponibles"
    else:
        return "Error, la compañia no tiene tantos buses porque no tiene dinero."


def returnTickets(tl, numReturn, busId):
    if 0 <= busId < len(tl):
        if numReturn <= tl[busId][0]:
            tl[busId][1] += numReturn
            tl[busId][0] -= numReturn
            return "Devueltos " + str(numReturn) + " tickets"
        else:
            return "Error, no se pueden devolver mas tickets de los vendidos"
    else:
        return "Error, la compañia no tiene tantos buses porque no tiene dinero."


def sellState(tl):
    info = ""
    for i in range(len(tl)):
        info += "bus" +"\nBus: " + str(i) + "\nTotal Plazas: " + str(tl[i][0] + tl[i][1]) + "\nTickets vendidos: " + str(
            tl[i][0]) + "\nTickets restantes: " + str(tl[i][1]) + "\n"
    return info


def ventaTickets():
    #buses = createBusTickets()
    # print(buses)

    exitProgram = False

    while not exitProgram:
        #print(bus + busLetters + "\n")
        print("""Que quieres hacer?
        1. Vender billetes (V)
        2. Devolucion de billetes (D)
        3. Estado de la venta (E)
        0. Salir (S)
        """)
        command = input("Escribe tu comando:")
        # print(buses)
        clear_screen()
        if command.capitalize() == "V":
            busId = int(input("Escoge el bus en el que quieras viajar: de 0 a " + "str(len(buses) - 1)" + ": "))
            numSell = int(input("Numero de tickets a vender: "))
            #print(sellTickets(buses, numSell, busId))
        elif command.capitalize() == "D":
            busId = int(input("Escoge el bus en el que quieras viajar: de 0 a " + "str(len(buses) - 1)" + ": "))
            numReturn = int(input("Numero de tickets a devolver: "))
            #print(returnTickets(buses, numReturn, busId))
        elif command.capitalize() == "E":
            "something"
            #print(sellState(buses))
        elif command.capitalize() == "S":
            exitProgram = True
        else:
            print("Invalid Command")

# Ejecucion de codigo
ventaTickets()

