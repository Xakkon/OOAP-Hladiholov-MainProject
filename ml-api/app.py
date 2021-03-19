import datetime
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    # Конфлікт вирішено 19.03
    return jsonify('Змінено з IDE')


@app.route('/datetime', methods=['GET'])
def hello():
    return jsonify({'datetime': datetime.datetime.now().strftime('%H:%M:%S %d/%m/%Y')})


if __name__ == '__main__':
    app.run()
