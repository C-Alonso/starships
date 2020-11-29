from db import db


class AffiliationModel(db.Model):
    """SQLAlchemy SET UP for Affiliation"""
    __tablename__ = 'affiliations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    starships = db.relationship('StarshipModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            "id": self.id
            "name": self.name,
            "starships": [starship.json()
                          for starship
                          in self.starships.all()]
        }

    def json_name(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def upsert(self):
        """Insert or Update a new Affiliation"""
        db.session.add(self)  # Session is a collection of objects.
        db.session.commit()

    def delete(self):
        """Delete an Affiliation"""
        db.session.delete(self)
        db.session.commit()
