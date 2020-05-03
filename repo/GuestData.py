from CustomExceptions import NoRoomFoundException
from models.Guest import Guest
from models.Room import *

# Mimic Some Data store
class GuestData:
    # Create some test data for our catalog in the form of a list of dictionaries.
    def __init__(self):
        self.guests = profile = {"data": [
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

    def createProfile(self, data):
        self.guests["data"].append(data)

    def findGuestById(self, name):
        rec = ([a for a in self.guests['data'] if a['id'] == id])
        return self.___mapToGuest(rec)

    def findGuestByName(self, name):
        rec = ([a for a in self.guests['data'] if a['name'].lower() == name.lower()])
        return self.___mapToGuest(rec)

    def findGuestByEmail(self, email):
        rec = ([a for a in self.guests['data'] if a['email'].lower() == email.lower()])
        return self.___mapToGuest(rec)

    def findGuestByPhone(self, phone):
        rec = ([a for a in self.guests['data'] if a['phone'].lower() == phone.lower()])
        return self.___mapToGuest(rec)



    def __mapToGuest(self, rec):
        if rec is not None:
            guest = Guest(rec[0]['id'], rec[0]['name'], rec[0]['address'], rec[0]['city'], rec[0]['state'],
                        rec[0]['zip'], rec[0]['email'],rec[0]['phone'])
        else:
            raise NoRoomFoundException("Sorry, no guest record found")

        return guest
