from flask import Blueprint

sellers_bp = Blueprint("sellers", __name__)

@sellers_bp.route("/")
def home():
    return {"msg": "Success"}, 200