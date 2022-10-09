"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Planet, People
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

@api.route('/api/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    user = User.query.get(user.id)
    return jsonify(user.serialize()), 200

@api.route('/api/users/<int:user_id>', methods=['PUT'])
def update_one_user(user_id):
    if first_name in request.body:
        user.first_name = request.body["first_name"]
    if last_name in request.body:
        user.last_name = request.body["last_name"]
    if "email" in request.body:
        user.email = request.body["email"]
    db.session.commit()
    return jsonify(user.serialize()), 200  

@api.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_people(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.serssion.commit()
    return f"a user has been deleted"


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

@api.route('/api/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet(request):
    planet = Planet.query.get(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return f"A planet has been deleted"

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

@api.route('/api/people/<int:people_id>', methods=['DELETE'])
def delete_person(people_id):
    people = People.query.get(people_id)
    db.session.delete(people)
    db.session.commit()
    return f"A person has been deleted"

@api.route('/api/favorite/planet/<int:planet_id>', methods=['POST'])
def create_favorite_planet(planet_id):
    request_body = request.get_json(),
    new_planet = Planet.query.get(planet_id)(
        name=request_body['name'],
        population=request_body['population'],
        terrain=request_body['terrain'],
        climate=request_body['climate'],
    )
    db.session.add(new_planet)
    db.session.commit()
    return f"A new favorite planet has been added"

@api.route('/api/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(request):
    planet = Planet.query.get(planet_id)
    db.session.delete(planet)
    db.session.commit()
    return f"a favorite planet has been deleted"

@api.route('/api/favorite/people/<int:person_id>', methods=['POST'])
def create_favorite_people(person_id):
    request.body = request.get_json()
    new_favroite_person = People.query.get(person_id)(
        name = request_body['name'],
        gender = request_body['gender'],
        skin_color = request_body['skin_color'],
        eye_color = request_body['eye_color'],
        height = request_body['height']
    )
    db.session.add(new_favroite_person)
    db.session.commit()
    return f"a new favorite person has been added"

@api.route('/api/favorite/people/<int:person_id>', methods=['DELETE'])
def delete_favorite_people(request):
    people = People.query.get(person_id)
    db.session.delete(people)
    db.session.commit()
    return f"a favorite person has been deleted"