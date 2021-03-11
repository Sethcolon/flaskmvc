from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory

user_views = Blueprint('user_views', __name__, template_folder='../templates')

# Views cannot import models but can import controllers
from App.controllers import ( get_users, get_users_json, create_user )

@user_views.route('/api/users')
def client_app():
    users_json = get_users_json()
    return jsonify(users_json)

@user_views.route('/api/users', methods=['POST'])
def client_app():
    data = request.json
    create_user(data['firstName'], data['lastName'])
    return 'Created'  

@user_views.route('/users', methods=['GET'])
def get_user_page():
    return render_template('users.html', users=get_users())

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')