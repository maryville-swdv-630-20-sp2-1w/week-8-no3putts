from flask import render_template
from app import app

# Create a URL route in our application for "/"  default to index.html
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    # return render_template('index.html', name ='Jerrie')
    return render_template('index.html')

#
# # If we're running in stand alone mode, run the application
# if __name__ == '__main__':
#     app.run(debug=True)