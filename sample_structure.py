from flask import Flask
from goodbye import GoodByeRouter
from hello import HelloRouter

def create_app():
    app = Flask(__name__)

    from database import db
    db.init_app(app)

    app.register_blueprint(HelloRouter.hello_router)
    app.register_blueprint(GoodByeRouter.goodbye_router)

    return app

if __name__ == "__main__":
    create_app().run()