from nasaapi import Client
from setting import NASA_API


class Nasa:
    def __init__(self):
        self.API = NASA_API
        self.client = Client(self.API)