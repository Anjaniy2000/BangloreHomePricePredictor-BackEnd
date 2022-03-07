import os

from flask import Flask, request, jsonify
from controllers import auth, ml

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome To Our Server"


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    email_address = request.form['email_id']
    password = request.form['password']

    response = jsonify({
        'response_text': auth.registrationController(email_address, password)
    })
    return response

    # flag = database_access_functions.registration(email_address, password)
    #
    # if flag == 1:
    #     response = jsonify({
    #         'response_text': 'Successful'
    #     })
    #     # response.headers.add('Access-Control-Allow-Origin', '*')
    #
    #     return response
    # else:
    #     response = jsonify({
    #         'response_text': 'Failed'
    #     })
    #     # response.headers.add('Access-Control-Allow-Origin', '*')
    #
    #     return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    email_address = request.form['email_id']
    password = request.form['password']

    response = jsonify({
        'response_text': auth.loginController(email_address, password)
    })
    return response

    # flag = database_access_functions.login(email_address, password)
    #
    # if flag == 1:
    #     response = jsonify({
    #         'response_text': 'Successful'
    #     })
    #     # response.headers.add('Access-Control-Allow-Origin', '*')
    #
    #     return response
    # else:
    #     response = jsonify({
    #         'response_text': 'Failed'
    #     })
    #     # response.headers.add('Access-Control-Allow-Origin', '*')
    #
    #     return response


#
#
# @app.route('/delete_account', methods=['GET', 'POST'])
# def delete():
#     email_address = request.form['email_id']
#
#     flag = database_access_functions.delete_account(email_address)
#
#     if flag == 1:
#         response = jsonify({
#             'response_text': 'Successful'
#         })
#         # response.headers.add('Access-Control-Allow-Origin', '*')
#
#         return response
#     else:
#         response = jsonify({
#             'response_text': 'Failed'
#         })
#         # response.headers.add('Access-Control-Allow-Origin', '*')
#
#         return response
#
#
# @app.route('/change_password', methods=['GET', 'POST'])
# def change_pwd():
#     email_address = request.form['email_id']
#     password_old = request.form['old_password']
#     password_new = request.form['new_password']
#
#     flag = database_access_functions.change_password(email_address, password_old, password_new)
#
#     if flag == 1:
#         response = jsonify({
#             'response_text': 'Successful'
#         })
#         # response.headers.add('Access-Control-Allow-Origin', '*')
#
#         return response
#     else:
#         response = jsonify({
#             'response_text': 'Failed'
#         })
#         # response.headers.add('Access-Control-Allow-Origin', '*')
#
#         return response
#
#
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': ml.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])

    response = jsonify({
        'estimated_price': ml.get_estimated_price(location, total_sqft, bhk, bath, balcony)
    })
    # response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
