from datetime import datetime
import random

from repo.GuestData import GuestData
from repo.ReservationData import ReservationData
from repo.RoomData import RoomData
from repo.StayData import StayData


class StayService:
    def __init__(self):
        self.stay = StayData()
        self.reservation = ReservationData()
        self.room = RoomData()
        self.guest = GuestData()

    def checkin(self, id):
        res = self.reservation.findReservationById(id)
        guestid = res.guestid
        roomType = res.roomType
        room = self.room.findRoomByType(roomType)
        roomid = room.id
        stayid  =  random.randint(100, 1000)
        gName = self.guest.findGuestById(guestid)

        stayData = {"id": stayid, "resid": id, "roomid": roomid, "guestid": guestid,
                    "in": datetime.now().strftime("%m/%d/%Y"), "out": ""}

        self.stay.checkin(stayData)

        return "Reservation {0} checked in  successfully.  Info: {1} ".format(id, gName.name)

    def checkout(self, id):
        return "Checkout Successful"

    def findAllStays(self):
        return self.stay.findAllStays()