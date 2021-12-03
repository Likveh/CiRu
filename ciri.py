"""
importy
https://blog.networktocode.com/post/Basic-API-use-with-python/
https://curl.trillworks.com/
https://ultraconfig.com.au/blog/restconf-tutorial-everything-you-need-to-know-about-restconf-in-2020/
"""
from commands.configure import Controller
from commands.router import Router
from commands.visuals import *
from commands.helper import Helper


def main():
    """
    Menu po ktorym porusza sie uzytkownik
    """

    menu = {
            "1" : "Sprawdz konfiguracje",
            "2" : "Zmien konfiguracje",
            #szybka (automatyczna) konfiguracja, wlasna (dokladna) konfiguracja
            "3" : "Zapisz zmiany",
            "4" : "Przywroc konfiguracje poczatkowa",
            "5" : "Pomoc",
            "6" : "Zakoncz"
            }

    connection = [input("Podaj adres IP glownego routera [x.x.x.x]\n"), input("Podaj maske [/xx]\n")]
    ControlRouter = Controller(connection[0], connection[1])
    Controller.markRouters(ControlRouter, "192.168.1.0", "192.168.20.0", "/24")

    while True:
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
            Helper.enter()
        elif selection == '6':
            raise SystemExit
        else:
            print("Podaj prawidlowy parametr")


if __name__=="__main__":
    main()
