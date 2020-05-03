# Mimic Some Data store
from CustomExceptions import ReservationNotFoundException
import HRMApp
from models.Reservation import Reservation


class ReservationData:
    # Create some test data for our catalog in the form of a list of dictionaries.
    def __init__(self):
        pass

    def createReservation(self, data):
        HRMApp.reservations["data"].append(data)

    def deleteReservation(self, id):
        for i in range(len(HRMApp.reservations['data'])):
            if HRMApp.reservations['data'][i]['id'] == int(id):
                del HRMApp.reservations['data'][i]
                break

    def findAllReservation(self):
        return HRMApp.reservations

    def findReservationById(self, id):
        rec = ([a for a in HRMApp.reservations['data'] if a['id'] == int(id)])
        return self.__mapToReservation(rec)

    def findRoomByGuestId(self, id):
        rec = ([a for a in self.reservations['data'] if a['guestid'] == int(id)])
        return self.__mapToReservation(rec)

    def __mapToReservation(self, rec):
        if rec is not None and rec.__len__() > 0:
            res = Reservation(rec[0]['id'], rec[0]['checkin'], rec[0]['checkout'], rec[0]['roomType'], rec[0]['guestid'])
        else:
            raise ReservationNotFoundException("Sorry, no reservation found")

        return res
