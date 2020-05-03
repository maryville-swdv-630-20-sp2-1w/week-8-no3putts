from CustomExceptions import NoRoomFoundException, NoGuestFoundException
from HRMApp import *

# Create some test data for our catalog in the form of a list of dictionaries.
from service.GuestService import GuestService


class GuestApi:
    def __init__(self):
        self.guestService = GuestService()


guestApi = GuestApi()


@app.route('/api/guest', methods=['POST'])
def createProfile():
    req_data = request.get_json()
    guestApi.guestService.createProfile(req_data)

    return "Added guest profile: {0}, name: {1} ".format(req_data["id"], req_data["name"])


@app.route('/api/guest', methods=['PUT'])
def updateProfile():
    return "Profile Update Successful"


@app.route('/api/guest/<id>', methods=['DELETE'])
def deleteProfile(id):
    guestApi.guestService.deleteProfile(id)
    return "Deleted record: {0}".format(id)


@app.route('/api/guest', methods=['GET'])
def getAllProfile():
    return jsonify(guestApi.guestService.findAllGuest())


@app.route('/api/guest/<id>', methods=['GET'])
def getProfile(id):
    try:
        return jsonify(guestApi.guestService.findProfileById(id).__dict__)
    except NoGuestFoundException:
        return "No rows found."
