from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return jsonify({'message': 'Welcome...!'})

# Simple API route
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'Sample Data',
        'info': 'This is a sample API endpoint.'
    }
    return jsonify(data)

# Route to accept POST request
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({'received': data})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
