from views import app


@app.route('/')
def index():
    return "Welcome To Our Server"
