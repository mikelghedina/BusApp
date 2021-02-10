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
        numTicketsToSell = int(input("Choose the number of tickets you want to sell: "))
        name = input("Write your name: ")
        lastname = input("Write your last name: ")
        enterprise1.sellTickets(busId, numTicketsToSell, name, lastname)
        print(enterprise1)
    elif option == 2:
        print("Devolver TIckets")
    elif option == 3:
        print("Ver status")
    elif option == 4:
        closeMenu = True
        #Exit
    else:
        print("Invalid command")

