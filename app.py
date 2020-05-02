from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import logging

app = Flask(__name__)
api = Api(app)

file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

app = Flask(__name__, template_folder="templates")

# include Controllers and APIs
from controllers import IndexController
from api import ReservationController
from api import AccountController
from api import RoomController


# If we're running in stand alone mode, run the application
# if __name__ == '__main__':
def main():
    print('******************************************')
    app.run(debug=True)

    # res = requests.post('http://localhost:5000/api/add_message/1234', json={"mytext": "lalala"})


main()
