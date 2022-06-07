from flask import Blueprint, abort, jsonify
from flask_restful import Api, Resource
from src.models.user import User

bp = Blueprint("restapi_user", __name__, url_prefix="/api/users")
api = Api(bp)

def create_user_api():
    api.add_resource(UserController.Get, "/")
    # api.add_resource(UserController.getById, "/<id>")
    return bp


class UserController():

    class Get(Resource):
        def get(self):
            users = User.query.all() or abort(204)
            return jsonify(
                {"users": [user.to_dict() for user in users]}
            )

    def getById(self, id):
        user = User.query.filter_by(id=id).first() or abort(404)
        return jsonify(user.to_dict())
