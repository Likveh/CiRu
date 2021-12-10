"""
biblioteka do zapytan GET/POST
"""

import json
import requests

#data needed for requests



#print(response)


class Controller:
    """
    handler zapytan
    """
    def __init__(self, device):
        #    https://[adresIp]:[Port]/restconf/data/modul
        self.device = device
        self.module = ""
        self.url = ""
        self.headers = {
                        "Accept" : "application/yang-data+json, application/yang-data.errors+json",
                        "Content-Type" : "application/yang-data+json",
                        }


    def set_module(self, module):
        """
        ustawia modul z ktorego bedziemy korzystac
        """
        self.module = module
        print(f"\nCurrent module: {self.module}\n")
        self.url = f"https://{self.device['host']}:{self.device['restconf_port']}/restconf/data/{self.module}"


    def get(self, module):
        """
        wykonujemy zapytanie GET
        """
        self.set_module(module)
        request = requests.get(
            self.url, headers=self.headers, auth=(self.device['username'], self.device['password'])
        ).text
        print(json.dumps(json.loads(request), indent=4, sort_keys=True))

    def put(self, module):
        """
        wykonujemy zapytanie PUT (edycja)
        """
        self.set_module(module)
        requests.put(
            self.url, headers=self.headers, auth=(self.device['username'], self.device['password'])
        )
        self.get(module)
