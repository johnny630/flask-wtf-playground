from dotenv import load_dotenv
from flask import Flask

from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    app.config.update(
        SECRET_KEY='secret_key'
    )

    csrf.init_app(app)

    from .views import register_blueprints
    register_blueprints(app)

    return app