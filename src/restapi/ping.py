from crypt import methods
from flask import Blueprint, abort, jsonify
from flask_restful import Api, Resource
from datetime import datetime

bp = Blueprint("pingController", __name__, url_prefix="/api/ping")
api = Api(bp)

def create_ping_api():
    # api.add_resource(PingController.get, "/")
    return api


class PingController(Resource):

    def get(self):
        return jsonify({"message": "Server Online", "date": datetime.now()})
