"""Creation of database objects: Affiliations and Starships"""
import os
import json
from models.starship import StarshipModel
from models.affiliation import AffiliationModel


SITE_ROOT = os.path.realpath(os.path.dirname(__file__))


def create_affiliations():
    AFFILIATIONS_FILE = os.path.join(SITE_ROOT, "dbfiles", "affiliations.json")
    a = open(AFFILIATIONS_FILE)
    affiliations = json.load(a)
    a.close()

    for affiliation in affiliations:
        new_affiliation = AffiliationModel(**affiliation)
        new_affiliation.upsert()


def create_starships():
    STARSHIPS_FILE = os.path.join(SITE_ROOT, "dbfiles", "starships.json")
    s = open(STARSHIPS_FILE)
    starships = json.load(s)
    s.close()

    for starship in starships:
        new_starship = StarshipModel(**starship)
        new_starship.upsert()
