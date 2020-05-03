from HRMApp import *

from service.RoomService import RoomService


class RoomApi:
    def __init__(self):
        self.roomService = RoomService()


room = RoomApi()

@app.route('/api/room/type/<type>', methods=['GET'])
def findRoomByType(type):
    rec = room.roomService.findByType(type)

    if rec is not None:
        return jsonify(rec.__dict__)
    else:
        return "No room found"


@app.route('/api/room', methods=['GET'])
def findAllRooms():
    rec = room.roomService.findAllRoom()

    if rec is not None:
        return jsonify(rec)
    else:
        return "No rooms found"


@app.route('/api/room/bed/brand/<brand>', methods=['GET'])
def findRoomByBrand(brand):
    rec = room.roomService.findByBrand(brand)

    if rec is not None:
        return jsonify(rec)
    else:
        return "No room found"


@app.route('/api/room/available', methods=['GET'])
def availability():
    recs = room.roomService.availability()

    if recs is not None:
        return jsonify(recs)
    else:
        return "No available rooms found"
