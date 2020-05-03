from flask import render_template
from HRMApp import app

# THIS IS A SAMPLE CONTROLLER THAT INTERACTS WITH A FRONT HTML
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    # return render_template('index.html', name ='Jerrie')
    return render_template('index.html')
