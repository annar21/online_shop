from flask import Flask

def init():
    app = Flask(__name__)

    from app.controllers.sellers_controller import sellers_bp
    app.register_blueprint(sellers_bp, url_prefix="/sellers")

    return app