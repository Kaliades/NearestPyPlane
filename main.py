import requests
from Challenge360FindTheNearestAeroplane import geodesic_distance
import json

r = requests.get('https://opensky-network.org/api/states/all')
decoded_data = r.json()

iterable = 0
longitudes = []
latitudes = []
while iterable < len(decoded_data["states"]):

    if decoded_data["states"][iterable][5] != None:
        longitudes.append(decoded_data["states"][iterable][5])
        longitudes.sort()

    if decoded_data["states"][iterable][6] != None:
        latitudes.append(decoded_data["states"][iterable][6])
        latitudes.sort()

    iterable += 1





