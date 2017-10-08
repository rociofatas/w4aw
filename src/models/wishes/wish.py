import uuid

from src.common.database import Database
import src.models.wishes.constants as WishConstants


class Wish(object):
    def __init__(self, wish, wish_keyword, user_email, _id=None):
        self.wish = wish
        self.wish_keyword = wish_keyword
        self.user_email = user_email
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<I wish for a world {}".format(self.wish)

    def save_to_mongo(self):
        Database.update(WishConstants.COLLECTION, {"_id": self._id}, self.json())

    def json(self):
        return {
            "_id": self._id,
            "wish": self.wish,
            "wish_keyword": self.wish_keyword,
            "user_email": self.user_email
        }

    @classmethod
    def get_by_id(cls, id):
        return cls(**Database.find_one(WishConstants.COLLECTION, {"_id": id}))


    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find(WishConstants.COLLECTION, {})]


    @classmethod
    def find_by_user_email(cls, user_email):
        return [cls(**elem) for elem in Database.find(WishConstants.COLLECTION, {'user_email': user_email})]

