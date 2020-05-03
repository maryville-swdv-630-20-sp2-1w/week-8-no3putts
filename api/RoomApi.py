from app import *

from service.RoomService import RoomService


class RoomApi:
    def __init__(self):
        self.roomService = RoomService()


@app.route('/api/room/type/<type>', methods=['GET'])
def findRoomByType(type):
    room = RoomApi()
    rec = room.roomService.findByType(type)

    if rec is not None:
        return jsonify(rec.__dict__)
    else:
        return "No room found"


@app.route('/api/room/bed/brand/<brand>', methods=['GET'])
def findRoomByBrand(brand):
    room = RoomApi()
    rec = room.roomService.findByBrand(brand)

    if rec is not None:
        return jsonify(rec)
    else:
        return "No room found"


@app.route('/api/room/available', methods=['GET'])
def availability():
    room = RoomApi()
    recs = room.roomService.availability()

    if recs is not None:
        return jsonify(recs)
    else:
        return "No available rooms found"
