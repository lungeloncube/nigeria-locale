import json

from flask_restx import Namespace, Resource

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
    """Gets a single lga coordinates"""

    def get(self):
        pass


@locations_namespace.route('/states')
class GetStates(Resource):
    """Gets all states coordinates"""

    def get(self):
        with open('static/states_list.json', 'r') as f:
            data = json.load(f)
            return data


@locations_namespace.route('/state')
class GetState(Resource):
    """Gets a single state coordinates"""

    def get(self):
        pass


@locations_namespace.route('/place/<name>')
class GetPlaceByName(Resource):
    """gets  cordinates by place name"""

    def get(self, name):
        pass


@locations_namespace.route('/lace/<Lat>/<Long>')
class GetPlaceByLatLong(Resource):
    """Get place by latlong"""

    def get(self, lat, long):
        pass


@locations_namespace.route('/regions')
class GetRegions(Resource):
    """Gets all the regions cordinates """

    def get(self):
        pass


@locations_namespace.route('/region')
class GetRegion(Resource):
    def get(self):
        pass


@locations_namespace.route('/place/<address>')
class GetPlaceByAddress(Resource):
    def get(self, address):
        pass
