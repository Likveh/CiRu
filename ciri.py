"""
https://devnetsandbox.cisco.com/RM/Diagram/Index/7b4d4209-a17c-4bc3-9b38-f15184e53a94?diagramType=Topology
https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology
https://developer.cisco.com/learning/modules/intro-device-level-interfaces/intro-restconf/step/1
"""

import json
import sys
import terminal as menu
#router information etc


with open('settings.json', encoding="UTF-8") as file:
    try:
        settings = json.load(file)
        devices = settings['configurations']
        deviceMain = devices[0]
    except Exception:
        print("Failed to load the configuration file! Closing")
        #exit
        sys.exit()

def main():
    """
    wybierz router na ktorym chcesz pracowac
    """

    #select the router to work on
    while True:
        device_number = 0
        for device in devices:
            device_number+=1
            print(f"{device_number}. {device['host']}")
        try:
            selection = input(f'{len(devices)+1}. Add a new device\n{len(devices)+2}. Remove a device \n{len(devices)+3}. Exit\nSelect: ')
            if selection == str(len(devices)+1):
                #add a device
                new_device  = {
                                "name": input("Name: "),
                                "host ip": input("Host Address: "),
                                "username": input("Username: "),
                                "password": input("Password: "),
                                "restconf_port": input("Restconf_port: "),
                                "management_interface" : input("management_interface: ")
                            }

                #append it to current list
                settings['configurations'].append(new_device)

                #file update
                with open('settings.json', "w", encoding="UTF-8") as file:
                    json.dump(settings, file, indent=4, sort_keys=True)
                continue

            if selection == str(len(devices)+2):
                #remove selected device
                device_key = int(input(f"Which one? [1-{len(devices)}]"))
                del settings['configurations'][device_key-1]

                #file update
                with open('settings.json', "w", encoding="UTF-8") as file:
                    json.dump(settings, file, indent=4, sort_keys=True)
                continue

            if selection == str(len(devices)+3):
                #exit
                sys.exit()

            selection = int(selection)
            device_selected = devices[selection-1]
            menu.showmenu(device_selected)
        except (ValueError, IndexError):
            print("The value is incorrect")
            continue
        except Exception as err:
            print(f"An unknown error occured [{type(err).__name__}: {err}]")
            continue


if __name__=="__main__":
    main()
