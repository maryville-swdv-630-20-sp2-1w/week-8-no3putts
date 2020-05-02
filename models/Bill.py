from models.CommonModel import *


class Customer(Base):
    def __init__(self, fname, lname, phone, email):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email

    __tablename__ = 'customer'

    # FILEDS
    id = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    phone = Column(String)
    email = Column(String)

    def getInfo(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()