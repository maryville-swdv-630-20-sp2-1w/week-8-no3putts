from app import *

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'name': 'John Doe',
     'address': '123 Vine St',
     'City': 'CityVille.',
     'state': 'AL',
     'zip': '91222',
     'checkin': '07/05/2020',
     'checkout': '07/10/2020',
     'guests': 4,
     'roomType': 'queen',
     'roomClass': 'standard'},
    {'id': 2,
     'name': 'John Doe',
     'address': '123 Vine St',
     'City': 'CityVille.',
     'state': 'AL',
     'zip': '91222',
     'checkin': '07/05/2020',
     'checkout': '07/10/2020',
     'guests': 4,
     'roomType': 'queen',
     'roomClass': 'standard'},
    {'id': 3,
     'name': 'John Doe',
     'address': '123 Vine St',
     'City': 'CityVille.',
     'state': 'AL',
     'zip': '91222',
     'checkin': '07/05/2020',
     'checkout': '07/10/2020',
     'guests': 4,
     'roomType': 'queen',
     'roomClass': 'standard'}
]


@app.route('/reservation', methods=['POST'])
def reserve():
    app.logger.info('Reservation Complete')
    return jsonify(books)


@app.route('/reservation/cancel/<id>', methods=['PUT'])
def cancel(id):
    return "Reservation " + id + " cancelled"


@app.route('/reservation/checkin/<id>', methods=['PUT'])
def checkin(id):
    return "Reservation " + id + " checkin"


@app.route('/reservation/checkout/<id>', methods=['PUT'])
def checkout(id):
    return "Reservation " + id + " checkout"
