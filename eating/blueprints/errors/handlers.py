from flask import Blueprint, render_template


"""Errors Blueprint"""

errors = Blueprint("errors", "__name__")


@errors.app_errorhandler(404)
def error_404(error):
    return (
        render_template("errors/404.html"),
        404,
    )  # 2nd argument in render_template is optional error code. 200 is default, why other routes don't include it


@errors.app_errorhandler(403)
def error_403(error):
    return render_template("errors/403.html"), 403


@errors.app_errorhandler(500)
def error_500(error):
    return render_template("errors/500.html"), 500
