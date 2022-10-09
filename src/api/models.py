from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), unique=False, nullable=False)
    last_name = db.Column(db.String(15), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    __tablename__ = 'Planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    population = db.Column(db.String(50), nullable=False)
    terrain = db.Column(db.String(15), nullable=False)
    climate = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
        "id": self.id,
        "name": self.name,
        "population": self.population,
        "terrain": self.terrain,
        "climate": self.climate
        }

class People(db.Model):
    __tablename__ = 'People'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(15), nullable=False)
    eye_color = db.Column(db.String(25), nullable=False)
    skin_color = db.Column(db.String(25), nullable=False)
    height = db.Column(db.String(25), nullable=False)

    def serialize(self):
        return {
        "id": self.id,
        "name": self.name,
        "gender": self.gender,
        "eye_color": self.eye_color,
        "skin_color": self.skin_color,
        "height": self.height
        }


class Favorites(db.Model):
    __tablename__ = 'Favorites'
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.Integer, db.ForeignKey ('People.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey ('Planet.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    people = db.relationship('People', lazy = True)
    planet = db.relationship('Planet', lazy = True)
    user = db.relationship('User', foreign_keys= [user_id])

    
    def __repr__(self):
       
        return f'<Favorites {self.people, self.planet_id}>'

    def serialize(self):
        return {
            "id": self.id,
            "people_id": self.people,
            "planet_id": self.planet_id,
            "user_id": self.user_id
            # do not serialize the password, its a security breach
        }