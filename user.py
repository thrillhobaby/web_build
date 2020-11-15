import uuid
from src.common.database import Database


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one('users', {'email': email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one('users', {'email': id})
        if data is not None:
            return cls(**data)


    @staticmethod
    def login_valid(email, password):
        # user.login_valid('user_email@gmail.com', 'password1234')
        # check if email matches password
        user = User.get_by_email(email)
        if user is not None:
            # check password
            return user.password == password
        return False

    @classmethod
    def register(cls, email, password):
        user = User.get_by_email(email)
        if user is None:
            # user doesn't exist, create it
            new_user = User(email, password)
            new_user.save_to_mongo()
            return True
        else:
            # user exists :0
            return False

    def login(self):
        pass

    def get_blogs(self):
        pass

    def json(self):
        pass

    def save_to_mongo(self):
        pass




