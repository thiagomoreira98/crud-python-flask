from .ping import create_ping_api
from .user import create_user_api

def init_app(app):
  # app.register_blueprint(create_ping_api())
  app.register_blueprint(create_user_api())