import os
from flask import Flask, render_template, request, redirect

user_list = {}


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/home")
    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/login')
    def login():
        return render_template("login.html")

    @app.route('/signup')
    def signup():
        return render_template("signup.html")

    @app.route('/about')
    def about():
        return render_template("about.html")

    @app.route('/resume')
    def resume():
        return render_template("resume.html")

    @app.route('/signup-data', methods=['POST'])
    def signup_data():
        name = request.form['name']
        email = request.form['email']
        user_list[str(name)] = str(email)
        print(str("User Name: " +
                  request.form['name'] + " User Email: " + request.form['email']))
        return redirect('/')

    @app.route('/user_list')
    def users():
        return render_template("user_list.html", user_list=user_list)

    from . import db
    db.init_app(app)

    return app
