__author__ = 'Brian Snyder'

class Contact:
    def __init__(self, name):
        self.name = name
        self.address = []

    def new_address(self, addr):
        self.address.append(addr)

