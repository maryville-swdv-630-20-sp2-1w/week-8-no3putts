from flask import json

from CustomExceptions import NoRoomFoundException, NoRoomAvailableException
from models.Room import *
import app


# Mimic Some Data store
class RoomData:
    # Create some test data for our catalog in the form of a list of dictionaries.
    def __init__(self):
        pass

    def findRoomByType(self, type):
        rec = ([a for a in app.rooms['data'] if a['type'] == type])
        return self.__mapToRoom(rec)

    def findRoomByBrand(self, brand):
        rec = ([a for a in app.rooms['data'] if a['brand'] == brand])
        return self.___mapToRoom(rec)

    def availability(self):
        room_json = json.loads(json.dumps(app.rooms))

        avail_rooms = []
        for r in room_json['data']:
            if r['available'] > 0:
                avail_rooms.append(r)

        if avail_rooms.__len__() > 0:
            return avail_rooms
        else:
            raise NoRoomAvailableException("Sorry, no available rooms found")

    def __mapToRoom(self, rec):
        if rec.__len__() > 0:
            room = Room(rec[0]['id'], rec[0]['name'], rec[0]['brand'], rec[0]['beds'], rec[0]['bedtype'],
                        rec[0]['type'],
                        rec[0]['available'])
        else:
            raise NoRoomFoundException("Sorry, no room found")

        return room
