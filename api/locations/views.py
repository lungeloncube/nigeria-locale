import json

from flask import request
from flask_restx import Namespace, Resource

from ..models.users import User

locations_namespace = Namespace("locations", description="a namespace for locations")


@locations_namespace.route('/locations')
class GetAllLocations(Resource):
    """Gets all regions and states and lgas coordinates"""

    def get(self):
        pass


@locations_namespace.route('/lgas/all')
class GetAllLgas(Resource):
    """Gets all the lags locations"""

    def get(self):
        pass


@locations_namespace.route('/lgas')
class GetLgas(Resource):
    """Gets a all lgas data"""

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

    def get(self, name):
        pass


@locations_namespace.route('/city/<latitude>/<longitude>')
class GetPlaceByLatLong(Resource):
    """Get city by latlong"""

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


@locations_namespace.route('/region/<name>')
class GetPlaceByAddress(Resource):
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
