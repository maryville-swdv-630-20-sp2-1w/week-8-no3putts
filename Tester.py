import json
import pprint

import requests


def showAllGuest():
    print('**** Current Guest Records ****')
    res = requests.get('http://127.0.0.1:5000/api/guest')
    pprint.pprint(json.loads(res.content))


def showAllRooms():
    print('**** Current Room Records ****')
    res = requests.get('http://127.0.0.1:5000/api/rooms')
    pprint.pprint(json.loads(res.content))


def guestTest(model):
    print('********************** RUNNING {} CREATION TEST ***************************'.format(model))
    url = 'http://127.0.0.1:5000/api/guest'

    showAllGuest()

    print('\n**** Adding {} Record ****'.format(model))
    jsonTxt = {
        "id": 17,
        "name": "John Doe",
        "address": "123 Vine St",
        "City": "CityVille.",
        "state": "AL",
        "zip": "91222",
        "email": "jd@doe.com",
        "phone": "888-555-1212"
    }

    res = requests.post(url, json=jsonTxt)
    print(res.content)
    showAllGuest()

    print('**** Deleting {} Record ****'.format(model))
    requests.delete(url + '/17')
    showAllGuest()


def roomTest(model):
    print('********************** RUNNING {} CREATION TEST ***************************'.format(model))
    url = 'http://127.0.0.1:5000/api/room'
    showAllGuest()

    print('\n**** Adding {} Record ****'.format(model))
    jsonTxt = {
        "id": 17,
        "name": "John Doe",
        "address": "123 Vine St",
        "City": "CityVille.",
        "state": "AL",
        "zip": "91222",
        "email": "jd@doe.com",
        "phone": "888-555-1212"
    }

    res = requests.post(url, json=jsonTxt)
    print(res.content)
    showAllGuest()

    print('**** Deleting {} Record ****'.format(model))
    requests.delete(url + '/17')
    showAllGuest()


def main():
    print('********************** STARTING STANDALONE ***************************')
    guestTest("Guest")


main()
