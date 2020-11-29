# STAR WARS Starships API

This application returns the Starships from Star Wars, ordered by hyperdrive.
Built with *Flask*, *Flask RESTful*, *Flask JWT*, and *Flask-SQLAlchemy*.

## Installation

The application is deployed on **Heroku**:
**[https://dashboard.heroku.com/apps/starships-ag](https://dashboard.heroku.com/apps/starships-ag)**

If you prefer to run it locally:

1. Download this Code
2. Install the following packages with [pip](https://pip.pypa.io/en/stable/):

```bash
pip install Flask
pip install Flask-RESTful
pip install Flask-JWT
pip install Flask-SQLAlchemy
python app_run_local.py
```

3. Run the server!

```bash
python app_run_local.py
```


## Usage

This API gives you access to two types of resources: **Affiliations** and **starships**.

### Starships

STARSHIPS:

A *starship* contains 4 parameters:
```json
{
    "name": "Slave I",
    "hyperdrive": 0.7,
    "atmospheric-speed": 1000.0,
    "affiliation": "Galactic Empire"
}
```
ENDPOINTS:

Retrieve all the starships, ordered by hyperdrive:
> GET https://starships-ag.herokuapp.com/starships

Retrieve a specific starship (by name):
> GET https://starships-ag.herokuapp.com/starship/<string:name>

Create a new starship:
> POST https://starships-ag.herokuapp.com/starship/<string:name>

include *JSON* body:


```json
{    
    "hyperdrive": (float),
    "atmospheric-speed": (float),
    "affiliation": (affiliation id)
}
```
*You can find an Affiliation ID by using the Affiliations endpoints.*

**Delete** a specific starship (requires JWT authentication):
> DELETE https://starships-ag.herokuapp.com/starship/<string:name>

### Affiliations

An *Affiliation* contains 1 parameter:
```json
{
    "name": "Rebel Alliance"
}
```
ENDPOINTS:

**Retrieve** all the affiliations:
> GET https://starships-ag.herokuapp.com/affiliations

**Retrieve** a specific affiliation (by name):
> GET https://starships-ag.herokuapp.com/affiliation/<string:name>

**Create** a new affiliation:
> POST https://starships-ag.herokuapp.com/affiliation/<string:name>

**Delete** a specific affiliation (requires JWT authentication):
> DELETE https://starships-ag.herokuapp.com/affiliation/<string:name>


## License
[MIT](https://choosealicense.com/licenses/mit/)
