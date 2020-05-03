import json
import pprint

import requests


def showAllGuest():
    print('*********  Guest Records *********')
    res = requests.get('http://127.0.0.1:5000/api/guest')
    pprint.pprint(json.loads(res.content))


def showAllRooms():
    print('*********  Room Records *********')
    res = requests.get('http://127.0.0.1:5000/api/room')
    pprint.pprint(json.loads(res.content))


def showAllReservations():
    print('*********  Reservation Records *********')
    res = requests.get('http://127.0.0.1:5000/api/reservation')
    pprint.pprint(json.loads(res.content))


def showAllHotelStays():
    print('*********  Hotel Stay Records *********')
    res = requests.get('http://127.0.0.1:5000/api/stay')
    pprint.pprint(json.loads(res.content))


def printJson(data):
    pprint.pprint(json.loads(data))


def guestTest(model):
    print('********************** RUNNING {} TEST ***************************'.format(model))
    url = 'http://127.0.0.1:5000/api/guest'

    showAllGuest()

    print('\n**** Adding {} Record ****'.format(model))
    jsonTxt = {
        "id": 17,
        "name": "John Doe",
        "address": "123 Vine St",
        "city": "CityVille.",
        "state": "AL",
        "zip": "91222",
        "email": "jd@doe.com",
        "phone": "888-555-1212"
    }

    res = requests.post(url, json=jsonTxt)
    print(res.content)
    showAllGuest()

    print('**** Retrieve {} Record 17 ****'.format(model))
    printJson(requests.get(url + '/17').content)

    print('**** Deleting {} Record 17 ****'.format(model))
    requests.delete(url + '/17')
    showAllGuest()
    print('\n********************* END RUNNING {} TEST *************************\n'.format(model))


def roomTest(model):
    print('********************** RUNNING {} TEST ***************************'.format(model))
    url = 'http://127.0.0.1:5000/api/room'
    showAllRooms()

    print('\n**** Find {} Record by type: deluxe ****'.format(model))
    res = requests.get(url + '/type/deluxe')
    printJson(res.content)

    print('\n**** Find {}: All Available ****'.format(model))
    res = requests.get(url + '/available')
    printJson(res.content)

    print('\n********************* END RUNNING {} TEST *************************\n'.format(model))


def reservationTest(model):
    print('********************** RUNNING {} TEST ***************************'.format(model))
    url = 'http://127.0.0.1:5000/api/reservation'
    showAllReservations()

    print('\n**** Adding {} Record ****'.format(model))
    jsonTxt = {
        "id": 15,
        "checkin": "12/12/2020",
        "checkout": "12/25/2020",
        "roomType": "Deluxe.",
        "guestid": "10"
    }

    res = requests.post(url, json=jsonTxt)
    print(res.content)
    showAllReservations()

    print('**** Retrieve {} Record 15 ****'.format(model))
    printJson(requests.get(url + '/15').content)

    print('**** Deleting {} Record 15 ****'.format(model))
    requests.delete(url + '/15')
    showAllGuest()

    print('\n********************* END RUNNING {} TEST *************************\n'.format(model))


def hotelStayTest(model):
    print('********************** RUNNING {} TEST ***************************'.format(model))
    url = 'http://127.0.0.1:5000/api/stay'
    showAllHotelStays()

    print('\n**** Checking in Reservation 11  ****')
    print('''
        Checkin process is a Facade which does a few things.  Here is the code:
        
                res = self.reservation.findReservationById(id)
                guestid = res.guestid
                roomType = res.roomType
                
                room = self.room.findRoomByType(roomType)
                roomid = room.id
    
                stayid  =  random.randint(100, 1000)
                
                gName = self.guest.findGuestById(guestid)
        
                stayData = {"id": stayid, "resid": id, "roomid": roomid, "guestid": guestid,
                            "in": datetime.now().strftime("%m/%d/%Y"), "out": ""}
        
                self.stay.checkin(stayData)          
    ''')
    res = requests.post(url + "/in/11")
    print(res.content)
    showAllHotelStays()

    print('\n********************* END RUNNING {} TEST *************************\n'.format(model))


def main_loop():
    while True:
        print('\n\n***********************************************************')
        print('''                    TEST RUNNER MENU                   ''')
        print('***********************************************************')
        print('Pick a test to run')
        print('[1] Guest Management')
        print('[2] Reservation')
        print('[3] Room Management')
        print('[4] Hotel Stay - multiple steps')
        print('--------------------')
        print('[5] exit')

        print()
        choice = input('Make a your selection: ')
        if choice == '1':
            guestTest("Guest")
        elif choice == '2':
            reservationTest("Reservation")
        elif choice == '3':
            roomTest("Room")
        elif choice == '4':
            hotelStayTest("Hotel Stay")
        elif choice == '5':
            exit()


def main():
    print('********************** STARTING TEST CASES ***************************')
    print('''
            Welcome to a partial simulation of a Hotel Management System

            This simulation uses Flask and runs a Flask server which provides a web server
            use to expose RESTfull APIS.  

            What is included with these test:
             1. Guest Creation
             2. Reservation Creation 
             3. Reservation Cancellation
             4. Room availability Check
             5. Room Search
             6. Checkin
        ''')
    choice = input('press any key to continue...')
    main_loop()


main()
