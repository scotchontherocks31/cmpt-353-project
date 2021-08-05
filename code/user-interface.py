import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim

def valid(address):
    pass

def main():
    locator = Nominatim(user_agent='user-interface.py')
    address = input("Enter your current address: ")

    # leaving validation for later
    # while True:
    #     address = input("Enter your current address: ")
    #     if valid(address):
    #         break
    #     else:
    #         print('Invalid address given.\n')
    
    print(f'Given address: {address}')

    location = locator.geocode(address)
    print(f'Translated address using GeoPy: {location.address}')
    print(f'Lat-long co-ordinates from given address: {location.latitude}, {location.longitude}')

    return

if __name__ == '__main__':
    main()
