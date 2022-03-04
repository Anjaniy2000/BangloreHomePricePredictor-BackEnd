from flask import jsonify
import json

__locations = None
__data_columns = None
__model = None


def get_location_names():
    print("Loading Saved Artifacts.....Start")
    global __data_columns
    global __locations

    with open("Columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]  # first 4 columns are sqft, bath, bhk, balcony

    response = jsonify({
        'locations': __locations
    })
    # response.headers.add('Access-Control-Allow-Origin', '*')

    return response


# def getLocations():
#     return __locations
#
#
# def get_data_columns():
#     return __data_columns

# def predict_home_price(total_sqft, location, bhk, bath, balcony):
#     response = jsonify({
#         'estimated_price': mlFunctions.get_estimated_price(location, total_sqft, bhk, bath, balcony)
#     })
#     # response.headers.add('Access-Control-Allow-Origin', '*')
#
#     return response
#
#
# def login(email_address, password):
#     flag = authFunctions.login(email_address, password)
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
# def registration(email_address, password):
#     flag = authFunctions.registration(email_address, password)
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
