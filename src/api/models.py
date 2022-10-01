from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
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

class Planets(db.Model):
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