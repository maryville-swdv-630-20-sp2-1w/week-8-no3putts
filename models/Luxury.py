from models.Room import Room


class Luxury(Room):
    def __init__(self, name, description, bedType="Saatva"):
        Room.__init__(self, name, description)
        self.beds = 1
        self.bedType = bedType
