
import jsobj as jsobj
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

    if rec != "":
        return jsonify(rec)
    else:
        return "No record found"


@app.route('/room/brand/<brand>', methods=['GET'])
def findRoomByBed(brand):
    rec = ([a for a in rooms['data'] if a['brand'] == brand])

    if rec != "":
        return jsonify(rec)
    else:
        return "No record found"


@app.route('/room/available', methods=['GET'])
def availability():
    app.logger.info('Checking Availability')
    room_json = json.loads(json.dumps(rooms))

    avail_rooms = []
    for r in room_json['data']:
        if r['available'] > 0:
            avail_rooms.append(r)

    app.logger.info('Available Rooms')
    for x in avail_rooms:
        print(x)

    return jsonify(avail_rooms)


@app.route('/room/checkin/<id>', methods=['PUT'])
def book(id):
    req_data = request.get_json()


    profile["data"].append(req_data)
    return "Added record: {0}, name: {1} ".format(req_data["id"], req_data["name"])
