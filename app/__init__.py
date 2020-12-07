from dotenv import load_dotenv
from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.update(
        SECRET_KEY='secret_key'
    )

    from .views import register_blueprints
    register_blueprints(app)

    return app