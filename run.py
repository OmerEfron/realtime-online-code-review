from app import build_app, create_db
app = build_app()

if __name__ == '__main__':
    with app.app_context():
        create_db() # to create the manually database
    app.run(host="0.0.0.0", port=5000)