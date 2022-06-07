from src.ext.database import db

def init_app(app):
  db.create_all(app=app)