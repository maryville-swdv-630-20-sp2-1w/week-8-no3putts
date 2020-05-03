from app import *

# Create some test data for our catalog in the form of a list of dictionaries.
reservation = [
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


@app.route('/api/stay/in/<resid>', methods=['POST'])
def checkin(resid):
    return jsonify(reservation)


@app.route('/api/stay/out/<resid>', methods=['PUT'])
def checkout(resid):
    return "Checkout " + id

