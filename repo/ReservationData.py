# Mimic Some Data store
from CustomExceptions import NoRoomFoundException
from models.Room import Room
import app


class ReservationData:
    # Create some test data for our catalog in the form of a list of dictionaries.
    def __init__(self):
        pass

    def findRoomByType(self, type):
        rec = ([a for a in app.reservations['data'] if a['type'] == type])
        return self.__mapToRoom(rec)

    def findRoomByBed(self, brand):
        rec = ([a for a in self.reservations['data'] if a['brand'] == brand])
        return self.___mapToRoom(rec)

    def __mapToRoom(self, rec):
        if rec != "":
            room = Room(rec[0]['id'], rec[0]['name'], rec[0]['brand'], rec[0]['beds'], rec[0]['bedtype'],
                        rec[0]['type'],
                        rec[0]['available'])
        else:
            raise NoRoomFoundException("Sorry, no room found")

        return room
