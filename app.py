from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <h1>Kamal Ghimire</h1>
    '''



    if __name__ == '__main__':
        app.run(debug=True, port=8000, host='127.0.0.1')