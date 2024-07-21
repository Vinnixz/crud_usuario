from flask import Flask
from api.routes.access import access_blueprint


def register_routes(app: Flask):
    app.register_blueprint(access_blueprint)