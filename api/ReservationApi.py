from HRMApp import *
from service.ReservationService import ReservationService


class ReservationApi:
    def __init__(self):
        self.reservationService = ReservationService()


reservationApi = ReservationApi()


@app.route('/api/reservation', methods=['POST'])
def reserve():
    req_data = request.get_json()
    reservationApi.reservationService.createReservation(req_data)

    return "Added reservation id: {0} for guest: {1} with a {2} room.".format(req_data["id"],
                                                                              req_data["guestid"], req_data["roomType"])


@app.route('/api/reservation/cancel/<id>', methods=['DELETE'])
def cancel(id):
    return reservationApi.reservationService.cancelReservation(id)


@app.route('/api/reservation/<id>', methods=['GET'])
def info(id):
    return jsonify(reservationApi.reservationService.findReservationById(id).__dict__)


@app.route('/api/reservation', methods=['GET'])
def findAll():
    return reservationApi.reservationService.findAllReservations()
