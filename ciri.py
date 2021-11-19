"""
importy
https://blog.networktocode.com/post/Basic-API-use-with-python/
https://curl.trillworks.com/

"""
from commands.configure import Controller


def main():
    """
    Menu po ktorym porusza sie uzytkownik
    """
    menu =  {
            "1." : "Sprawdz konfiguracje",
            "2." : "Zmien konfiguracje",
            "3." : "Zapisz zmiany",
            "4." : "Przywroc konfiguracje poczatkowa",
            "5." : "Zakoncz"
            }
    connection = [input("Podaj adres IP routera [x.x.x.x]\n"), input("Podaj maske [x.x.x.x]\n")]

    while True:
        options=menu.keys()
        for entry in options:
            print(entry, menu[entry])

        selection=input("Please Select:")
        if selection =='1':
            print("add")
        elif selection == '2':
            Controller(connection[0], connection[1])
        elif selection == '3':
            print("find")
        elif selection == '4':
            break
        else:
            print("Podaj prawidlowy parametr")


if __name__=="__main__":
    main()
