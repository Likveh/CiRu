"""
biblioteka do zapytan GET/POST
"""
import requests

class Controller:
    """
    handler zapytan
    """
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask
        print(self.ip, self.mask)

    def set(self):
        """
        TBE
        """
        url = 'https://www.w3schools.com/python/demopage.js'
        request = requests.get(url)
        print(request.json())
