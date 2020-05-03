import requests
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import logging

app = Flask(__name__)
api = Api(app)

# file_handler = logging.FileHandler('app.log')
# app.logger.addHandler(file_handler)
# app.logger.setLevel(logging.INFO)

app = Flask(__name__, template_folder="templates")

# include Controllers and APIs
from controllers import IndexController
from api import ReservationApi
from api import GuestApi
from api import RoomApi
from api import StayApi

# DATA STORE IN MEM
guests = None
rooms = None
reservations = None
stays = None


def initGuests():
    global guests
    guests = {"data": [
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


def initRooms():
    global rooms
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


def initReservations():
    global reservations
    reservations = {"data": [
        {'id': 10,
         'name': 'John Doe',
         'address': '123 Vine St',
         'City': 'CityVille.',
         'state': 'AL',
         'zip': '91222',
         'checkin': '07/05/2020',
         'checkout': '07/10/2020',
         'guests': 4,
         'roomType': 'queen',
         'roomClass': 'standard'},
        {'id': 11,
         'name': 'John Doe',
         'address': '123 Vine St',
         'City': 'CityVille.',
         'state': 'AL',
         'zip': '91222',
         'checkin': '07/05/2020',
         'checkout': '07/10/2020',
         'guests': 4,
         'roomType': 'queen',
         'roomClass': 'standard'},
        {'id': 12,
         'name': 'John Doe',
         'address': '123 Vine St',
         'City': 'CityVille.',
         'state': 'AL',
         'zip': '91222',
         'checkin': '07/05/2020',
         'checkout': '07/10/2020',
         'guests': 4,
         'roomType': 'queen',
         'roomClass': 'standard'}
    ]}


def initStays():
    global stays
    stays = {"data": [
        {"id": 10,
         "resid": 10,
         "roomid": 10,
         "custid": 10},
        {"id": 11,
         "resid": 11,
         "roomid": 11,
         "custid": 11},
        {"id": 12,
         "resid": 12,
         "roomid": 12,
         "custid": 12}
    ]}


def main():
    print('********************** STARTING STANDALONE ***************************')
    print('''
        Welcome to a partial simulation of a Hotel Management System
        
        This simulation uses Flask and runs a Flask server which provides a webserver
        use to expose RESTfull APIS.  Partial implementation of certain classes will be 
        demonstrated. No GUI interface provided.
         
         What is create with flask:
         1.  RESTful APIs
            - AuthenticationApi
            - ReservationApi
            - GuestApi
            - RoomApi'
            - StayApi
         
        ***  A test file, Tester.py, is provides and must be run separately 
    ''')
    print('**********************************************************************')
    initGuests()
    initReservations()
    initRooms()
    initStays()
    app.run(debug=True, use_reloader=False)

main()
