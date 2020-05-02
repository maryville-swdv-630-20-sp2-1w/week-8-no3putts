from models.CommonModel import *


class Reservation(Base):
    def __init__(self, checkin, checkout, roomid, customerid):
        self.checkin = checkin
        self.checkout = checkout
        self.room = roomid
        self.customer = customerid


    __tablename__ = 'reservation'

    # FILEDS
    id = Column(Integer, primary_key=True)
    checkin = Column(String)
    checkout = Column(String)
    room = Column(String)
    customerid = Column(String)

    def getInfo(self):
        raise NotImplementedError()

    def cancel(self):
        raise NotImplementedError()
