from CustomExceptions import NoGuestFoundException
from repo.GuestData import GuestData


class GuestService:
    def __init__(self):
        self.guestData = GuestData()

    def createProfile(self, data):
        return self.guestData.createProfile(data)

    def deleteProfile(self, id):
        return self.guestData.deleteProfile(id)

    def findAllGuest(self):
        return self.guestData.findAllGuest()

    def updateProfile(self, data):
        pass

    def findProfileById(self,  id):
        try:
            return self.guestData.findGuestById(id)
        except NoGuestFoundException:
            raise NoGuestFoundException("No record found")

    def findProfileByName(self, name):
        pass

    def findProfileByEmail(self, email):
        pass

    def findProfileByPhone(self,phone):
        pass