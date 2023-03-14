from . import db

class Properties(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(256))
    no_rooms = db.Column(db.Integer)
    no_bathrooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    property_type = db.Column(db.String(80))
    location = db.Column(db.String(80))
    photo = db.Column(db.String(256))

    def __init__(self, title, description, no_rooms, no_bathrooms, price, property_type, location):
        self.title = title
        self.description = description
        self.no_rooms = no_rooms
        self.no_bathrooms = no_bathrooms
        self.price = price
        self.property_type = property_type
        self.location = location
        self.photo = location

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support