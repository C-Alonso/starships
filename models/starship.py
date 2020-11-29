from db import db
from models.affiliation import AffiliationModel


class StarshipModel(db.Model):
    """SQLAlchemy SET UP for Starship"""
    __tablename__ = 'starships'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    hyperdrive = db.Column(db.Float(precision=2))
    atmosphericSpeed = db.Column(db.Float(precision=2))

    affiliation_id = db.Column(db.Integer, db.ForeignKey('affiliations.id'))
    affiliation = db.relationship('AffiliationModel')

    def __init__(self, name, hyperdrive, atmosphericSpeed, affiliation_id):
        self.name = name
        self.hyperdrive = hyperdrive
        self.atmosphericSpeed = atmosphericSpeed
        self.affiliation_id = affiliation_id

    def json(self):
        return {
            "name": self.name,
            "hyperdrive": self.hyperdrive,
            "atmospheric-speed": self.atmosphericSpeed,
            # Get the name of the Affiliation.
            "affiliation":
            AffiliationModel.find_by_id(self.affiliation_id).name
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def upsert(self):
        """Create or update a starship"""
        db.session.add(self)  # Session is a collection of objects.
        db.session.commit()

    def delete(self):
        """Delete a starship"""
        db.session.delete(self)
        db.session.commit()
