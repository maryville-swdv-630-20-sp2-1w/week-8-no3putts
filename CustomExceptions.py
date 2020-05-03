# define user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class NoRoomAvailableException(Error):
    print('No available rooms found')


class NoRoomFoundException(Error):
    print('No rooms found')


class NoGuestFoundException(Error):
    print('No guest found')


class ReservationNotFoundException(Error):
    print('Reservation rooms found')
