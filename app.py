'''
Flask application : Server

'''


from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

data_store = {}

# HTML 페이지 렌더링
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post_example():
    data = request.get_json()
    user_id = data.get("user_id")
    if user_id:
        data_store[user_id] = data  
        response = {
            "message": "Data received",
            "data": data
        }
    else:
        response = {
            "message": "User ID is required"
        }
    return jsonify(response)

@app.route('/get', methods=['GET'])
def get_data():
    return jsonify(data_store)

@app.route('/reset', methods=['POST'])
def reset_data():
    global data_store
    data_store = {}  # 데이터 초기화
    return jsonify({"message": "Data store reset", "data_store": data_store})

if __name__ == '__main__':
    app.run(host='Mobina.access.ly', port=5000, ssl_context=('mycertificate.crt','myprivate.key'), debug=True)