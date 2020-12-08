from .index import index_bp
from .field_view import field_view_bp
from .validator_view import validator_view_bp

def register_blueprints(app):
    app.register_blueprint(field_view_bp, url_prefix='/field')
    app.register_blueprint(validator_view_bp, url_prefix='/validator')
    app.register_blueprint(index_bp, url_prefix='/')
