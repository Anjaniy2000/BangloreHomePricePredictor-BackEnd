from flask import jsonify

import mlFunctions
import authFunctions


def get_location_names():
    response = jsonify({
        'locations': mlFunctions.get_location_names()
    })
    # response.headers.add('Access-Control-Allow-Origin', '*')

    return response


def predict_home_price(total_sqft, location, bhk, bath, balcony):
    response = jsonify({
        'estimated_price': mlFunctions.get_estimated_price(location, total_sqft, bhk, bath, balcony)
    })
    # response.headers.add('Access-Control-Allow-Origin', '*')

    return response


def registration(email_address, password):
    flag = authFunctions.registration(email_address, password)

    if flag == 1:
        response = jsonify({
            'response_text': 'Successful'
        })
        # response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    else:
        response = jsonify({
            'response_text': 'Failed'
        })
        # response.headers.add('Access-Control-Allow-Origin', '*')

        return response


def login(email_address, password):
    flag = authFunctions.login(email_address, password)

    if flag == 1:
        response = jsonify({
            'response_text': 'Successful'
        })
        # response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    else:
        response = jsonify({
            'response_text': 'Failed'
        })
        # response.headers.add('Access-Control-Allow-Origin', '*')

        return response
