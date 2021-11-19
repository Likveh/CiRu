
#wyswietla opcje w terminalu
def printMenu(menu):
    options = menu.keys()
    for entry in options:
        print(entry, menu[entry])
    return input("Wybierz: ")