from web_app import app

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'