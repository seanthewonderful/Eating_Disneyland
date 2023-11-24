from flask import Blueprint, render_template
from .utils import make_fountain_map, make_map
from eating.crud import get_all_restaurants, get_all_fountains

"""Map Blueprint"""

map_bp = Blueprint("map_bp", "__name__")


"""Map Routes """


@map_bp.route("/map")
def map():
    """Return restaurant map html"""

    make_map(get_all_restaurants())

    return render_template("disneyland_map.html")


@map_bp.route("/fountain_map")
def fountain_map():
    """Return fountain map html"""

    make_fountain_map(get_all_fountains())

    return render_template("fountain_map.html")


"""Custom image preview route"""


@map_bp.route("/hp_image_preview")
def hp_image_preview():
    return render_template("hp_image_preview.html")
