# define user-defined exceptions
from app import *


class Error(Exception):
    """Base class for other exceptions"""
    pass


class NoRoomAvailableException(Error):
    app.logger.info('No available rooms found')


class NoRoomFoundException(Error):
    app.logger.info('No rooms found')


class ReservationNotFoundException(Error):
    app.logger.info('Reservation rooms found')
