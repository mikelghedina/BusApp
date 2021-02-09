from busTickets import Tickets
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

