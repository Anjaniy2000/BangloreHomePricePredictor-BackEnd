import os

from flask import Flask, request, jsonify
from backend import mlController

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome To Our Server"


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': mlController.get_location_names()
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
        'estimated_price': mlController.get_estimated_price(location, total_sqft, bhk, bath, balcony)
    })
    # response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting python Flask Server For Home Price Prediction...")
    mlController.load_saved_artifacts()
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
