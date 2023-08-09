from app import build_app, create_db, print_db, drop_db
app = build_app()

if __name__ == '__main__':
    with app.app_context():
        create_db()
        print_db()
    app.run(debug=True)