from flask import Blueprint
from user import UserDAO, UserRecord


class HelloRouter(object):
    hello_router = Blueprint('hello', __name__)

    @staticmethod
    @hello_router.route('/hello', methods=["GET"])
    def hello():
        return "hello"


    @staticmethod
    @hello_router.route('/hello/<name>', methods=["GET"])
    def hello_name(name):
        user = UserDAO.save(UserRecord(name))
        return "name %s added" % user.name