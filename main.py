from Enterprise import Enterprise


enterprise1 = Enterprise()
enterprise1.createBuses()

print(enterprise1)

closeMenu = False

while not closeMenu:
    print("""1.Vender tickets
2.Devolver tickets
3.Ver stats
4.Exit""")

    option = int(input("Introduce la opcion deseada: "))

    if option == 1:
        busId = int(input("Choose the bus: "))
        if enterprise1.getBusOfList(busId) != False:
            bus = enterprise1.getBusOfList(busId)
            numTicketsToSell = int(input("Choose the number of tickets you want to sell: "))
            if len(bus.ticketsList)-1 == numTicketsToSell:
                name = input("Write your name: ")
                lastname = input("Write your last name: ")
                enterprise1.sellTickets(busId, numTicketsToSell, name, lastname)
            else:
                print("Those many are not available")
        else:
            print("This bus doesn't exist")
            #print(enterprise1)
    elif option == 2:
        busId = int(input("Choose the bus: "))
        if enterprise1.getBusOfList(busId) != False:
            numPlace = int(input('Introduce el numero de asiento que quieres devolver: '))
            bus = enterprise1.getBusOfList(busId)

            if bus.returnTicket(numPlace):
                print('Se ha devuelto el ticket correctamente')
            else:
                print('El ticket que quieres devolver no existe')
        else:
            print('No existe el bus seleccionado')
    elif option == 3:
        busId = int(input("Choose the bus: "))
        print(enterprise1.busesList[busId])
    elif option == 4:
        closeMenu = True
        #Exit
    else:
        print("Invalid command")

