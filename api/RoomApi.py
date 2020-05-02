from json import dumps as jsonstring
from flask import json

from app import *

from service.RoomService import RoomService

rooms = {"data": [
    {"id": 10,
     "name": "Grand Suite",
     "brand": "Saatva",
     "beds": 1,
     "bedtype": "king",
     "type": "luxury",
     "available": 1},
    {"id": 12,
     "name": "Garden Room",
     "brand": "Beautyrest",
     "beds": 2,
     "bedtype": "queen",
     "type": "deluxe",
     "available": 5},
    {"id": 13,
     "name": "Standard Room",
     "brand": "Tempurpedic",
     "beds": 2,
     "bedtype": "double",
     "type": "standard",
     "available": 0}
]}


class RoomApi:
    def __init__(self):
        self.roomService = RoomService()


@app.route('/room/type/<type>', methods=['GET'])
def findRoomByType(type):
    room = RoomApi()
    rec = room.roomService.findByType(type)

    # rec = ([a for a in rooms['data'] if a['type'] == type])
    print(rec)
    if rec is not None:
        return jsonify(rec.__dict__)
    else:
        return "No record found"


@app.route('/room/bed/brand/<brand>', methods=['GET'])
def findRoomByBrand(brand):
    rec = ([a for a in rooms['data'] if a['brand'] == brand])

    if rec is not None:
        return jsonify(rec)
    else:
        return "No record found"


@app.route('/room/available', methods=['GET'])
def availability():
    app.logger.info('Checking Availability')

    room = RoomApi()
    recs = room.roomService.availabiloty()

    if recs is not None:
        return jsonify(recs)
    else:
        return "No available rooms found"
