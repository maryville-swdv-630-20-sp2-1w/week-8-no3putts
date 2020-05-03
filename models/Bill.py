from sqlalchemy import Float

from models.CommonModel import *

# THIS IS WHAT A TYPICACAL MODEL SHOULD LOOK LIKE THAT MAPS TO A TABLE VIA ORM
class Biil(Base):
    def __init__(self, custid, stayid, extras, roomCharge, tax ):
        self.custid = custid
        self.stayid = stayid
        self.extras = extras
        self.roomCharge = roomCharge
        self.subtotal = 0.00
        self.tax = tax
        self.total = 0.0

    __tablename__ = 'customer'

    # FILEDS
    id = Column(Integer, primary_key=True)
    custid = Column(Integer)
    stayid = Column(Integer)
    extras = Column(Float)
    roomCharge = Column(Float)
    tax = Column(Float)

    def getInfo(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()