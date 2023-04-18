import flask

app = flask.Flask(__name__)

@app.route('/', methods = ['GET'])
def mod():
    num1 = float(flask.request.args.get('num1'))
    num2 = float(flask.request.args.get('num2'))
    return flask.jsonify({'result': num1 % num2})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8005, debug = True)
