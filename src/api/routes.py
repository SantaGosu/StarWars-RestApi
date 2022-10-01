"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Planets
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/api/users', methods=['POST'])
def create_user(request):
    request_body = request.get_json(),
    new_user = User(
        first_name=request_body['first_name'],
        last_name=request_body['last_name'],
        email=request_body['email'],
        password=request_body['password'],
        is_active=True
        )
    db.session.add(new_user)
    db.session.commit()
    return f"A new user has been added"

@api.route('/api/users', methods=['GET'])
def get_users(request):
    allUsers = User.query.all()
    userList = list(map(lambda x: x.serialize, allUsers))
    
    return jsonify(userList), 200