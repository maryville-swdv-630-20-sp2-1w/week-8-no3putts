from models.Room import Room


class Deluxe(Room):
    def __init__(self, name, description, bedType='TEMPUR-BREEZE'):
        Room.__init__(self, name, description)
        self.beds = 2
        self.bedType = bedType
