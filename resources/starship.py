from flask_restful import Resource, reqparse
from models.starship import StarshipModel


class Starship(Resource):
    """Create a parser and specify
    the arguments expected from the request"""
    parser = reqparse.RequestParser()
    parser.add_argument(
        'hyperdrive',
        type=float,
        required=True,
        help="Hyperdrive field cannot be left blank!"
        )
    parser.add_argument(
        'atmospheric-speed',
        type=float,
        required=True,
        help="Max speed field cannot be left blank!"
        )
    parser.add_argument(
        'affiliation_id',
        type=int,
        required=True,
        help="Select an affiliation!"
        )

    def get(self, name):
        """Retrieve a starship"""
        starship = StarshipModel.find_by_name(name)
        if starship:
            return starship.json()  # JSONify the starship.
        return {"message": "Starship not found"}, 404

    def post(self, name):
        """Create a new starship"""
        starship = StarshipModel.find_by_name(name)
        if starship is not None:
            return {"message":
                    f"A starship with name '{name}'' already exists"
                    }, 400

        # This line of code was moved down here
        # following the Error First Approach.
        request_data = Starship.parser.parse_args()
        starship = StarshipModel(name,
                                 request_data["hyperdrive"],
                                 request_data["atmospheric-speed"],
                                 request_data["affiliation_id"])
        try:
            starship.upsert()
        except Exception:
            return {
                "message":
                "An error occurred during the insertion of the starship."
                }, 500

        return starship.json(), 201

    # @jwt_required()
    def delete(self, name):
        """Delete a starship"""
        starship = StarshipModel.find_by_name(name)
        if starship:
            starship.delete()
        return {"message": "Starship destroyed!"}

    def put(self, name):
        """Update or create a new starship"""
        # Get the information from the parser.
        request_data = Starship.parser.parse_args()
        # Check if the starship already exists.
        starship = StarshipModel.find_by_name(name)
        # If the starship already exists...
        if starship:
            # ...update its information.
            try:
                starship.hyperdrive = request_data["hyperdrive"]
                starship.atmosphericSpeed = request_data["atmospheric-speed"]
                starship.affiliation_id = request_data["affiliation_id"]
                return {"message":
                        "Starship successfully edited.",
                        "Starship": starship.json()
                        }
            except Exception:
                return {
                    "message": "An error occurred during the update operation."
                    }, 500
        else:
            # If the starship doesn't exist, create it.
            try:
                starship = StarshipModel(name,
                                         request_data["hyperdrive"],
                                         request_data["atmospheric-speed"],
                                         request_data["affiliation_id"])
                starship.upsert()
                return {"message":
                        "Starship successfully created.",
                        "Starship": starship.json()
                        }
            except Exception:
                return {"message":
                        "An error occurred during the \
                            creation of the starship."
                        }, 500


class StarshipList(Resource):
    """Return all the starships, ordered by hyperdrive."""
    def get(self):
        return {"starships":
                [starship.json() for starship in
                 StarshipModel.query.order_by(StarshipModel.hyperdrive).all()]
                }
        # return {"starships": list(map(lambda starship: starship.json(),
        #                               StarshipModel.query.all()))}
