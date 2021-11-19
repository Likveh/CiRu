"""
biblioteka do zapytan GET/POST
"""
import requests
import ipaddress


class Controller:
    """
    handler zapytan
    """
    def __init__(self, addrIp, addrMask):
        self.addrIp = addrIp
        self.addrMask = addrMask
        self.routers = []
        print(self.addrIp, self.addrMask)

    def markRouters(self, addrIpBegin, addrIpEnd, addrMask):
        addr = ipaddress.ip_network(addrIpBegin+addrMask)
        addrEnd = ipaddress.ip_network(addrIpEnd+addrMask)
        while addr < addrEnd:
            #ugly
            addr = ipaddress.ip_network(str(addr.broadcast_address + 1)+addrMask)
            self.routers.append(addr)

        print(self.routers)

    def set(self):
        """
        TBE
        """
        url = 'https://www.w3schools.com/python/demopage.js'
        request = requests.get(url)
        print(request.json())
        for network in self.routers:
            #set router ip to last host
            #and other stuff for every router - most likely call it's own def
            pass
