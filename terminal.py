"""
TUI dla uzytkownika
"""

import configure as handler





menu_check = {
        "1" : ("Version", "Cisco-IOS-XE-native:native/version"),
        "2" : ("Banner", "Cisco-IOS-XE-native:native/banner/motd"),
        "3" : ("Hostname", "Cisco-IOS-XE-native:native/hostname"),
        "4" : ("Users", "Cisco-IOS-XE-native:native/username"),
        "5" : ("IP Forwarding", "Cisco-IOS-XE-native:native/ip"),
        "6" : ("Interfaces", "Cisco-IOS-XE-native:native/interface")
        }

def check_config(router):
    """
    polecenia GET
    """
    while True:
        print()
        for entry in sorted(menu_check.keys()):
            print(f"{entry}. {menu_check[entry][0]}")

        selection = input(
                        f"Type [{len(menu_check)+1}] to change go back.\nPlease Select: "
                    )
        try:
            if int(selection) == (len(menu_check)+1):
                return
            router.get(menu_check.get(selection,[None])[1])
        except IndexError:
            print("Something went wrong")
            continue




def change_banner():
    """
    edit banner
    """
    banner = input("Type new banner name: ")
    post =  {
                'Cisco-IOS-XE-native:motd': {
                                                'banner': banner
                                                }
            }
    return post
def change_hostname():
    """
    changes hostname
    """
    hostname = input("Type new banner name: ")
    post =  {
                'Cisco-IOS-XE-native:hostname': hostname
            }
    return post
def change_user():
    """
    good question
    """
def change_ip_forwarding():
    """
    greater question
    """
def change_interfaces():
    """
    wht
    """


menuChange = {
        "1" : ("Banner", "Cisco-IOS-XE-native:native/banner/motd", change_banner),
        "2" : ("Hostname", "Cisco-IOS-XE-native:native/hostname", change_hostname),
        "3" : ("Users", "Cisco-IOS-XE-native:native/username", change_user),
        "4" : ("IP Forwarding", "Cisco-IOS-XE-native:native/ip", change_ip_forwarding),
        "5" : ("Interfaces", "Cisco-IOS-XE-native:native/interface", change_interfaces)
        }

def change_config(router):
    """
    polecenia POST
    """
    while True:
        print()
        for entry in sorted(menu_check.keys()):
            print(f"{entry}. {menu_check[entry][0]}")

        selection = input(
                        f"Type [{len(menu_check)+1}] to change go back.\nPlease Select: "
                    )
        try:
            if int(selection) == (len(menu_check)+1):
                return
            request = menu_check.get(selection,[None])[2]()
            router.post(request)
        except IndexError:
            print("Something went wrong")
            continue


#Menu po ktorym porusza sie uzytkownik
menu = {
        "1" : ("Check Config", check_config),
        "2" : ("Change Config", change_config)
        }



def showmenu(device):
    """
    obsluga menu
    """
    print(f"\nWybrano Urządzenie: {device['host']}")
    router = handler.Controller(device)
    while True:
        print()
        for entry in sorted(menu.keys()):
            print(f"{entry}. {menu[entry][0]}")

        selection = input(
                        f"Type [{len(menu)+1}] to change device..\nPlease Select: "
                    )
        try:
            if int(selection) == (len(menu)+1):
                break
            menu.get(selection,[None])[1](router)
        except IndexError:
            print("Something went wrong")
            continue
