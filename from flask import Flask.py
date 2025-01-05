from flask import Flask
import time

app = Flask(__name__)

@app.route('/test')
def test():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=False, port=5000)
