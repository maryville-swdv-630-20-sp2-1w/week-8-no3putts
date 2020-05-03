import jsobj as jsobj
from flask import json

from app import *

# Create some test data for our catalog in the form of a list of dictionaries.
from service.GuestService import GuestService

profile = {"data": [
    {"id": 10,
     "name": "John Doe",
     "address": "123 Vine St",
     "City": "CityVille.",
     "state": "AL",
     "zip": "91222",
     "email": "jd@doe.com",
     "phone": "888-555-1212"},
    {"id": 11,
     "name": "John Doe II",
     "address": "123 Vine St",
     "City": "CityVille.",
     "state": "AL",
     "zip": "91222",
     "email": "jd@doe.com",
     "phone": "888-555-1212"},
    {"id": 12,
     "name": "John Doe III",
     "address": "123 Vine St",
     "City": "CityVille.",
     "state": "AL",
     "zip": "91222",
     "email": "jd@doe.com",
     "phone": "888-555-1212"}
]}


class GuestApi:
    def __init__(self):
        self.guestService = GuestService()


@app.route('/api/guest', methods=['POST'])
def createProfile():
    guestApi = GuestApi()
    req_data = request.get_json()
    guest = guestApi.guestService.createProfile(req_data)

    # profile["data"].append(req_data)
    return "Added record: {0}, name: {1} ".format(req_data["id"], req_data["name"])


guestApi = GuestApi()

@app.route('/api/guest/<custid>', methods=['PUT'])
def updateProfile(custid):
    return "Update profile Successful"


@app.route('/api/guest/<id>', methods=['DELETE'])
def deleteProfile(id):
    guest = guestApi.guestService.deleteProfile(id)
    return "Deleted record: {0}, name: {1} ".format(guest["id"], guest["name"])


@app.route('/api/guest', methods=['GET'])
def getAllProfile():
    return jsonify(guestApi.guestService.findAllGuest())


@app.route('/api/guest/<custid>', methods=['GET'])
def getProfile(custid):
    rec = ([a for a in profile['data'] if a['id'] == int(custid)])

    if rec != "":
        return jsonify(rec)
    else:
        return "No record found"
