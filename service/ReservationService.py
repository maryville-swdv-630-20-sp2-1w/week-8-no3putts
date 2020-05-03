from CustomExceptions import ReservationNotFoundException
from repo.ReservationData import ReservationData


class ReservationService:
    def __init__(self):
        self.reservation = ReservationData()

    def createReservation(self, data):
        self.reservation.createReservation(data)

    def findReservationById(self, id):
        try:
            return self.reservation.findReservationById(id)
        except ReservationNotFoundException:
            raise ReservationNotFoundException("reservation not found")

    def findAllReservations(self):
        return self.reservation.findAllReservation()

    def cancelReservation(self, id):
        self.reservation.deleteReservation(id)

    def updateReservation(self, data):
        pass
