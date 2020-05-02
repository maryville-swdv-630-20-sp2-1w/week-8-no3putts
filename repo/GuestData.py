from CustomExceptions import NoRoomFoundException
from models.Room import *

# Mimic Some Data store
class RoomData:
    # Create some test data for our catalog in the form of a list of dictionaries.
    def __init__(self):
        self.guests = profile = {"data": [
            {"id": 10,
             "name": "John Doe",
             "address": "123 Vine St",
             "City": "CityVille.",
             "state": "AL",
             "zip": "91222",
             "email": "jd@doe.com",
             "phone": "888-555-1212"},
            {"id": 11,
             "name": "John Doe II",
             "address": "123 Vine St",
             "City": "CityVille.",
             "state": "AL",
             "zip": "91222",
             "email": "jd@doe.com",
             "phone": "888-555-1212"},
            {"id": 12,
             "name": "John Doe III",
             "address": "123 Vine St",
             "City": "CityVille.",
             "state": "AL",
             "zip": "91222",
             "email": "jd@doe.com",
             "phone": "888-555-1212"}
        ]}

    def findRoomByType(self, type):

        rec = ([a for a in self.guests['data'] if a['type'] == type])
        return self.__mapToRoom(rec)

    def findRoomByBed(self, brand):
        rec = ([a for a in self.guests['data'] if a['brand'] == brand])
        return self.___mapToRoom(rec)

    def __mapToRoom(self, rec):
        if rec != "":
            room = Room(rec[0]['id'], rec[0]['name'], rec[0]['brand'], rec[0]['beds'], rec[0]['bedtype'],
                        rec[0]['type'],
                        rec[0]['available'])
        else:
            raise NoRoomFoundException("Sorry, no room found")

        return room
