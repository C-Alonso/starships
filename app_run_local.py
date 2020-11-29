import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import authenticate, identity
from resources.user import UserRegister
from resources.starship import Starship, StarshipList
from resources.affiliation import Affiliation, AffiliationList
from models.starship import StarshipModel
from create_tables import create_affiliations, create_starships


app = Flask(__name__)  # Create an object of the Flask class.
app.config["SQLALCHEMY_DATABASE_URI"] = \
                        os.environ.get('DATABASE_URL',
                                       'sqlite:///data.db')  # Default value.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'MUCH_SECRET'
api = Api(app)


# Generate DB data before the first request
@app.before_first_request
def create_tables():
    db.create_all()
    #if not os.path.isfile("data.db"):  # True if DB hasn't been created.
    # Load the DB if it's empty.
    if not StarshipModel.query.all():        
        create_affiliations()
        create_starships()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(UserRegister, '/register')
api.add_resource(Starship, '/starship/<string:name>')
api.add_resource(StarshipList, '/starships')
api.add_resource(Affiliation, '/affiliation/<string:name>')
api.add_resource(AffiliationList, '/affiliations')

# So it doesn't get run when imported elsewhere.
DEBUG_MODE = False if os.environ.get('ON_HEROKU') else True
if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=DEBUG_MODE)
