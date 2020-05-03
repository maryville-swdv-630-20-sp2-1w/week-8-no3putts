from flask import Flask, jsonify, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

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
         "city": "cityVille.",
         "state": "AL",
         "zip": "91222",
         "email": "jd@doe.com",
         "phone": "888-555-1212"},
        {"id": 11,
         "name": "John Doe II",
         "address": "123 Vine St",
         "city": "cityVille.",
         "state": "AL",
         "zip": "91222",
         "email": "jd@doe.com",
         "phone": "888-555-1212"},
        {"id": 12,
         "name": "John Doe III",
         "address": "123 Vine St",
         "city": "cityVille.",
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
        {"id": 10,
         "checkin": "12/12/2020",
         "checkout": "12/25/2020",
         "roomType": "Deluxe",
         "guestid": "10"},
        {"id": 11,
         "checkin": "12/12/2020",
         "checkout": "12/25/2020",
         "roomType": "Standard",
         "guestid": "11"},
        {"id": 12,
         "checkin": "12/12/2020",
         "checkout": "12/25/2020",
         "roomType": "Luxury",
         "guestid": "12"}
    ]}


def initStays():
    global stays
    stays = {"data": [
        {"id": 10,
         "resid": 10,
         "roomid": 10,
         "guestid": 10,
         "in": "12/22/2020",
         "out": ""},
        {"id": 11,
         "resid": 11,
         "roomid": 11,
         "guestid": 11,
         "in": "12/13/2020",
         "out": "12/16/2020"},
        {"id": 12,
         "resid": 12,
         "roomid": 12,
         "guestid": 12,
         "in": "11/02/2020",
         "out": "11/08/2020"}
    ]}


def main():
    print('********************** STARTING FLASK SERVER ***************************')
    print('''
        Welcome to a partial simulation of a Hotel Management System
        
        This simulation uses Flask and runs a Flask server which provides a web server
        to expose RESTfull APIS.  Partial implementation of certain classes will be 
        demonstrated. For an in-memory database, a Dictionary is used.  No GUI interface 
        provided.
         
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
