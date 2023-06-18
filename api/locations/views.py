import json

from flask import request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_restx import Namespace, Resource
from app import app

from ..models.users import User

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per day", "1000 per second"],
    storage_uri="memory://")

locations_namespace = Namespace("locations", description="a namespace for locations")


@locations_namespace.route('/lgas/<name>')
class GetAllLgas(Resource):
    """Gets all the lags locations"""

    @limiter.limit("5 per hour")
    def get(self, name):
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') is not None:
            api_key = request.headers.get('x-api-key')
            user = User.query.filter_by(api_key=api_key).first()

            if user is not None:
                with open('static/clean_lgas.json', 'r') as f:
                    data = json.load(f)
                    output_dict = [x for x in data if x['admin2Name'] == name]

                    return output_dict
            else:
                return {"message": "Please provide a valid key"}, 400

        else:
            return {"message": "Please provide an API key"}, 400


@locations_namespace.route('/lgas')
class GetLgas(Resource):
    """Gets a all lgas data"""

    @limiter.limit("5 per hour")
    def get(self):
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') is not None:
            api_key = request.headers.get('x-api-key')
            user = User.query.filter_by(api_key=api_key).first()

            if user is not None:
                with open('static/clean_lgas.json', 'r') as f:
                    data = json.load(f)

                    return data
            else:
                return {"message": "Please provide a valid key"}, 400

        else:
            return {"message": "Please provide an API key"}, 400


@locations_namespace.route('/states')
class GetStates(Resource):
    """Gets all states coordinates"""

    @limiter.limit("2 per hour")
    def get(self):

        if request.headers.get('x-api-key') and request.headers.get('x-api-key') is not None:
            api_key = request.headers.get('x-api-key')
            user = User.query.filter_by(api_key=api_key).first()

            if user is not None:
                with open('static/cities.json', 'r') as f:
                    data = json.load(f)
                    return data
            else:
                return {"message": "Please provide a valid key"}, 400

        else:
            return {"message": "Please provide an API key"}, 400


@locations_namespace.route('/city/<city_name>')
class GetState(Resource):
    """Gets a single city coordinates"""

    @limiter.limit("2 per hour")
    def get(self, city_name):

        if request.headers.get('x-api-key') and request.headers.get('x-api-key') is not None:
            api_key = request.headers.get('x-api-key')
            user = User.query.filter_by(api_key=api_key).first()

            if user is not None:
                # Transform json input to python objects
                with open('static/cities.json', 'r') as f:
                    data = json.load(f)
                    # Filter python objects with list comprehensions
                    output_dict = [x for x in data if x['name'] == city_name]
                    #
                    # # Transform python object back into json
                    # output_json = json.dumps(output_dict)
                    return output_dict
            else:
                return {"message": "Please provide a valid key"}, 400

        else:
            return {"message": "Please provide an API key"}, 400


@locations_namespace.route('/state/<state_name>')
class GetState(Resource):
    """Gets a single city coordinates"""

    @limiter.limit("2 per hour")
    def get(self, state_name):

        if request.headers.get('x-api-key') and request.headers.get('x-api-key') is not None:
            api_key = request.headers.get('x-api-key')
            user = User.query.filter_by(api_key=api_key).first()

            if user is not None:
                # Transform json input to python objects
                with open('static/cities.json', 'r') as f:
                    data = json.load(f)
                    # Filter python objects with list comprehensions
                    output_dict = [x for x in data if x['state_or_region'] == state_name]
                    return output_dict
            else:
                return {"message": "Please provide a valid key"}, 400

        else:
            return {"message": "Please provide an API key"}, 400


@locations_namespace.route('/place/<name>')
class GetPlaceByName(Resource):
    """gets  cordinates by place name"""

    @limiter.limit("2 per hour")
    def get(self, name):
        pass


@locations_namespace.route('/city/<latitude>/<longitude>')
class GetPlaceByLatLong(Resource):
    """Get city by latlong"""

    @limiter.limit("2 per hour")
    def get(self, latitude, longitude):
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') is not None:
            api_key = request.headers.get('x-api-key')
            user = User.query.filter_by(api_key=api_key).first()

            if user is not None:
                # Transform json input to python objects
                with open('static/zw-ng.json', 'r') as f:
                    data = json.load(f)
                    # Filter python objects with list comprehensions
                    output_dict = [x for x in data if x['lat'] == latitude and x['lng'] == longitude]
                    if output_dict:
                        return output_dict[0]
                    else:
                        return {"message": "Nothing found"}, 404
            else:
                return {"message": "Please provide a valid key"}, 400

        else:
            return {"message": "Please provide an API key"}, 400


@locations_namespace.route('/regions')
class GetRegions(Resource):
    """Gets all the regions with their states """

    @limiter.limit("2 per hour")
    def get(self):
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') is not None:
            api_key = request.headers.get('x-api-key')
            user = User.query.filter_by(api_key=api_key).first()

            if user is not None:
                # Transform json input to python objects
                with open('static/nr_regions.json', 'r') as f:
                    data = json.load(f)
                    # Filter python objects with list comprehensions

                    return data
            else:
                return {"message": "Please provide a valid key"}, 400

        else:
            return {"message": "Please provide an API key"}, 400


@locations_namespace.route('/region/state/<name>')
class GetRegion(Resource):
    """Gets  the region name using state name """

    @limiter.limit("2 per hour")
    def get(self, name):
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') is not None:
            api_key = request.headers.get('x-api-key')
            user = User.query.filter_by(api_key=api_key).first()

            if user is not None:
                # Transform json input to python objects
                with open('static/nr_regions.json', 'r') as f:
                    data = json.load(f)
                    # Filter python objects with list comprehensions

                    output_dict = [x for x in data if name in x['states']]
                    if output_dict:
                        return {"region": output_dict[0]['name']}
                    else:
                        return {"message": "Nothing found"}, 404
            else:
                return {"message": "Please provide a valid key"}, 400

        else:
            return {"message": "Please provide an API key"}, 400


@locations_namespace.route('/region/<name>/detailed/cities')
class GetRegionByName(Resource):

    @limiter.limit("2 per hour")
    def get(self, name):
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') is not None:
            api_key = request.headers.get('x-api-key')
            user = User.query.filter_by(api_key=api_key).first()

            if user is not None:
                # Transform json input to python objects
                with open('static/nr_regions.json', 'r') as f:
                    data = json.load(f)
                with open('static/cities.json', 'r') as g:
                    cities = json.load(g)

                    # Filter python objects with list comprehensions
                    output_dict = [x for x in data if x['name'] == name]
                    new_dict = []
                    if output_dict:
                        for state in output_dict[0]["states"]:
                            for city in cities:
                                if state == city["state_or_region"]:
                                    new_dict.append(city)

                    return new_dict
            else:
                return {"message": "Please provide a valid key"}, 400

        else:
            return {"message": "Please provide an API key"}, 400


@locations_namespace.route('/country/<name>/cities')
class GetRegion(Resource):
    """Gets  the cities  using country name """

    @limiter.limit("2 per hour")
    def get(self, name):
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') is not None:
            api_key = request.headers.get('x-api-key')
            user = User.query.filter_by(api_key=api_key).first()

            if user is not None:
                # Transform json input to python objects
                with open('static/zw-ng.json', 'r') as f:
                    data = json.load(f)
                    # Filter python objects with list comprehensions

                    output_dict = [x for x in data if name in x['country']]
                    return output_dict
            else:
                return {"message": "Please provide a valid key"}, 400

        else:
            return {"message": "Please provide an API key"}, 400


@locations_namespace.route('/region/<name>/detailed/cities/lgas')
class GetRegionByName(Resource):

    @limiter.limit("2 per hour")
    def get(self, name):
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') is not None:
            api_key = request.headers.get('x-api-key')
            user = User.query.filter_by(api_key=api_key).first()

            if user is not None:
                # Transform json input to python objects
                with open('static/nr_regions.json', 'r') as f:
                    data = json.load(f)
                with open('static/cities.json', 'r') as g:
                    cities = json.load(g)

                with open('static/clean_lgas.json', 'r') as s:
                    lgas = json.load(s)

                    # Filter python objects with list comprehensions
                    output_dict = [x for x in data if x['name'] == name]
                    new_dict = []
                    consolidated_list = []
                    if output_dict:
                        for state in output_dict[0]["states"]:
                            for city in cities:
                                if state == city["state_or_region"]:
                                    new_dict.append(city)
                    if new_dict is not None:
                        for item in new_dict:
                            output_dict = [x for x in lgas if x['admin1Name'] == item['state_or_region']]

                            new_item = {
                                "city": item["name"],
                                "state": item["state_or_region"],
                                "latitude": item["latitude"],
                                "longitude": item["longitude"],
                                "lgas": output_dict
                            }
                            consolidated_list.append(new_item)

                    return consolidated_list
            else:
                return {"message": "Please provide a valid key"}, 400

        else:
            return {"message": "Please provide an API key"}, 400


@locations_namespace.route("/country/<name>")
class Country(Resource):

    def get(self, name):
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') is not None:
            api_key = request.headers.get('x-api-key')
            user = User.query.filter_by(api_key=api_key).first()
            if user is not None:
                return name
            else:
                return {"message": "Please provide a valid key"}, 400

        else:
            return {"message": "Please provide an API key"}, 400
