from flask import Flask
from flask_cors import CORS
from .routes import lobby_blueprint, code_block_blueprint
from .events import socketio
from .code_block import db, DBCodeBlock
from .data import dummy_data
from config.config import *


def build_app():
    """Creates a Flask application with the necessary configuration and extensions."""
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config['CORS_HEADERS'] = CORS_HEADERS
    db.init_app(app)
    app.register_blueprint(lobby_blueprint)
    app.register_blueprint(code_block_blueprint)
    CORS(app)
    socketio.init_app(app, cors_allowed_origins="*")
    return app


def create_db():
    """Creates the database tables."""
    db.create_all()
    init_db()


def drop_db():
    """Drops the database tables."""
    db.drop_all()


def init_db():
    """Initializes the database with dummy data."""
    if DBCodeBlock.query.count() == 0:
        for id, cb in dummy_data.items():
            db_code_block = DBCodeBlock(id=id, title=cb.get_title(), code=cb.get_code(), solution=cb.get_solution())
            db.session.add(db_code_block)
        db.session.commit()

