from app import build_app
from app.routes import lobby_blueprint, code_block_blueprint
app = build_app()

if __name__ == '__main__':
    app.run()

