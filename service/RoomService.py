from repo.RoomData import RoomData


class RoomService:
    def __init__(self):
        self.roomData = RoomData()

    def findByType(self, type):
        return self.roomData.findRoomByType(type)