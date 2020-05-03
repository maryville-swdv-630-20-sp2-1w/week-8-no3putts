import jsobj as jsobj
from flask import json

from app import *

@app.route('/login', methods=['GET'])
def login():
    return "Login Successful"

