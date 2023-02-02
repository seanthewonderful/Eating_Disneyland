from src.server import app

if __name__ == "__main__":
    # app.jinja_env.auto_reload = app.debug
    # DebugToolbarExtension(app)
    # connect_to_db(app)
    app.run(debug=False)