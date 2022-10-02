"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Planets, People
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

@api.route('/api/users', methods=['DELETE'])
def delete_people(request):
    db.session.delete(self)


@api.route('/api/planets', methods=['POST'])
def create_planet(request):
    request_body = request.get_json(),
    new_planet = Planet(
        name=request_body['name'],
        population=request_body['population'],
        terrain=request_body['terrain'],
        climate=request_body['climate'],
    )
    db.session.add(new_planet)
    db.session.commit()
    return f"A new planet has been added"

@api.route('/api/planets', methods=['GET'])
def get_planets(request):
    allPlanets = Planet.query.all()
    planetList = list(map(lambda x: x.serialize, allPlanets))
    
    return jsonify(planetList), 200

@api.route('/api/planet/delete', methods=['DELETE'])
def delete_planet(request):
    db.session.delete(self)



@api.route('/api/people', methods=['POST'])
def create_person(request):
    request_body = request.get_json(),
    new_person = Person(
        name=request_body['name'],
        gender=request_body['gender'],
        eye_color=request_body['eye_color'],
        skin_color=request_body['skin_color'],
        height=request_body['height']
    )
    db.session.add(new_person)
    db.session.commit()
    return f"A new person has been added"

@api.route('/api/people', methods=['GET'])
def get_people(request):
    allPeople = Person.query.all()
    personList = list(map(lambda x: x.serialize, allPeople))
    return jsonify(personList), 200

@api.route('/api/people/delete', methods=['DELETE'])
def delete_person(request):
    db.session.delete(self)
    return f"A new person has been deleted"