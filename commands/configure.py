"""
biblioteka do zapytan GET/POST
"""
import requests

class Controller:
    """
    handler zapytan
    """
    def __init__(self, addrIp, addrMask):
        self.addrIp = addrIp
        self.addrMask = addrMask
        print(self.addrIp, self.addrMask)

    def set(self):
        """
        TBE
        """
        url = 'https://www.w3schools.com/python/demopage.js'
        request = requests.get(url)
        print(request.json())
