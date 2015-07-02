from flask import Blueprint
from simple_flask_blueprint.core.blueprint_core import say_hallo


bp = Blueprint('simple_flask_blueprint', __name__)


@bp.route('/')
def discovery():
    return say_hallo()
