from flask import json
import HRMApp

from CustomExceptions import NoRoomFoundException, NoRoomAvailableException
from models.Room import *

# Mimic Some Data store
from models.Stay import Stay


class StayData:
    # Create some test data for our catalog in the form of a list of dictionaries.
    def __init__(self):
        pass

    def findAllStays(self):
        return HRMApp.stays

    def checkin(self, data):
        HRMApp.stays['data'].append(data)

    def checkout(self, id):
        rec = ([a for a in HRMApp.stays['data'] if a['stayid'] == int(id)])

        for i in range(len(HRMApp.stays['data'])):
            if HRMApp.stays['data'][i]['id'] == int(id):
                tmp =  HRMApp.reservations['data'][i]
                tmp['']
                break

    def __mapToStays(self, rec):
        if rec.__len__() > 0:
            stay = Stay(rec[0]['id'], rec[0]['name'], rec[0]['brand'], rec[0]['beds'], rec[0]['bedtype'],
                        rec[0]['type'],
                        rec[0]['available'])
        else:
            raise NoRoomFoundException("Sorry, no room found")

        return stay
