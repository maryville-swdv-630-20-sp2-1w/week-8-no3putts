from CustomExceptions import NoRoomFoundException, NoRoomAvailableException
from repo.RoomData import RoomData


class RoomService:
    def __init__(self):
        self.roomData = RoomData()

    def findByType(self, type):
        try:
            return self.roomData.findRoomByType(type)
        except NoRoomFoundException:
            print("No room found")
            return None

    def findByBrand(self, brand):
        try:
            return self.roomData.findRoomByBed(brand)
        except NoRoomFoundException:
            print("No room found")
            return None

    def findAllRoom(self):
        return self.roomData.findAllRooms()

    def availability(self):
        try:
            return self.roomData.availability()
        except NoRoomAvailableException:
            print("No available rooms found")
            return None
