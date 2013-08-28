from flask import Blueprint
from user import UserDAO


class GoodByeRouter(object):
    goodbye_router = Blueprint('goodbye', __name__)

    @staticmethod
    @goodbye_router.route('/goodbye/<name>', methods=["GET"])
    def goodbye(name):
        user = UserDAO.get(name)
        if user:
            return "Goodbye %s" % user.name
        else:
            return "you haven't said hello yet", 400