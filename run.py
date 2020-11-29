from app import app
from db import db
from create_tables import create_affiliations, create_starships
from models.starship import StarshipModel

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()
    # Load the DB if it's empty.
    if not StarshipModel.query.all():
        create_affiliations()
        create_starships()
