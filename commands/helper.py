from .visuals import *

class Helper:
    def __init__(self):
        pass
    def enter():
        while True:
            menu = {
                    "1" : "WiP",
                    "2" : "WiP",
                    "3" : "WiP",
                    "4" : "WiP",
                    "5" : "WiP",
                    "6" : "Exit"
                }
            selection = printMenu(menu)

            if selection == '1':
                pass
            elif selection == '2':
                pass
            elif selection == '3':
                pass
            elif selection == '4':
                pass
            elif selection == '5':
                pass
            elif selection == '6':
                raise SystemExit
            else:
                print("Podaj prawidlowy parametr")
