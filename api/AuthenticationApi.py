import jsobj as jsobj
from flask import json

from HRMApp import *


class Authentication:
    pass


@app.route('/api/login', methods=['GET'])
def login():
    return "Login Successful"
