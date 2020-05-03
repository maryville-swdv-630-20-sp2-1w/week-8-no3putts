from CustomExceptions import NoRoomFoundException
from models.Guest import Guest
import app


# Mimic Some Data store
class GuestData:
    def __init__(self):
        pass

    def createProfile(self, data):
        app.guests["data"].append(data)

    def deleteProfile(self, id):
        rec = None
        for i in range(len(app.guests['data'])):
            if app.guests['data'][i]['id'] == int(id):
                rec = app.guests['data'][i]
                del app.guests['data'][i]
                break

        return self.__mapToGuest(rec)

    def findAllGuest(self):
        return app.guests

    def findGuestById(self, name):
        rec = ([a for a in self.guests['data'] if a['id'] == id])
        return self.__mapToGuest(rec)

    def findGuestByName(self, name):
        rec = ([a for a in self.guests['data'] if a['name'].lower() == name.lower()])
        return self.__mapToGuest(rec)

    def findGuestByEmail(self, email):
        rec = ([a for a in self.guests['data'] if a['email'].lower() == email.lower()])
        return self.__mapToGuest(rec)

    def findGuestByPhone(self, phone):
        rec = ([a for a in self.guests['data'] if a['phone'].lower() == phone.lower()])
        return self.__mapToGuest(rec)

    def __mapToGuest(self, rec):
        if rec is not None:
            guest = Guest(rec[0]['id'], rec[0]['name'], rec[0]['address'], rec[0]['city'], rec[0]['state'],
                          rec[0]['zip'], rec[0]['email'], rec[0]['phone'])
        else:
            raise NoRoomFoundException("Sorry, no guest record found")

        return guest
