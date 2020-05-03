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


@app.route('/api/profile/<custid>', methods=['PUT'])
def updateProfile(custid):
    app.logger.info('Update profile Successful')
    return "Update profile Successful"


@app.route('/api/profile/<custid>', methods=['DELETE'])
def deleteProfile(custid):
    app.logger.info('Update profile Successful')
    return "Update profile Successful"


@app.route('/api/profile/all', methods=['GET'])
def getAllProfile():
    app.logger.info(jsonify(profile))
    return jsonify(profile)


@app.route('/api/profile/<custid>', methods=['GET'])
def getProfile(custid):
    app.logger.info("Getting Profile for id: {}".format(custid))
    rec = ([a for a in profile['data'] if a['id'] == int(custid)])

    if rec != "":
        return jsonify(rec)
    else:
        return "No record found"
