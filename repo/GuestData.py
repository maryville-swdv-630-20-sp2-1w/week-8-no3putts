from CustomExceptions import NoRoomFoundException, NoGuestFoundException
from models.Guest import Guest
import HRMApp


# Mimic Some Data store
class GuestData:
    def __init__(self):
        pass

    def createProfile(self, data):
        HRMApp.guests["data"].append(data)

    def deleteProfile(self, id):
        for i in range(len(HRMApp.guests['data'])):
            if HRMApp.guests['data'][i]['id'] == int(id):
                del HRMApp.guests['data'][i]
                break

    def findAllGuest(self):
        return HRMApp.guests

    def findGuestById(self, id):
        rec = ([a for a in HRMApp.guests['data'] if a['id'] == int(id)])
        return self.__mapToGuest(rec)

    def findGuestByName(self, name):
        rec = ([a for a in HRMApp.guests['data'] if a['name'].lower() == name.lower()])
        return self.__mapToGuest(rec)

    def findGuestByEmail(self, email):
        rec = ([a for a in HRMApp.guests['data'] if a['email'].lower() == email.lower()])
        return self.__mapToGuest(rec)

    def findGuestByPhone(self, phone):
        rec = ([a for a in HRMApp.guests['data'] if a['phone'].lower() == phone.lower()])
        return self.__mapToGuest(rec)

    def __mapToGuest(self, rec):
        if rec is not None and rec.__len__() > 0:
            guest = Guest(rec[0]['id'], rec[0]['name'], rec[0]['address'], rec[0]['city'], rec[0]['state'],
                          rec[0]['zip'], rec[0]['email'], rec[0]['phone'])
        else:
            raise NoGuestFoundException("Sorry, no guest record found")

        return guest
