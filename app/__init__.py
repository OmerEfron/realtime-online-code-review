from flask import Flask
from .routes import lobby_blueprint, code_block_blueprint
from .events import socketio
def build_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "The Diamond of the south - 24 in red"
    app.register_blueprint(lobby_blueprint)
    app.register_blueprint(code_block_blueprint)
    socketio.init_app(app)
    return app
