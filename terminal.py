"""
TUI dla uzytkownika
"""

import configure as handler


#komendy do edycji wartosci na urzadzeniu, TODO: daj do innego pliku
def change_banner(module, router):
    """
    edit banner
    """
    banner = input("Type new banner name: ")
    data =  {
                "banner": {
                    "motd": {
                            "banner": banner
                    }
                }
            }
    router.put(module, data)
    return

def change_hostname(module, router):
    """
    changes hostname
    """
    hostname = input("Type new hostname: ")
    data =  {
                'hostname': hostname
            }
    router.put(module, data)
    return
def change_interfaces(module, router):
    """
    add
    """
    selection = input("What do you want to do? [Add/Remove/Edit]: ")

    #REMOVE INTERFACE
    if selection.lower() == 'remove':
        name = input('Interface name: ')
        module += '/interface='+name
        router.delete(module)
        return

    #ADD/EDIT INTERFACE
    if selection.lower() == 'add' or 'edit':

        #all data needed for interface
        name = input('Interface name: ')
        description = input("Description: ")
        interface_type = input("interface type: ") #iana-if-type:softwareLoopback
        enabled = bool(int(input("enable? [1/0]: ")))
        address_ip = input("Ipv4: ")
        address_mask = input("Mask: ")
        data = {
                    "ietf-interfaces:interface": {
                        "name": name,
                        "description": description,
                        "type": interface_type,
                        "enabled": enabled,
                        "ietf-ip:ipv4": {
                            "address": [
                                {
                                    "ip": address_ip,
                                    "netmask": address_mask
                                }
                            ]
                        }
                    }
                }
        """
        {
                "description": input("Description: "),
                "enabled": bool(int(input("enable? [1/0]: "))),
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": input("Ipv4: "),
                            "netmask": input("Mask: ")
                        }
                    ]
                },
                "ietf-ip:ipv6": {},
                "name": input('Interface name: '),
                "type": "iana-if-type:ethernetCsmacd"
        }
        """
        if selection.lower == 'add':
            router.post(module, data)
        if selection.lower == 'edit':
            router.put(module, data)
        return


#listy opcji wyswietlanych w terminalu
menu_check = {
        "1" : ("Version", "Cisco-IOS-XE-native:native/version"),
        "2" : ("Banner", "Cisco-IOS-XE-native:native/banner"),
        "3" : ("Hostname", "Cisco-IOS-XE-native:native/hostname"),
        "4" : ("Users", "Cisco-IOS-XE-native:native/username"),
        "5" : ("IP Forwarding", "Cisco-IOS-XE-native:native/ip"),
        "6" : ("Interfaces", "ietf-interfaces:interfaces")
        }
menu_change = {
        "1" : ("Banner", "Cisco-IOS-XE-native:native/banner", change_banner),
        "2" : ("Hostname", "Cisco-IOS-XE-native:native/hostname", change_hostname),
        "3" : ("Interfaces", "ietf-interfaces:interfaces", change_interfaces)
        }

def print_menu(option_menu):
    """
    wyswietla menu wyboru
    """
    print()
    for entry in sorted(option_menu.keys()):
        print(f"{entry}. {option_menu[entry][0]}")

def check_config(router):
    """
    menu do wybrania wyswietlania configu
    """
    while True:
        print_menu(menu_check)
        selection = input(
                        f"{len(menu_check)+1}. Go back\nPlease Select: "
                    )
        try:
            if int(selection) == (len(menu_check)+1):
                return
            router.get(menu_check.get(selection,[None])[1])
        except IndexError:
            print("The value is incorrect")
            continue
        except Exception as err:
            print(f"An unknown error occured [{type(err).__name__}: {err}]")
            continue


def change_config(router):
    """
    menu do wybrania edycji configu
    """
    while True:
        print()
        print_menu(menu_change)

        selection = input(
                        f"{len(menu_change)+1}. Go back\nPlease Select: "
                    )
        try:
            if int(selection) == (len(menu_change)+1):
                return

            #wysyla PUT o module z menu_change oraz aktywuje funkcje wskazana przez menu change
            module = menu_change.get(selection,[None])[1]
            menu_change.get(selection,[None])[2](module, router)
        except IndexError:
            print("Select a valid router")
            continue
        except Exception as err:
            print(f"An unknown error occured [{type(err).__name__}: {err}]")
            continue

#rodzaje po ktorym porusza sie uzytkownik
menu = {
        "1" : ("Check Config", check_config),
        "2" : ("Change Config", change_config)
        }



#wyswietla menu urzadzenia
def showmenu(device):
    """
    obsluga menu
    """
    print(f"\nSelected device: {device['host']}")
    router = handler.Controller(device)
    while True:
        print_menu(menu)

        selection = input(
                        f"{len(menu)+1}. Change device\nPlease Select: "
                    )
        try:
            if int(selection) == (len(menu)+1):
                break
            menu.get(selection,[None])[1](router)
        except IndexError:
            print("The value is incorrect")
            continue
        except Exception as err:
            print(f"An unknown error occured [{type(err).__name__}: {err}]")
            continue
