from . import app

@app.route('/')
def index():
	return('index.html')