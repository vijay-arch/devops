from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"


@app.route('/app/user')
def user():
    user_info = {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }
    return jsonify(user_info)



if __name__ == "__main__":
    app.run(debug=True)