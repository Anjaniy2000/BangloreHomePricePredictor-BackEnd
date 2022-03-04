import os

from views import app

port = int(os.environ.get('PORT', 8080))


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run(host='0.0.0.0', port=port, debug=True)
