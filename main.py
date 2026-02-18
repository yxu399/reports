# Reports Generator Microservice
# main

from flask import Flask
from flask import request

app = Flask(__name__)


# arbitrary route for demonstration
@app.route('/')
def index():
    return 'Reports Index Page'


# arbitrary call to index()
index()

if __name__ == '__main__':
    app.run(debug=True)
