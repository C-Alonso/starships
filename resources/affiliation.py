from flask_restful import Resource
from models.affiliation import AffiliationModel
from flask_jwt import jwt_required


class Affiliation(Resource):
    def get(self, name):
        affiliation = AffiliationModel.find_by_name(name)
        if affiliation:
            return affiliation.json()
        return {"message": "Affiliation non-existent."}

    def post(self, name):
        if AffiliationModel.find_by_name(name):
            return {"message": f"{name} affiliation already exists."}, 400

        affiliation = AffiliationModel(name)
        try:
            affiliation.upsert()
        except Exception:
            return {"message":
                    "An error occurred while creating the affiliation."}, 500

        return affiliation.json(), 201

    @jwt_required()
    def delete(self, name):
        """Delete an affiliation"""
        affiliation = AffiliationModel.find_by_name(name)
        if affiliation:
            affiliation.delete()

        # The message is sent regardless of wheather
        # the Affiliation exists or not.
        return {"message": "Affiliation destroyed!"}


class AffiliationList(Resource):
    def get(self):
        return {"affiliations": [affiliation.json_name()
                                 for affiliation
                                 in AffiliationModel.query.all()]}
