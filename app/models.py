from flask_login import UserMixin
from app.db import db

class UserData:
    def __init__(self, username, password, usertype):
        self.username = username
        self.password = password
        self.usertype = usertype


class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        :param user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password
        self.usertype = user_data.usertype

    @staticmethod
    def query(username):
        user_doc = db.session.execute(f"SELECT * FROM users WHERE username = '{username}';").fetchone()
        user_data = UserData(
            username=user_doc.username,
            password=user_doc.password,
            usertype=user_doc.usertype
        )

        return UserModel(user_data)
