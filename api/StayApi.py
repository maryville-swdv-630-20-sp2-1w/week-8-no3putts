from HRMApp import *

from service.StayService import StayService


class StayApi:
    def __init__(self):
        self.stayService = StayService()


stayApi = StayApi()


@app.route('/api/stay/in/<resid>', methods=['POST'])
def checkin(resid):
    return stayApi.stayService.checkin(resid)


@app.route('/api/stay/out/<stayid>', methods=['PUT'])
def checkout(stayid):
    return stayApi.stayService.checkout(stayid)


@app.route('/api/stay', methods=['GET'])
def findAllStays():
    rec = stayApi.stayService.findAllStays()

    if rec is not None:
        return jsonify(rec)
    else:
        return "No rooms found"
