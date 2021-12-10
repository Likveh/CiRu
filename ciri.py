"""

https://devnetsandbox.cisco.com/RM/Diagram/Index/7b4d4209-a17c-4bc3-9b38-f15184e53a94?diagramType=Topology
https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology

https://developer.cisco.com/learning/modules/intro-device-level-interfaces/intro-restconf/step/1

https://www.youtube.com/watch?v=qeanMXpcHIk
https://www.youtube.com/watch?v=XmOBTqDBFyI

https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/172/b_172_programmability_cg/restconf_protocol.html
https://developer.cisco.com/learning/modules
"""

import json
import sys
import terminal as menu
#router information etc

with open('settings.json', encoding="UTF-8") as file:
    settings = json.load(file)
    devices = settings['configurations']
    deviceMain = devices[0]

def main():
    """
    main fun
    """

    #select the router to work on
    while True:
        device_number = 0
        for device in devices:
            device_number+=1
            print(f"{device_number}. {device['host']}")
        try:
            selection = input('Wybierz urządzenie lub wpisz [exit] aby wyjsc: ')
            if selection == 'exit':
                sys.exit()
            selection = int(selection)
            device_selected = devices[selection-1]
            menu.showmenu(device_selected)
        except (ValueError, IndexError):
            print("Something went wrong")
            continue


if __name__=="__main__":
    main()
