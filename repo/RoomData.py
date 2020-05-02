from flask import json
import jsonpickle
from models.Room import *


# Mimic Some Data store
class RoomData:
    # Create some test data for our catalog in the form of a list of dictionaries.
    def __init__(self):
        self.rooms = {"data": [
        {"id": 10,
         "name": "Grand Suite",
         "brand": "Saatva",
         "beds": 1,
         "bedtype": "king",
         "type": "luxury",
         "available": 1},
        {"id": 12,
         "name": "Garden Room",
         "brand": "Beautyrest",
         "beds": 2,
         "bedtype": "queen",
         "type": "deluxe",
         "available": 5},
        {"id": 13,
         "name": "Standard Room",
         "brand": "Tempurpedic",
         "beds": 2,
         "bedtype": "double",
         "type": "standard",
         "available": 0}
    ]}

    def findRoomByType(self, type):
        rec = ([a for a in self.rooms['data'] if a['type'] == type])

        if rec != "":
            return json.dumps(rec)
        else:
            raise Exception("Sorry, no room found")

    def findRoomByBed(self, brand):
        rec = ([a for a in self.rooms['data'] if a['brand'] == brand])

        if rec != "":
            return json.dumps(rec)
        else:
            raise Exception("Sorry, no room found")
