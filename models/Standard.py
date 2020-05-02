from models.Room import Room


class Standard(Room):
    def __init__(self, name, description, bedType="Beautyrest"):
        Room.__init__(self, name, description)
        self.beds = 2
        self.bedType = bedType
