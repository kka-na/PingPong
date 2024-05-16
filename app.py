'''
Flask application : Server

'''


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post_example():
    data = request.get_json()
    response = {
        "message": "Data received",
        "data": data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
