import flask
import requests

app = flask.Flask(__name__)

port_map = {
    'add': 8000,
    'subtract': 8001,
    'multiply': 8002,
    'divide': 8003,
    'pow': 8004,
    'mod': 8005,
    'lt': 8006,
    'gt': 8007,
    'eq': 8008,
    'ne': 8009,
    'leq': 8010,
    'geq': 8011,
    'gcd': 8012,
}

@app.route('/', methods = ['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')

    num1 = float(flask.request.form.get('num1'))
    num2 = float(flask.request.form.get('num2'))
    operation = flask.request.form.get('operation')

    if operation not in port_map.keys():
        return 'Invalid Operation'

    url = f'http://{operation}:{port_map[operation]}/'
    result = requests.get(url, params = {
        'num1': num1,
        'num2': num2
    }).json()['result']
    
    return flask.render_template('index.html', result = {
        'num1': num1,
        'num2': num2,
        'operation': operation,
        'result': result if isinstance(result, bool) else round(result, 3)
    })

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = True)
