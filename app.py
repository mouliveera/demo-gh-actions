from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hellow_world():
    return '<h1 style="color:yellow">Hellow World!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

