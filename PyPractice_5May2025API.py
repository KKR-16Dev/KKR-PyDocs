from flask import Flask,request,jsonify
import json

app = Flask(__name__)

users = {
    "id":1, "name":"Kishor Kumar R",
    "id":2, "name":"N Chaithra"
}

@app.route('/user', methods=['GET'])
def get_user_data():
    return jsonify(users)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_single_user(user_id):
    usr = (u for u in users if u['id'] == user_id)
    if usr:
        return jsonify(usr)
    return jsonify({"Error":"User not found"}),404

@app.route('/users', methods=['POST'])
def create_newuser():
    data = request.json()
    new_users = {
        'id':users[-1]['id']+1 if users else 1,
        'name':data['name']
    }
    return jsonify(new_users)


if __name__ == '__main__':
    app.run(debug = True)

print("Hello world From API")