from database import db
from ._user_record import UserRecord


class UserDAO(object):
    @classmethod
    def save(cls, user):
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def get(cls, name):
        return UserRecord.query.filter(name=name).first()