#No. 6 set up user.py
import models
from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from playhouse.shortcuts import model_to_dict

user = Blueprint('users', 'user')

@user.route('/register', methods =['POST'])
def register():
    payload = request.get_json() 
    payload['email']=payload['email'].lower()
    try:
        models.User.get(models.User.email == payload['email'])
        return jsonify(data={}, status={'code':401, 'message': 'A user with the same email already exists'})
    except models.DoesNotExist:
        payload['password']=generate_password_hash(payload['password'])
        user = models.User.create(**payload)
        login_user(user)
        user_dict = model_to_dict(user)
        # print(user_dict)
        del user_dict['password']
        return jsonify(data = user_dict, status = {'code': 201, 'message': 'success'}), 200

@user.route('/login', methods = ['POST'])
def login():
    payload = request.get_json()
    try:
        user = models.User.get(models.User.email == payload['email'])
        user_dict = model_to_dict(user)
        if(check_password_hash(user_dict['password'], payload['password'])):
            del user_dict['password']
            login_user(user)
            # print(user, 'this is user')
            return jsonify(data = user_dict, status={'code':200, 'message': 'success'}), 200
        else:
            return jsonify(data = {}, status={'code':401, 'message': 'email or password is not correct'}), 401
    except models.DoesNotExist:
        return jsonify(data = {}, status={'code':401, 'message': 'email or password is not correct'}), 401

#no.7 check current user or log out
@user.route('/logged_in_user', methods = ['GET'])
def get_logged_in_user():
    print(current_user)
    print(f'{current_user.email} is current_user.email in get logged_in_user')
    user_dict = model_to_dict(current_user)
    user_dict.pop('password')
    return jsonify(data = user_dict), 200

@user.route('/', methods = ['GET'])
def users_index():
    result = models.User.select()
    user_dicts = [model_to_dict(user) for user in result]
    return jsonify({
        'data': user_dicts,
        'message': f'successfully found {len(user_dicts)} users',
        'status':200
    }), 200

@user.route('/logout', methods = ['GET'])
def logout():
    logout_user()
    return jsonify(
        data={},
        message = 'Successfully logged out',
        status = 200
    ), 200