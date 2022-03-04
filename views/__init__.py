from flask import Flask

app = Flask(__name__, static_url_path='/ml-data')

from views import views
