from flask import request

from views import app
from controllers import controllers


@app.route('/')
def index():
    return "Welcome To Our Server"


# @app.route('/registration', methods=['GET', 'POST'])
# def registration():
#     email_address = request.form['email_id']
#     password = request.form['password']
#     return controllers.registration(email_address, password)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     email_address = request.form['email_id']
#     password = request.form['password']
#     return controllers.login(email_address, password)


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    return controllers.get_location_names()


# @app.route('/predict_home_price', methods=['GET', 'POST'])
# def predict_home_price():
#     total_sqft = float(request.form['total_sqft'])
#     location = request.form['location']
#     bhk = int(request.form['bhk'])
#     bath = int(request.form['bath'])
#     balcony = int(request.form['balcony'])
#     return controllers.predict_home_price(total_sqft, location, bhk, bath, balcony)
