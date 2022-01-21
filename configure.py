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
        ustawia modul/lisc z ktorego bedziemy korzystac
        """
        self.module = module
        self.url = f"https://{self.device['host']}:{self.device['restconf_port']}/restconf/data/{self.module}"


    def get(self, module):
        """
        wykonujemy zapytanie GET
        """
        try:
            self.set_module(module)
            request = requests.get(
                self.url, headers=self.headers, auth=(self.device['username'], self.device['password'])
            ).text
            #https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-native:native/version
            print(json.dumps(json.loads(request), indent=4, sort_keys=True))
        except Exception:
            print("\nSomething went wrong")

    def post(self, module, packet):
        """
        wykonujemy zapytanie POST (kreacja)
        """
        try:
            self.set_module(module)
            packet = json.dumps(packet)
            post = requests.post(
                self.url, data=packet, headers=self.headers, auth=(self.device['username'], self.device['password'])
            )
            print(post.text)
            print("\nRequest Successful")
        except Exception:
            print("\nSomething went wrong")

    def put(self, module, packet):
        """
        wykonujemy zapytanie PUT (edycja)
        """
        try:
            self.set_module(module)
            packet = json.dumps(packet)
            put = requests.put(
                self.url, data=packet, headers=self.headers, auth=(self.device['username'], self.device['password'])
            )
            print(put.text)
            print("\nRequest Successful")
        except Exception:
            print("\nSomething went wrong")

    def delete(self, module):
        """
        wykonujemy zapytanie DELETE (edycja)
        """
        try:
            self.set_module(module)
            requests.delete(
                self.url, headers=self.headers, auth=(self.device['username'], self.device['password'])
            )
            print("\DELETE Request Successful")
        except Exception:
            print("\nSomething went wrong")