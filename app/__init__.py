from flask import Flask
from .routes import lobby_blueprint, code_block_blueprint
from .events import socketio
from .code_block import db, DBCodeBlock
from .data import dummy_data
def build_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "The Diamond of the south - 24 in red"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///code_blocks.db"
    db.init_app(app)
    app.register_blueprint(lobby_blueprint)
    app.register_blueprint(code_block_blueprint)
    socketio.init_app(app)
    return app

def create_db():
    db.create_all()
    init_db()

def drop_db():
    db.drop_all()
def init_db():
    if DBCodeBlock.query.count() == 0:
        for id, cb in dummy_data.items():
            print(f"creating code block {id}")
            db_code_block = DBCodeBlock(id=id, title=cb.get_title(), code=cb.get_code(), solution=cb.get_solution())
            db.session.add(db_code_block)
        db.session.commit()

