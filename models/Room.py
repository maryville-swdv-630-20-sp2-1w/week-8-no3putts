from models.CommonModel import *
from util.Database import *


class Room(Base):
    def __init__(self, name, brand, beds, bedType, type):
        self.name = name
        self.bedBrand = brand
        self.beds = beds
        self.bedType = bedType
        self.type = type

    __tablename__ = 'room'

    # FILEDS
    id = Column(Integer, primary_key=True)
    name = Column(String)
    bedBrand = Column(String)
    beds = Column(Integer)
    bedType = Column(String)
    type = Column(String)
