import models.Room as Room


class RoomLoader:
    def __init__(self):
        pass

    @staticmethod
    def createRooms(database):
        session = database.session

        print('''
        Creating rooms:
         
        tmp = room('Grand Suite', 'Saatva', 1, 'king', 'luxury', 5)
        session.add(tmp)
        tmp = room('Garden Room', 'Beautyrest', 2, 'quuen', 'deluxe', 10)
        session.add(tmp)
        tmp = room('Standard Room', 'Beautyrest', 2, 'double', 'standard', 10)
        session.add(tmp)
        ''')

        tmp = Room('Grand Suite', 'Saatva', 1, 'king', 'luxury', 5)
        session.add(tmp)
        tmp = Room('Garden Room', 'Beautyrest', 2, 'quuen', 'deluxe', 10)
        session.add(tmp)
        tmp = Room('Standard Room', 'Tempurpedic', 2, 'double', 'standard', 20)
        session.add(tmp)

        session.commit()

        for row in session.query(Room).all():
            print('{:3} {}'.format(row.id, row.name))
