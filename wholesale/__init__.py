""" """
import os
from flask import Flask, render_template, session, g, url_for
from wholesale.db import get_db

def create_app(test_config=None):
    """
    Create and configure the application (app factory method).

    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        MYSQL_HOST='localhost',
        MYSQL_USER='root',
        MYSQL_PASS='justapassword',
        MYSQL_DB='wholesale',
        TIME_FMT='%Y-%m-%d %H:%M', # e.g., 2018-10-01 15:45
        CONFIGURED=True
    )
    # --- END WARNING SECTION ---

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in at startup
        app.config.from_mapping(test_config)

    # ensure the instance directory exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # check whether first-time configuration is done already
    if not app.config['CONFIGURED']:
        # if not, only set up the setup blueprint
        pass    # NOTE: here we will eventually import the setup blueprint

    else:
        # since the app is configured, import & register the blueprints
        # add close_db() to the app context teardown
        from . import db
        db.init_app(app)

        @app.route('/')
        def testindex():
            try:
                dbcursor = get_db().cursor()
                num = dbcursor.execute(
                    'SELECT Name, Contact'
                    ' FROM user'
                    ' WHERE User_Id = 12345'
                )
                testdata = dbcursor.fetchone()
                return render_template('index.html', testdata=testdata)
            except:
                return render_template('index.html')

        @app.route('/test')
        def test():
            try:
                dbcursor = get_db().cursor()
                num = dbcursor.execute(
                    'SELECT Name, Contact'
                    ' FROM user'
                    ' WHERE User_Id = 12346'
                )
                testdata = dbcursor.fetchone()
                return render_template('index.html', testdata=testdata)
            except:
                return render_template('index.html')

    return app
