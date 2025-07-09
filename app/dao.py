import json


def load_user_data():
    with open('../data/users.json', 'r') as file:
        data = json.load(file)
    return data


def auth_user(username, password):
    user_data = load_user_data()
    for user in user_data:
        if user['username'] == username and user['password'] == password:
            return True
    return False

