from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["100 per day"])

@app.route('/')
def index():
    return 'Welcome to my API!'

@app.route('/hello')
@limiter.limit("10 per hour")
def hello():
    return 'Hello, world!'

@app.route('/data', methods=['POST'])
@limiter.limit("50 per day")
def create_data():
    data = request.get_json()
    # Process the data and store it somewhere
    return jsonify({'message': 'Data created successfully.'})

@app.route('/data/<id>', methods=['PUT'])
@limiter.limit("25 per day")
def update_data(id):
    data = request.get_json()
    # Update the data with the given ID
    return jsonify({'message': f'Data with ID {id} updated successfully.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
