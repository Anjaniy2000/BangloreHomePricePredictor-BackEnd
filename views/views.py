from views import app
from controllers import controllers


@app.route('/')
def index():
    return "Welcome To Our Server"
