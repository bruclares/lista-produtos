from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    from .controllers import product_controller

    app.register_blueprint(product_controller.bp)
    
    return app
